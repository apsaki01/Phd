#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
  Hide & Seek — Graph-as-Policy (GaP) two-team self-learning harness
  ─────────────────────────────────────────────────────────────────────────────
  Re-implementation of the GaP methodology (Chen et al., arXiv:2607.05369) for
  the quadrant hide-and-seek scenario.  Instead of a neural policy trained with
  PPO (train_ada.py), each TEAM is controlled by a directed computation graph
  built from a small library of atomic skills (perception / planning / control
  nodes).  There is ONE graph for the hiders and ONE graph for the seekers.

  GaP self-learning loop (Algorithm 1 of the paper), adapted to a 2-team game:
      1. Scene variational sampling  – sample N task instances from the belief
         space B (door configuration p_door ∈ TASK_SPACE, random spawn seeds).
      2. Parallel rehearsal          – roll the candidate graph out against the
         opponent team's graph in N worker processes (MuJoCo).
      3. Failure analysis            – structured per-episode diagnostics
         (who was seen, when, where; which segments timed out; object states).
      4. Graph update                – propose modified graphs (swap nodes,
         re-wire segments, change parameters), re-rehearse, keep the best.
         Updates come from an LLM coding agent when GAP_LLM_API_KEY is set
         (the paper's mechanism) and otherwise from a failure-weighted
         structural search over the same graph grammar.
      5. Alternate the learning team (hiders ↔ seekers) → autocurriculum.

  The skill library deliberately contains ONLY primitive skills (move / face /
  grab / release / lock / route through a door / flee / chase / search).  No
  skill encodes "block the door" or "hide the ramp"; those strategies must be
  COMPOSED by the graph search, which is what makes their appearance an
  emergent-behaviour result comparable to the PPO runs.

  Emergent-behaviour detectors (computed from simulator state every episode):
      chasing, door_blocking, seeker_ramp_use, hider_ramp_defense.

  Usage:
      SMOKE_TEST=1      python3 train_gap.py      # ~1 min end-to-end check (tiny budget)
      GAP_ORACLE_TEST=1 python3 train_gap.py      # validate skills + detectors with hand-written graphs
      bash run_gap.sh                             # full 43.4M-episode run (resumable)
      python3 render_gap.py                       # render the current best graphs to MP4
═══════════════════════════════════════════════════════════════════════════════
"""
import os, re, sys, time, json, copy, random, signal, traceback, urllib.request, urllib.error
import queue, threading
import multiprocessing as mp
from collections import defaultdict, deque
from concurrent.futures import Future

# one BLAS/OpenMP thread per rehearsal worker (28 workers would otherwise oversubscribe the CPU)
for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(REPO_DIR)  # shared env folders live at the Phd repo root
sys.path.insert(0, os.path.join(ROOT_DIR, 'mujoco-worldgen'))
sys.path.insert(0, os.path.join(ROOT_DIR, 'multi-agent-emergence-environments'))

os.environ.setdefault('MUJOCO_PY_MJPRO_PATH', os.path.expanduser('~/.mujoco/mjpro150'))
os.environ.setdefault('MUJOCO_PY_MJKEY_PATH', os.path.expanduser('~/.mujoco/mjkey.txt'))
os.environ.setdefault('MUJOCO_GL', 'osmesa')
_mujoco_bin = os.path.join(os.environ['MUJOCO_PY_MJPRO_PATH'], 'bin')
_ld = os.environ.get('LD_LIBRARY_PATH', '')
if _mujoco_bin not in _ld.split(os.pathsep):
    os.environ['LD_LIBRARY_PATH'] = _mujoco_bin + (os.pathsep + _ld if _ld else '')

import gym, gym.spaces
if not hasattr(gym.spaces, 'dict_space'):
    gym.spaces.dict_space = gym.spaces.dict
if not hasattr(gym.spaces, 'tuple_space'):
    gym.spaces.tuple_space = gym.spaces.tuple
import warnings
warnings.filterwarnings('ignore')

from mae_envs.envs.hide_and_seek import make_env
from mujoco_worldgen.util.sim_funcs import qpos_idxs_from_joint_prefix, qvel_idxs_from_joint_prefix


# ═════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═════════════════════════════════════════════════════════════════════════════

class Config:
    seed              = int(os.environ.get('SEED', '0'))
    n_workers         = int(os.environ.get('GAP_WORKERS', '14'))   # container cgroup quota is ~15 CPUs; 12-14 workers saturate it (~22 eps/s)
    total_episodes    = int(os.environ.get('GAP_TOTAL_EPISODES', '43400000'))  # rehearsal-episode budget (same as run4)
    iterations        = int(os.environ.get('GAP_ITERS', '0'))        # 0 = unlimited (budget-driven)
    rehearsals        = int(os.environ.get('GAP_REHEARSALS', '100' if os.environ.get('GAP_LLM_ONLY') == '1' else '40'))  # task instances per candidate (N)
    candidates        = int(os.environ.get('GAP_CANDIDATES', '6'))   # proposed graphs per iteration
    pool_size         = 8          # past opponent graphs kept for rehearsal variety
    pool_prob         = 0.3        # probability an instance uses a past opponent graph
    plateau_patience  = 40         # iterations without improvement before exploration is boosted
    stop_on_plateau   = os.environ.get('GAP_STOP_ON_PLATEAU', '0') == '1'
    omniscient_objects = os.environ.get('GAP_OMNISCIENT_OBJECTS', '1') == '1'  # team-shared object poses (known workcell)
    # Environment (identical to train_ada.py / run4)
    n_hiders, n_seekers = 2, 2
    horizon, prep_fraction = 80, 0.4
    lock_ramp = False
    # Paths
    output_dir = os.path.abspath(os.environ.get('GAP_OUTPUT_DIR', os.path.expanduser('~/training_output_gap')))
    # Optional LLM graph-update agent (OpenAI-compatible chat endpoint)
    llm_api_key  = os.environ.get('GAP_LLM_API_KEY', '')
    llm_api_key_header = os.environ.get('GAP_LLM_API_KEY_HEADER', 'Authorization')
    llm_base_url = os.environ.get('GAP_LLM_BASE_URL', 'https://api.openai.com/v1')
    llm_model    = os.environ.get('GAP_LLM_MODEL', 'gpt-4o-mini')
    llm_only     = os.environ.get('GAP_LLM_ONLY', '0') == '1'      # no structural-search candidates
    llm_proposals = int(os.environ.get('GAP_LLM_PROPOSALS', '5' if llm_only else '1'))
    # several samples of the same prompt are only useful if they differ
    llm_temperature = float(os.environ.get('GAP_LLM_TEMPERATURE', '0.7' if llm_proposals > 1 else '0.3'))
    llm_repairs  = int(os.environ.get('GAP_LLM_REPAIRS', '1'))       # retries with the validator error
    # LLM writers run continuously; each round rehearses whatever proposals arrived in this window
    round_window = float(os.environ.get('GAP_ROUND_WINDOW', '45'))
    # J differences below this are mostly rehearsal noise
    accept_margin = float(os.environ.get('GAP_ACCEPT_MARGIN', '0.05'))

cfg = Config()
SMOKE = os.environ.get('SMOKE_TEST', '0') == '1'
ORACLE = os.environ.get('GAP_ORACLE_TEST', '0') == '1'
if SMOKE:
    cfg.n_workers, cfg.iterations, cfg.rehearsals, cfg.candidates = 2, 3, 4, 3
    cfg.total_episodes = 10 ** 9
    cfg.output_dir = os.path.abspath(os.environ.get('GAP_OUTPUT_DIR', os.path.expanduser('~/training_output_gap_smoke')))

ONSET_THRESHOLD = {'chasing': 0.3, 'door_blocking': 0.5, 'ramp_use': 0.3, 'ramp_defense': 0.5}
ABBR = {'chasing': 'chase', 'door_blocking': 'door', 'ramp_use': 'r_use', 'ramp_defense': 'r_def'}

ENV_KWARGS = dict(
    n_hiders=cfg.n_hiders, n_seekers=cfg.n_seekers,
    grab_box=True, grab_out_of_vision=False, grab_selective=False, grab_exclusive=False,
    lock_box=True, lock_type='all_lock_team_specific', lock_out_of_vision=False,
    n_substeps=15, horizon=cfg.horizon, scenario='quadrant',
    prep_fraction=cfg.prep_fraction, rew_type='joint_zero_sum',
    restrict_rect=[0.1, 0.1, 5.9, 5.9], p_door_dropout=0.5,
    quadrant_game_hider_uniform_placement=True, ramp_outside_quadrant=False,
    n_boxes=2, box_only_z_rot=True, boxid_obs=False,
    n_ramps=1, lock_ramp=cfg.lock_ramp, penalize_objects_out=True,
    n_food=0, n_lidar_per_agent=30, prep_obs=True)

TASK_SPACE = [1.0, 0.75, 0.5, 0.25, 0.0]          # p_door_dropout values (belief space B)
N_AGENTS = cfg.n_hiders + cfg.n_seekers
HIDERS = list(range(cfg.n_hiders))
SEEKERS = list(range(cfg.n_hiders, N_AGENTS))
PREP_STEPS = int(cfg.horizon * cfg.prep_fraction)
FLOOR, GRID = 6.0, 30
CELL = FLOOR / GRID
ACT_MAX = 0.9          # action_lims of the environment
N_BINS = 11


# ═════════════════════════════════════════════════════════════════════════════
# GRAPH GRAMMAR  (the "MORSL" skill library for hide-and-seek)
# ═════════════════════════════════════════════════════════════════════════════
#
# A team graph is a JSON-serialisable dict:
#   {
#     "team": "hider" | "seeker",
#     "assign": "fixed" | "nearest_object",       # role-assignment node
#     "params": {"gain":..,"damp":..,"tol":..,"offset":..,"seg_timeout":..},
#     "roles": [                                     # one role per agent slot
#        {"prep": [Segment,...], "play": {"behaviour": .., "target": .., "route": ..,
#                                          "segments": [Segment,...]}},
#        ...
#     ]
#   }
# Segment = {"acquire": null|"box"|"ramp", "deliver": Target|null, "lock": bool,
#            "release": bool, "face": "target"|"align"|"yaw0".."yaw3", "route": "door"|"direct",
#            "gate": null|Predicate}   # the segment starts only once the predicate holds
#
# Data edges: perception → planning (assign, target selection, routing) → control.
# Control edges: phase predicate (prep/play), segment-completion predicates,
# visibility predicates (chase/flee only when an opponent is perceived).

TARGETS = ['door_block', 'door_inside', 'quadrant_interior', 'quadrant_corner', 'ramp_inside', 'outside_wall',
           'climb', 'teammate', 'opponent', 'away_from_opponent', 'ramp', 'box',
           'wander', 'stay']
ACQUIRE = [None, 'box', 'ramp']
FACES = ['target', 'align', 'yaw0', 'yaw1', 'yaw2', 'yaw3']
ROUTES = ['door', 'direct']
BEHAVIOURS = ['stay', 'flee', 'chase', 'search', 'go', 'segments']
ASSIGNS = ['fixed', 'nearest_object']
GATES = [None, 'teammate_inside', 'ramp_inside', 'opponent_visible', 'doors_sealed', 'door']
PARAM_RANGES = {'gain': (1.0, 6.0), 'damp': (0.2, 0.8), 'tol': (0.2, 0.6),
                'offset': (0.0, 0.6), 'seg_timeout': (8, 40)}
RAMP_GAP = 0.38        # ramp centre-to-wall-line distance that leaves the ramp flush with the wall
V_MAX = 7.0            # m/s speed cap for the velocity controller (particle reaches ~9 m/s at full force)


def default_params():
    return {'gain': 4.0, 'damp': 0.5, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 30}


def minimal_graph(team):
    """Initial graphs: neutral for both teams (no chase, flee, or object use), so every
    behaviour, including chasing, has to be found by the graph search."""
    role = {'prep': [], 'play': {'behaviour': 'stay', 'target': 'stay',
                                 'route': 'door', 'segments': []}}
    return {'team': team, 'assign': 'fixed', 'params': default_params(),
            'roles': [copy.deepcopy(role) for _ in range(2)]}


def oracle_graphs():
    """Hand-written reference graphs used ONLY to validate that the primitive
    skills can physically realise the four behaviours (never used for training)."""
    hider = {'team': 'hider', 'assign': 'nearest_object', 'params': default_params(), 'roles': [
        {'prep': [{'acquire': 'box', 'deliver': 'door_inside', 'lock': False, 'release': False,
                   'face': 'target', 'route': 'door', 'gate': None},
                  {'acquire': None, 'deliver': 'door_block', 'lock': True, 'release': True,
                   'face': 'target', 'route': 'direct', 'gate': 'teammate_inside'},
                  {'acquire': 'box', 'deliver': 'door_block', 'lock': True, 'release': True,
                   'face': 'target', 'route': 'door', 'gate': None}],
         'play': {'behaviour': 'go', 'target': 'quadrant_corner', 'route': 'door', 'segments': []}},
        {'prep': [{'acquire': 'ramp', 'deliver': 'quadrant_corner', 'lock': False, 'release': True,
                   'face': 'target', 'route': 'door', 'gate': None},
                  {'acquire': 'box', 'deliver': 'door_block', 'lock': True, 'release': True,
                   'face': 'target', 'route': 'door', 'gate': None}],
         'play': {'behaviour': 'go', 'target': 'quadrant_interior', 'route': 'door', 'segments': []}}]}
    seeker = {'team': 'seeker', 'assign': 'nearest_object', 'params': default_params(), 'roles': [
        {'prep': [], 'play': {'behaviour': 'segments', 'target': 'opponent', 'route': 'door', 'segments': [
            {'acquire': 'ramp', 'deliver': 'outside_wall', 'lock': False, 'release': True,
             'face': 'align', 'route': 'door'},
            {'acquire': None, 'deliver': 'climb', 'lock': False, 'release': False,
             'face': 'target', 'route': 'direct'},
            {'acquire': None, 'deliver': 'opponent', 'lock': False, 'release': False,
             'face': 'target', 'route': 'direct'}]}},
        {'prep': [], 'play': {'behaviour': 'chase', 'target': 'opponent', 'route': 'door', 'segments': []}}]}
    return hider, seeker


def validate_graph(g, team, verbose=False, errors=None):
    """Static structural validation (GaP's graph validation step)."""
    try:
        assert isinstance(g, dict), 'root must be a JSON object'
        assert g['team'] == team, 'team must be %r' % team
        assert g['assign'] in ASSIGNS, 'assign must be one of %s' % ASSIGNS
        p = g.setdefault('params', {})
        defaults = default_params()
        for k, (lo, hi) in PARAM_RANGES.items():
            p.setdefault(k, defaults[k])
            p[k] = float(np.clip(float(p[k]), lo, hi))
        assert len(g['roles']) == 2, 'roles must contain exactly two agent roles (one per agent), got %d' % len(g['roles'])
        for role in g['roles']:
            assert isinstance(role['prep'], list) and len(role['prep']) <= 4, 'role prep must be a list of at most 4 segments'
            for s in role['prep']:
                _validate_segment(s)
            pl = role['play']
            assert pl['behaviour'] in BEHAVIOURS, 'unknown play behaviour %r' % pl['behaviour']
            assert pl['target'] in TARGETS, 'unknown play target %r' % pl['target']
            assert pl['route'] in ROUTES, 'unknown route %r' % pl['route']
            assert isinstance(pl['segments'], list) and len(pl['segments']) <= 4, 'play segments must be a list of at most 4 segments'
            for s in pl['segments']:
                _validate_segment(s)
        if team == 'seeker':
            for role in g['roles']:
                role['prep'] = []       # seekers are frozen in the preparation phase
        return True
    except Exception as exc:
        if verbose:
            print('  graph validation detail: %s: %s' % (type(exc).__name__, exc), flush=True)
        if errors is not None:
            errors.append('%s: %s' % (type(exc).__name__, exc))
        return False


def _validate_segment(s):
    assert isinstance(s, dict), 'segment must be a JSON object'
    s.setdefault('gate', None)
    s.setdefault('acquire', None)
    s.setdefault('deliver', None)
    if s.get('face') is None:
        s['face'] = 'target'
    if s.get('route') is None:
        s['route'] = 'door'
    for key in ('lock', 'release'):
        value = s.get(key)
        if value is None:
            s[key] = False
        elif value in (0, 1, 'true', 'false', 'True', 'False') and not isinstance(value, bool):
            s[key] = value in (1, 'true', 'True')
    assert s.get('acquire') in ACQUIRE, 'unknown segment acquire %r' % s.get('acquire')
    assert s.get('deliver') is None or s.get('deliver') in TARGETS, 'unknown segment deliver %r' % s.get('deliver')
    assert isinstance(s.get('lock'), bool) and isinstance(s.get('release'), bool), \
        'segment lock/release must be booleans; got lock=%r (%s), release=%r (%s)' % (
            s.get('lock'), type(s.get('lock')).__name__, s.get('release'), type(s.get('release')).__name__)
    assert s.get('face') in FACES, 'unknown segment face %r' % s.get('face')
    assert s.get('route') in ROUTES, 'unknown segment route %r' % s.get('route')
    assert s['gate'] in GATES, 'unknown segment gate %r' % s['gate']
    assert s.get('acquire') is not None or s.get('deliver') is not None, 'segment must acquire or deliver'
    assert not (s['gate'] == 'doors_sealed' and s.get('deliver') == 'door_block'), \
        'gate doors_sealed can never fire on a segment that delivers to door_block (the segment itself seals the door)'
    assert not (s['gate'] == 'ramp_inside' and s.get('acquire') == 'ramp' and s.get('deliver') == 'ramp_inside'), \
        'gate ramp_inside can never fire on a segment that moves the ramp inside (the segment itself does that)'


def graph_signature(g):
    return json.dumps({k: g[k] for k in ('assign', 'roles')}, sort_keys=True) + \
        json.dumps({k: round(v, 2) for k, v in g['params'].items()}, sort_keys=True)


def describe_graph(g):
    lines = ["assign=%s params=%s" % (g['assign'], {k: round(v, 2) for k, v in g['params'].items()})]
    for i, role in enumerate(g['roles']):
        segs = ' -> '.join(_seg_str(s) for s in role['prep']) or '(none)'
        pl = role['play']
        play = pl['behaviour'] + ('(%s,%s)' % (pl['target'], pl['route']) if pl['behaviour'] == 'go' else '')
        if pl['segments']:
            play += ' then ' + ' -> '.join(_seg_str(s) for s in pl['segments'])
        lines.append("  role%d prep: %s | play: %s" % (i, segs, play))
    return '\n'.join(lines)


def _seg_str(s):
    parts = []
    if s.get('gate'):
        parts.append('[when %s]' % s['gate'])
    if s['acquire']:
        parts.append('grab %s' % s['acquire'])
    if s['deliver']:
        parts.append('to %s[%s,%s]' % (s['deliver'], s['face'], s['route']))
    if s['lock']:
        parts.append('lock')
    if s['release']:
        parts.append('release')
    return ' '.join(parts)


# ═════════════════════════════════════════════════════════════════════════════
# SCENE GEOMETRY  (known workcell: quadrant walls + doors from env metadata)
# ═════════════════════════════════════════════════════════════════════════════

class Scene:
    def __init__(self, env):
        u = env.unwrapped
        q = u.metadata['quadrant_size']
        # walls are 0.1 wide and centred on grid-cell centres
        self.wall_x = (GRID - q + 0.5) * CELL    # centre line of the vertical quadrant wall
        self.wall_y = (q + 0.5) * CELL           # centre line of the horizontal quadrant wall
        self.interior = np.array([self.wall_x + 0.35, FLOOR - 0.3, 0.3, self.wall_y - 0.35])  # xmin,xmax,ymin,ymax
        self.center = np.array([(self.interior[0] + self.interior[1]) / 2, (self.interior[2] + self.interior[3]) / 2])
        self.corner = np.array([FLOOR - 0.5, 0.5])
        self.doors = []
        for d in u.metadata['doors']:
            (x0, y0), (x1, y1) = d
            if x0 == x1:          # door in the vertical wall
                c = np.array([(x0 + 0.5) * CELL, ((y0 + y1) / 2 + 0.5) * CELL])
                normal = np.array([1.0, 0.0])
            else:                 # door in the horizontal wall
                c = np.array([((x0 + x1) / 2 + 0.5) * CELL, (y0 + 0.5) * CELL])
                normal = np.array([0.0, -1.0])
            self.doors.append({'center': c, 'inward': normal})
        self.outer_corner = np.array([self.wall_x - 0.45, self.wall_y + 0.45])

    def inside(self, p):
        return p[0] > self.wall_x + 0.05 and p[1] < self.wall_y - 0.05

    def outside(self, p):
        return p[0] < self.wall_x - 0.05 or p[1] > self.wall_y + 0.05

    def door_block_point(self, door, offset):
        return door['center'] + door['inward'] * offset

    def door_blocked(self, door, box_pos):
        """A box whose centre sits in the doorway (either side) seals it."""
        for b in box_pos:
            rel = b[:2] - door['center']
            along = abs(rel @ door['inward'])
            perp = abs(rel @ np.array([-door['inward'][1], door['inward'][0]]))
            if along < 0.6 and perp < 0.35:
                return True
        return False

    def outside_wall_point(self, p, offset):
        """Closest point just outside the quadrant walls (for ramp placement) and the
        inward wall normal there."""
        y = float(np.clip(p[1], 0.4, self.wall_y - 0.4))
        a = (np.array([self.wall_x - RAMP_GAP - offset, y]), np.array([1.0, 0.0]))
        x = float(np.clip(p[0], self.wall_x + 0.4, FLOOR - 0.4))
        b = (np.array([x, self.wall_y + RAMP_GAP + offset]), np.array([0.0, -1.0]))
        return min([a, b], key=lambda c: np.linalg.norm(c[0] - p[:2]))

    def segment_hits_quadrant(self, a, b):
        xmin, xmax, ymin, ymax = self.wall_x - 0.05, FLOOR, 0.0, self.wall_y + 0.05
        for t in np.linspace(0.0, 1.0, 12):
            q = a + (b - a) * t
            if xmin < q[0] < xmax and ymin < q[1] < ymax:
                return True
        return False

    def avoid(self, a, b):
        """Leg from a to b (both outside): detour via the outer corner if it cuts the quadrant."""
        if self.segment_hits_quadrant(a, b) and not self.inside(a) and not self.inside(b):
            return [self.outer_corner.copy(), b]
        return [b]


# ═════════════════════════════════════════════════════════════════════════════
# GRAPH EXECUTOR  (interprets a team graph → per-agent actions every step)
# ═════════════════════════════════════════════════════════════════════════════

def wrap_angle(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def to_bin(f):
    return int(np.clip(np.round((np.clip(f, -ACT_MAX, ACT_MAX) / ACT_MAX + 1.0) * (N_BINS - 1) / 2.0), 0, N_BINS - 1))


class State:
    """Simulator-side perception for one step (true poses + visibility masks)."""
    def __init__(self, sim, ids, obs, step):
        self.step = step
        self.in_prep = step < PREP_STEPS
        self.agent_pos = sim.data.body_xpos[ids['agents']].copy()
        self.agent_vel = sim.data.qvel[ids['agent_vel']].copy()          # (N,2)
        self.agent_rz = sim.data.qpos[ids['agent_rz']].copy()            # (N,)
        self.agent_vrz = sim.data.qvel[ids['agent_vrz']].copy()
        self.box_pos = sim.data.body_xpos[ids['boxes']].copy()
        self.ramp_pos = sim.data.body_xpos[ids['ramp']].copy()
        self.ramp_rz = float(sim.data.qpos[ids['ramp_rz']])
        self.box_locked = obs['box_obs'][0, :, -1] > 0.5
        self.box_team_lock = obs['box_obs'][:, :, -2] > 0.5        # (agent, box): locked by the agent's team
        # physical grab state: the agent↔object weld constraint is active
        eq_act = sim.model.eq_active[ids['agent_eq']]
        eq_obj = sim.model.eq_obj2id[ids['agent_eq']]
        self.grabbed = {}
        for a in range(N_AGENTS):
            if eq_act[a]:
                self.grabbed[a] = ids['body2obj'].get(int(eq_obj[a]))
        self.mask_aa = obs['mask_aa_obs']
        self.mask_ab = obs['mask_ab_obs']
        self.mask_ar = obs['mask_ar_obs']

    def sees_agent(self, i, j):
        others = [k for k in range(N_AGENTS) if k != i]
        return bool(self.mask_aa[i, others.index(j)])


class TeamController:
    """Executes one team graph.  Holds the team's belief state and per-agent
    segment progress (the graph's control-edge state)."""

    def __init__(self, graph, agents, opponents, scene):
        self.g = graph
        self.p = graph['params']
        self.agents = agents
        self.opp = opponents
        self.scene = scene
        self.role_of = {a: i for i, a in enumerate(agents)}
        self.seg_idx = {a: 0 for a in agents}
        self.seg_t = {a: 0 for a in agents}
        self.phase_of_seg = {a: 'prep' for a in agents}
        self.claimed_obj = {}            # (kind, idx) -> agent
        self.prev_carry = {}
        self.claimed_door = {}           # door idx -> agent
        self.lock_timer = {a: 0 for a in agents}
        self.last_seen_opp = {}          # opp idx -> pos
        self.obj_belief = {'box': {}, 'ramp': {}}
        self.wander_t = {a: None for a in agents}
        self.search_i = {a: 0 for a in agents}
        self.waypoints = {a: [] for a in agents}
        self.wp_goal = {a: None for a in agents}
        self.target_normal = {a: None for a in agents}
        self.trace = {a: [] for a in agents}        # (segment id, status, step) for failure analysis
        self.assigned = False
        self.node_active = {a: 'init' for a in agents}

    # ── perception node ──────────────────────────────────────────────────
    def perceive(self, st):
        for j in self.opp:
            if any(st.sees_agent(i, j) for i in self.agents):
                self.last_seen_opp[j] = st.agent_pos[j, :2].copy()
        for b in range(len(st.box_pos)):
            if cfg.omniscient_objects or any(st.mask_ab[i, b] for i in self.agents):
                self.obj_belief['box'][b] = st.box_pos[b].copy()
        if cfg.omniscient_objects or any(st.mask_ar[i, 0] for i in self.agents):
            self.obj_belief['ramp'][0] = st.ramp_pos.copy()

    # ── role-assignment node ─────────────────────────────────────────────
    def assign_roles(self, st):
        if self.g['assign'] == 'nearest_object' and len(self.agents) == 2:
            a0, a1 = self.agents
            def cost(agent, role):
                segs = self.g['roles'][role]['prep'] or self.g['roles'][role]['play']['segments']
                if not segs or segs[0]['acquire'] is None:
                    return 0.0
                kind = segs[0]['acquire']
                poses = list(self.obj_belief[kind].values())
                if not poses:
                    return 0.0
                return min(np.linalg.norm(p[:2] - st.agent_pos[agent, :2]) for p in poses)
            if cost(a0, 0) + cost(a1, 1) > cost(a0, 1) + cost(a1, 0):
                self.role_of = {a0: 1, a1: 0}
        self.assigned = True

    # ── main entry: returns {agent: (fx, fy, torque, pull, glue)} ─────────
    def act(self, st):
        self.perceive(st)
        if not self.assigned:
            self.assign_roles(st)
        out = {}
        for a in self.agents:
            role = self.g['roles'][self.role_of[a]]
            segs = role['prep'] if st.in_prep else role['play']['segments']
            key = 'prep' if st.in_prep else 'play'
            if self.phase_of_seg[a] != key:
                self.phase_of_seg[a] = key
                self.seg_idx[a], self.seg_t[a], self.waypoints[a], self.wp_goal[a] = 0, 0, [], None
                for k_ in [k_ for k_, owner in self.claimed_obj.items() if owner == a]:
                    del self.claimed_obj[k_]
            if st.in_prep and a in SEEKERS:
                out[a] = (0.0, 0.0, 0.0, 0, 0)
                continue
            if self.seg_idx[a] < len(segs) and (st.in_prep or role['play']['behaviour'] == 'segments'):
                out[a] = self.run_segment(a, segs[self.seg_idx[a]], st, key)
            elif not st.in_prep:
                out[a] = self.run_play(a, role['play'], st)
            else:
                out[a] = self.run_play(a, role['play'], st) if role['play']['behaviour'] in ('go', 'stay') \
                    else self.hold(a, st)
            # lock maintenance: a team-mate standing next to a team-locked box with
            # glue=0 would UNLOCK it (all_lock_team_specific), so keep glue pressed there
            if out[a][4] == 0:
                for b in range(len(st.box_pos)):
                    if st.box_team_lock[a, b] and np.linalg.norm(st.box_pos[b, :2] - st.agent_pos[a, :2]) < 0.75:
                        out[a] = out[a][:4] + (1,)
                        break
        return out

    # ── segment node (acquire → deliver → lock → release) ─────────────────
    def run_segment(self, a, seg, st, key):
        self.seg_t[a] += 1
        sid = '%s%d/%d' % (key, self.role_of[a], self.seg_idx[a])
        self.node_active[a] = sid
        if self.seg_t[a] > self.p['seg_timeout'] * (2 if seg['deliver'] in ('climb',) else 1):
            self.trace[a].append((sid, 'timeout', st.step))
            self.advance(a)
            return self.hold(a, st)
        if seg.get('gate') and not self.gate_open(a, seg['gate'], st):
            self.node_active[a] = sid + ':wait'
            carrying = st.grabbed.get(a)
            return self.hold(a, st, scan=carrying is None, pull=1 if carrying else 0)
        carrying = st.grabbed.get(a)            # physical weld state (None if not holding anything)
        if carrying != self.prev_carry.get(a):
            self.waypoints[a], self.wp_goal[a] = [], None      # grab / drop → re-plan
            if self.prev_carry.get(a) is not None and carrying is None:
                self.trace[a].append((sid, 'dropped', st.step))
            self.prev_carry[a] = carrying
        for key_, owner in list(self.claimed_obj.items()):
            if owner == a and key_ != carrying:
                del self.claimed_obj[key_]
        if carrying is not None:
            self.claimed_obj[carrying] = a
        pos = st.agent_pos[a]
        # 1) acquire
        if seg['acquire'] is not None and carrying is None:
            target = self.pick_object(a, seg['acquire'], st)
            if target is None:
                self.trace[a].append((sid, 'no_object', st.step))
                self.advance(a)
                return self.hold(a, st)
            kind, idx = target
            self.claimed_obj[(kind, idx)] = a          # reserve it for this agent
            opos = self.obj_belief[kind][idx]
            d = np.linalg.norm(opos[:2] - pos[:2])
            fx, fy = self.steer(a, opos[:2], st, route=seg['route'])
            return (fx, fy, self.face(a, opos[:2], st), 1 if d < 0.9 else 0, 0)
        # 2) deliver
        if seg['deliver'] is not None:
            target = self.resolve_target(a, seg['deliver'], st, seg)
            if target is None:
                self.trace[a].append((sid, 'no_target', st.step))
                self.advance(a)
                return self.hold(a, st)
            ctrl_pos = self.obj_belief[carrying[0]][carrying[1]][:2] if carrying else pos[:2]
            d = np.linalg.norm(target - ctrl_pos)
            tol = self.p['tol'] if seg['deliver'] not in ('climb', 'opponent') else 0.5
            if d > tol:
                fx, fy = self.steer(a, target, st, route=seg['route'], ctrl_pos=ctrl_pos)
                torque = self.face_yaw(a, seg['face'], target, st, carrying)
                return (fx, fy, torque, 1 if carrying else 0, 0)
        # 3) lock
        if seg['lock'] and carrying and carrying[0] == 'box':
            if self.lock_timer[a] < 2:
                self.lock_timer[a] += 1
                return (0.0, 0.0, 0.0, 1, 1)
        # 4) release / finish
        self.lock_timer[a] = 0
        if carrying and seg['release']:
            self.claimed_obj.pop(carrying, None)
        self.trace[a].append((sid, 'done', st.step))
        self.advance(a)
        keep = 1 if (carrying and not seg['release']) else 0
        return (0.0, 0.0, 0.0, keep, 0)

    def advance(self, a):
        self.seg_idx[a] += 1
        self.seg_t[a] = 0
        self.waypoints[a], self.wp_goal[a] = [], None

    def gate_open(self, a, gate, st):
        sc = self.scene
        if gate == 'teammate_inside':
            return all(sc.inside(st.agent_pos[m, :2]) for m in self.agents if m != a)
        if gate == 'ramp_inside':
            return sc.inside(st.ramp_pos[:2])
        if gate == 'opponent_visible':
            return any(st.sees_agent(i, j) for i in self.agents for j in self.opp)
        if gate == 'doors_sealed':
            return all(sc.door_blocked(d, st.box_pos) for d in sc.doors)
        if gate == 'door':
            return any(np.linalg.norm(st.agent_pos[i, :2] - d['center']) < 0.8
                       for i in self.agents for d in sc.doors)
        return True

    def pick_object(self, a, kind, st):
        best, bd = None, 1e9
        for idx, opos in self.obj_belief[kind].items():
            if (kind, idx) in self.claimed_obj and self.claimed_obj[(kind, idx)] != a:
                continue
            if kind == 'box' and st.box_locked[idx]:
                continue
            d = np.linalg.norm(opos[:2] - st.agent_pos[a, :2])
            if d < bd:
                best, bd = (kind, idx), d
        return best

    # ── target-selection node ─────────────────────────────────────────────
    def resolve_target(self, a, name, st, seg=None):
        sc, pos = self.scene, st.agent_pos[a, :2]
        if name in ('door_block', 'door_inside'):
            if a in self.claimed_door.values():
                di = [k for k, v in self.claimed_door.items() if v == a][0]
            else:
                free = [i for i, d in enumerate(sc.doors)
                        if i not in self.claimed_door and not sc.door_blocked(d, st.box_pos)]
                if not free:
                    return None
                di = min(free, key=lambda i: np.linalg.norm(sc.doors[i]['center'] - pos))
                self.claimed_door[di] = a
            if name == 'door_inside':
                return sc.doors[di]['center'] + sc.doors[di]['inward'] * 0.95
            return sc.door_block_point(sc.doors[di], self.p['offset'])
        if name == 'quadrant_interior':
            return sc.center.copy()
        if name == 'quadrant_corner':
            return sc.corner.copy()
        if name == 'ramp_inside':
            return sc.corner.copy()
        if name == 'outside_wall':
            pt, normal = sc.outside_wall_point(pos, self.p['offset'])
            self.target_normal[a] = normal
            return pt
        if name == 'climb':
            return sc.center.copy()
        if name == 'teammate':
            mates = [m for m in self.agents if m != a]
            return st.agent_pos[mates[0], :2].copy() if mates else None
        if name == 'opponent':
            if not self.last_seen_opp:
                return None
            return min(self.last_seen_opp.values(), key=lambda q: np.linalg.norm(q - pos)).copy()
        if name == 'away_from_opponent':
            if not self.last_seen_opp:
                return None
            q = min(self.last_seen_opp.values(), key=lambda q: np.linalg.norm(q - pos))
            v = pos - q
            n = np.linalg.norm(v)
            v = v / n if n > 1e-6 else np.array([1.0, 0.0])
            t = pos + v * 1.5
            lo, hi = (sc.interior[[0, 2]], sc.interior[[1, 3]]) if sc.inside(pos) else (0.4, FLOOR - 0.4)
            return np.clip(t, lo, hi)
        if name == 'ramp':
            return self.obj_belief['ramp'][0][:2].copy() if self.obj_belief['ramp'] else None
        if name == 'box':
            if not self.obj_belief['box']:
                return None
            return min(self.obj_belief['box'].values(), key=lambda q: np.linalg.norm(q[:2] - pos))[:2].copy()
        if name == 'wander':
            if self.wander_t[a] is None or np.linalg.norm(self.wander_t[a] - pos) < 0.4:
                self.wander_t[a] = np.random.uniform(0.5, FLOOR - 0.5, size=2)
            return self.wander_t[a]
        if name == 'stay':
            return pos.copy()
        return None

    # ── play-phase behaviour node ─────────────────────────────────────────
    def run_play(self, a, play, st):
        b = play['behaviour']
        self.node_active[a] = 'play/' + b
        pos = st.agent_pos[a, :2]
        if b == 'stay':
            return self.hold(a, st)
        if b == 'flee':
            t = self.resolve_target(a, 'away_from_opponent', st)
            if t is None:
                return self.hold(a, st, scan=True)
            fx, fy = self.steer(a, t, st, route='door')
            return (fx, fy, self.face(a, pos + (pos - t), st), 0, 0)
        if b == 'chase':
            t = self.resolve_target(a, 'opponent', st)
            if t is None:
                return self.search(a, st)
            fx, fy = self.steer(a, t, st, route='door')
            return (fx, fy, self.face(a, t, st), 0, 0)
        if b == 'search':
            return self.search(a, st)
        if b in ('go', 'segments'):
            t = self.resolve_target(a, play['target'], st)
            if t is None:
                return self.search(a, st) if a in SEEKERS else self.hold(a, st, scan=True)
            fx, fy = self.steer(a, t, st, route=play['route'])
            return (fx, fy, self.face(a, t, st), 0, 0)
        return self.hold(a, st)

    def search(self, a, st):
        """Patrol: door approach points, then the quadrant interior (via doors)."""
        sc, pos = self.scene, st.agent_pos[a, :2]
        pts = [d['center'] - d['inward'] * 0.6 for d in sc.doors] + [sc.center, sc.corner]
        if not pts:
            pts = [sc.center]
        t = pts[self.search_i[a] % len(pts)]
        if np.linalg.norm(t - pos) < 0.45:
            self.search_i[a] += 1
            t = pts[self.search_i[a] % len(pts)]
        self.node_active[a] = 'play/search'
        fx, fy = self.steer(a, t, st, route='door')
        return (fx, fy, self.face(a, t, st), 0, 0)

    def hold(self, a, st, scan=False, pull=0):
        v = st.agent_vel[a]
        torque = 0.4 if scan else 0.0
        return (float(np.clip(-0.3 * v[0], -ACT_MAX, ACT_MAX)),
                float(np.clip(-0.3 * v[1], -ACT_MAX, ACT_MAX)), torque, pull, 0)

    # ── motion-planning + control nodes ───────────────────────────────────
    def steer(self, a, goal, st, route='door', ctrl_pos=None):
        sc = self.scene
        pos = st.agent_pos[a, :2] if ctrl_pos is None else ctrl_pos
        goal = np.asarray(goal, dtype=float)
        if self.wp_goal[a] is None or np.linalg.norm(goal - self.wp_goal[a]) > 0.25:
            self.waypoints[a], self.wp_goal[a] = [], goal.copy()       # goal changed → re-plan
        if route == 'door' and sc.inside(pos) != sc.inside(goal) and (sc.inside(pos) or sc.inside(goal)):
            if not self.waypoints[a]:
                self.waypoints[a] = self.plan_door_route(pos, goal, st)
        elif route == 'door' and sc.outside(pos) and sc.outside(goal) and sc.segment_hits_quadrant(pos, goal):
            if not self.waypoints[a]:
                self.waypoints[a] = sc.avoid(pos, goal)
        if self.waypoints[a]:
            wp = self.waypoints[a][0]
            if np.linalg.norm(wp - pos) < 0.45:
                self.waypoints[a].pop(0)
                wp = self.waypoints[a][0] if self.waypoints[a] else goal
        else:
            wp = goal
        if self.waypoints[a] and len(self.waypoints[a]) > 1:
            d = wp - pos                                  # intermediate waypoint: full speed
            n = np.linalg.norm(d)
            return self.velocity_control(a, d / n * (V_MAX / self.p['gain']) if n > 1e-6 else d, st)
        return self.velocity_control(a, wp - pos, st)

    def velocity_control(self, a, d, st):
        """Desired velocity ∝ position error (speed-capped); force tracks it.  The particle's
        slide joints have damping 10 and gear 100, so f≈v/10 holds a steady velocity."""
        v_des = self.p['gain'] * d
        n = np.linalg.norm(v_des)
        if n > V_MAX:
            v_des = v_des / n * V_MAX
        v = st.agent_vel[a]
        f = 0.1 * v_des + self.p['damp'] * (v_des - v)
        return float(np.clip(f[0], -ACT_MAX, ACT_MAX)), float(np.clip(f[1], -ACT_MAX, ACT_MAX))

    def plan_door_route(self, pos, goal, st):
        sc = self.scene
        best, bc = None, 1e9
        for i, d in enumerate(sc.doors):
            if sc.door_blocked(d, st.box_pos) and not sc.inside(pos):
                continue       # a sealed door cannot be used from the outside
            out_pt = d['center'] - d['inward'] * 0.55
            in_pt = d['center'] + d['inward'] * 0.55
            c = np.linalg.norm(pos - (in_pt if sc.inside(pos) else out_pt)) + np.linalg.norm(goal - (out_pt if sc.inside(pos) else in_pt))
            if c < bc:
                best, bc = (in_pt, out_pt) if sc.inside(pos) else (out_pt, in_pt), c
        if best is None:
            return [goal]
        if sc.inside(pos):
            return [best[0], best[1]] + sc.avoid(best[1], goal)
        return sc.avoid(pos, best[0]) + [best[1], goal]

    def turn_to(self, a, err, st, carrying=False):
        """Torque for a yaw error; ~0.75 rad of rotation per step per unit torque."""
        tmax = 0.5 if carrying else 0.8
        return float(np.clip(0.9 * err, -tmax, tmax))

    def face(self, a, target, st):
        rel = np.asarray(target)[:2] - st.agent_pos[a, :2]
        if np.linalg.norm(rel) < 0.15:
            return 0.0
        desired = np.arctan2(rel[1], rel[0]) + np.pi / 2
        return self.turn_to(a, wrap_angle(desired - st.agent_rz[a]), st)

    def face_yaw(self, a, face, target, st, carrying):
        if face == 'target' or not carrying:
            rel = np.asarray(target)[:2] - st.agent_pos[a, :2]
            if np.linalg.norm(rel) < 0.15:
                return 0.0
            desired = np.arctan2(rel[1], rel[0]) + np.pi / 2
            return self.turn_to(a, wrap_angle(desired - st.agent_rz[a]), st, carrying=bool(carrying))
        if face == 'align':
            # rotate the carried ramp so its slope rises toward the wall (climbable from outside)
            if carrying[0] != 'ramp' or self.target_normal[a] is None:
                return self.face(a, target, st)
            n = self.target_normal[a]
            desired_ramp = np.arctan2(n[0], -n[1])
            return self.turn_to(a, wrap_angle(desired_ramp - st.ramp_rz), st, carrying=True)
        k = int(face[-1])
        desired = k * np.pi / 2
        return self.turn_to(a, wrap_angle(desired - st.agent_rz[a]), st, carrying=True)


# ═════════════════════════════════════════════════════════════════════════════
# EPISODE ROLLOUT  +  EMERGENT-BEHAVIOUR DETECTORS  +  FAILURE ANALYSIS
# ═════════════════════════════════════════════════════════════════════════════

def cache_ids(env):
    sim = env.unwrapped.sim
    m = sim.model
    qpos = [qpos_idxs_from_joint_prefix(sim, 'agent%d' % i) for i in range(N_AGENTS)]   # [tx, ty, tz, rz]
    qvel = [qvel_idxs_from_joint_prefix(sim, 'agent%d' % i) for i in range(N_AGENTS)]
    agent_bodies = [m.body_name2id('agent%d:particle' % i) for i in range(N_AGENTS)]
    eq_ids = []
    for i in range(N_AGENTS):
        eq_ids.append([e for e, b in enumerate(m.eq_obj1id) if b == agent_bodies[i]][0])
    body2obj = {m.body_name2id('moveable_box%d' % i): ('box', i) for i in range(ENV_KWARGS['n_boxes'])}
    body2obj[m.body_name2id('ramp0:ramp')] = ('ramp', 0)
    ids = {'agents': np.array(agent_bodies),
           'agent_eq': np.array(eq_ids), 'body2obj': body2obj,
           'boxes': np.array([m.body_name2id('moveable_box%d' % i) for i in range(ENV_KWARGS['n_boxes'])]),
           'ramp': m.body_name2id('ramp0:ramp'),
           'ramp_rz': qpos_idxs_from_joint_prefix(sim, 'ramp0')[-1],
           'agent_rz': np.array([q[-1] for q in qpos]),
           'agent_vrz': np.array([v[-1] for v in qvel]),
           'agent_vel': np.array([v[:2] for v in qvel])}
    return ids


def set_p_door(env, p):
    for mod in env.unwrapped.modules:
        if hasattr(mod, 'p_door_dropout'):
            mod.p_door_dropout = p


def run_episode(env, hider_graph, seeker_graph, p_door, seed, verbose=False, frame_cb=None):
    """Rehearse one task instance.  Returns a result dict with the objective,
    behaviour flags and a structured failure summary for both teams."""
    set_p_door(env, p_door)
    np.random.seed(seed)
    try:
        env.seed(seed)
    except Exception:
        pass
    obs = env.reset()
    ids = cache_ids(env)
    sim = env.unwrapped.sim
    scene = Scene(env)
    H = TeamController(hider_graph, HIDERS, SEEKERS, scene)
    S = TeamController(seeker_graph, SEEKERS, HIDERS, scene)
    st = State(sim, ids, obs, 0)
    ramp_start = st.ramp_pos.copy()
    box_start = st.box_pos.copy()
    hid_rew, play_steps = 0.0, 0
    first_seen = None
    chase_hits, chase_steps = 0, 0
    seeker_max_z, seeker_entered, wall_crossing = 0.0, False, False
    seeker_inside_prev = {s: scene.inside(st.agent_pos[s, :2]) for s in SEEKERS}
    prep_end = None
    if verbose:
        print('doors:', [(np.round(d['center'], 2).tolist(), d['inward'].tolist()) for d in scene.doors],
              'wall_x=%.2f wall_y=%.2f' % (scene.wall_x, scene.wall_y), 'p_door', p_door)
    for t in range(cfg.horizon):
        st = State(sim, ids, obs, t)
        if frame_cb is not None:
            frame_cb(env, t)
        acts = {}
        acts.update(H.act(st))
        acts.update(S.act(st))
        if verbose:
            carry = dict(st.grabbed)
            print('t=%2d %s | ' % (t, 'PREP' if st.in_prep else 'play') + ' | '.join(
                '%s%d (%.2f,%.2f,z%.2f) %s c=%s a=(%.1f,%.1f,%.1f,%d,%d)' % (
                    'h' if a in HIDERS else 's', a, st.agent_pos[a, 0], st.agent_pos[a, 1], st.agent_pos[a, 2],
                    (H if a in HIDERS else S).node_active[a], carry.get(a), *acts[a]) for a in range(N_AGENTS))
                + ' | boxes=%s lk=%s ramp=%s rz=%.2f' % (np.round(st.box_pos[:, :2], 2).tolist(), st.box_locked.astype(int).tolist(),
                                                       np.round(st.ramp_pos[:2], 2).tolist(), st.ramp_rz))
        move = np.array([[to_bin(acts[a][0]), to_bin(acts[a][1]), to_bin(acts[a][2])] for a in range(N_AGENTS)])
        action = {'action_movement': move,
                  'action_pull': np.array([int(acts[a][3]) for a in range(N_AGENTS)]),
                  'action_glueall': np.array([int(acts[a][4]) for a in range(N_AGENTS)])}
        obs, rew, done, info = env.step(action)
        if info.get('discard_episode'):
            return None
        st2 = State(sim, ids, obs, t + 1)
        if prep_end is None and not st2.in_prep:
            prep_end = {'box_pos': st2.box_pos.copy(), 'box_locked': st2.box_locked.copy(),
                        'ramp_pos': st2.ramp_pos.copy()}
        if not st2.in_prep:
            play_steps += 1
            hid_rew += 1.0 if rew[0] > 0 else 0.0
            for s in SEEKERS:
                seeker_max_z = max(seeker_max_z, float(st2.agent_pos[s, 2]))
                now_inside = scene.inside(st2.agent_pos[s, :2])
                if now_inside:
                    seeker_entered = True
                if now_inside and not seeker_inside_prev[s]:
                    near_door = any(np.linalg.norm(st2.agent_pos[s, :2] - d['center']) < 0.55 for d in scene.doors)
                    if not near_door:
                        wall_crossing = True        # entered the quadrant over the wall, not through a doorway
                seeker_inside_prev[s] = now_inside
                hp = st2.agent_pos[HIDERS, :2]
                dists = np.linalg.norm(hp - st2.agent_pos[s, :2], axis=1)
                h = int(np.argmin(dists))
                v = st2.agent_vel[s]
                if dists[h] < 3.0 and np.linalg.norm(v) > 0.5:
                    chase_steps += 1
                    direction = (hp[h] - st2.agent_pos[s, :2]) / (dists[h] + 1e-6)
                    if direction @ v / np.linalg.norm(v) > 0.6:
                        chase_hits += 1
            if first_seen is None and rew[0] < 0:
                for s in SEEKERS:
                    for h in HIDERS:
                        if st2.sees_agent(s, h):
                            first_seen = {'step': t + 1, 'seeker': s, 'hider': h,
                                          'hider_inside': bool(scene.inside(st2.agent_pos[h, :2])),
                                          'seeker_inside': bool(scene.inside(st2.agent_pos[s, :2])),
                                          'seeker_z': round(float(st2.agent_pos[s, 2]), 2)}
                            break
                    if first_seen:
                        break
        if done:
            break
    if prep_end is None:
        return None
    J_h = hid_rew / max(play_steps, 1)
    open_doors = scene.doors
    doors_blocked = [bool(scene.door_blocked(d, prep_end['box_pos'])) for d in open_doors]
    locked_in_doors = [any(scene.door_blocked(d, prep_end['box_pos'][[b]]) and prep_end['box_locked'][b]
                           for b in range(len(prep_end['box_pos']))) for d in open_doors]
    door_blocking = len(open_doors) > 0 and all(locked_in_doors)
    ramp_moved_prep = float(np.linalg.norm(prep_end['ramp_pos'][:2] - ramp_start[:2]))
    ramp_started_outside = not scene.inside(ramp_start[:2])
    ramp_inside_prep = bool(scene.inside(prep_end['ramp_pos'][:2]))
    # ramp defense: the hiders BROUGHT the ramp into the quadrant during preparation
    ramp_defense = bool(ramp_started_outside and ramp_inside_prep and ramp_moved_prep > 0.4)
    # ramp use: a seeker got into the quadrant over the wall (not through a doorway)
    ramp_use = bool(wall_crossing and seeker_max_z > 0.3)
    chasing = chase_steps >= 4 and chase_hits / max(chase_steps, 1) > 0.5
    res = {
        'J_hider': J_h, 'hider_win': bool(J_h > 0.5), 'p_door': p_door, 'seed': seed,
        'behaviours': {'chasing': bool(chasing), 'door_blocking': bool(door_blocking),
                       'ramp_use': ramp_use, 'ramp_defense': ramp_defense},
        'applicable': {'chasing': True, 'door_blocking': True, 'ramp_use': True, 'ramp_defense': ramp_started_outside},
        'first_seen': first_seen,
        'n_doors': len(open_doors), 'doors_blocked': doors_blocked, 'doors_locked': locked_in_doors,
        'boxes_moved_prep': [round(float(np.linalg.norm(prep_end['box_pos'][b, :2] - box_start[b, :2])), 2)
                             for b in range(len(box_start))],
        'boxes_locked_prep': [bool(x) for x in prep_end['box_locked']],
        'ramp_moved_prep': round(ramp_moved_prep, 2), 'ramp_inside_prep': ramp_inside_prep,
        'ramp_inside_start': not ramp_started_outside,
        'seeker_max_z': round(seeker_max_z, 2), 'seeker_entered': seeker_entered, 'wall_crossing': wall_crossing,
        'hider_trace': {str(a): H.trace[a] for a in HIDERS},
        'seeker_trace': {str(a): S.trace[a] for a in SEEKERS},
        'hider_nodes': {str(a): H.node_active[a] for a in HIDERS},
        'seeker_nodes': {str(a): S.node_active[a] for a in SEEKERS},
    }
    return res


# ═════════════════════════════════════════════════════════════════════════════
# PARALLEL REHEARSAL WORKERS
# ═════════════════════════════════════════════════════════════════════════════

def _worker(pipe, seed):
    env = make_env(**ENV_KWARGS)
    random.seed(seed)
    np.random.seed(seed)
    try:
        while True:
            msg = pipe.recv()
            if msg is None:
                break
            out = []
            for (job_id, hg, sg, p_door, ep_seed) in msg:        # a batch of jobs
                try:
                    res = run_episode(env, hg, sg, p_door, ep_seed)
                except Exception:          # MuJoCo instabilities → drop the instance
                    res = None
                out.append((job_id, res))
            pipe.send(out)
    except (EOFError, BrokenPipeError, KeyboardInterrupt):
        pass


class RehearsalPool:
    BATCH = 2   # jobs per worker message; small so late-arriving candidates start quickly

    def __init__(self, n, seed):
        self.pipes, self.procs = [], []
        for i in range(n):
            parent, child = mp.Pipe()
            p = mp.Process(target=_worker, args=(child, seed * 1000 + i), daemon=True)
            p.start()
            child.close()
            self.pipes.append(parent)
            self.procs.append(p)
        self._q = queue.Queue()
        self._thread = threading.Thread(target=self._dispatch, daemon=True)
        self._thread.start()

    def submit(self, jobs):
        """jobs: list of (hider_graph, seeker_graph, p_door, seed) → Future of results (None = discarded)."""
        fut = Future()
        if not jobs:
            fut.set_result([])
        else:
            self._q.put((fut, list(jobs)))
        return fut

    def run(self, jobs):
        return self.submit(jobs).result()

    def _dispatch(self):
        from multiprocessing.connection import wait
        pending, groups, idle, busy, next_gid = deque(), {}, list(self.pipes), set(), 0
        try:
            while True:
                try:
                    while True:
                        item = self._q.get() if not (pending or busy) else self._q.get_nowait()
                        if item is None:
                            return
                        fut, jobs = item
                        groups[next_gid] = [fut, [None] * len(jobs), len(jobs)]
                        pending.extend((next_gid, i, job) for i, job in enumerate(jobs))
                        next_gid += 1
                except queue.Empty:
                    pass
                while idle and pending:
                    pipe = idle.pop()
                    batch = [pending.popleft() for _ in range(min(self.BATCH, len(pending)))]
                    pipe.send([((gid, i),) + tuple(job) for gid, i, job in batch])
                    busy.add(pipe)
                for pipe in wait(list(busy), timeout=0.05):
                    for (gid, i), res in pipe.recv():
                        g = groups[gid]
                        g[1][i] = res
                        g[2] -= 1
                        if g[2] == 0:
                            g[0].set_result(g[1])
                            del groups[gid]
                    busy.discard(pipe)
                    idle.append(pipe)
        except Exception as e:
            traceback.print_exc()
            for g in groups.values():
                g[0].set_exception(e)

    def close(self):
        self._q.put(None)
        self._thread.join(timeout=5)
        for p in self.pipes:
            try:
                p.send(None)
            except Exception:
                pass
        for p in self.procs:
            p.join(timeout=2)
            if p.is_alive():
                p.terminate()


# ═════════════════════════════════════════════════════════════════════════════
# GRAPH UPDATE  (failure-weighted structural search  +  optional LLM agent)
# ═════════════════════════════════════════════════════════════════════════════

def random_segment(team):
    acquire = random.choice(ACQUIRE)
    deliver = random.choice([t for t in TARGETS if t not in ('stay',)])
    if acquire is None and deliver is None:
        deliver = 'wander'
    return {'acquire': acquire, 'deliver': deliver, 'lock': random.random() < 0.5,
            'release': random.random() < 0.7, 'face': random.choice(FACES), 'route': random.choice(ROUTES),
            'gate': random.choice(GATES) if random.random() < 0.3 else None}


def mutate(graph, blame):
    """One random structural / parametric edit.  Nodes with higher blame
    (active during failures) are edited with higher probability."""
    g = copy.deepcopy(graph)
    team = g['team']
    roles = g['roles']
    weights = np.array([1.0 + blame.get('role%d' % i, 0.0) for i in range(len(roles))])
    ri = int(np.random.choice(len(roles), p=weights / weights.sum()))
    role = roles[ri]
    ops = ['param', 'assign', 'play_behaviour', 'play_target', 'seg_add', 'seg_del', 'seg_edit', 'seg_swap']
    if team == 'seeker':
        ops = [o for o in ops if o not in ()]
    op = random.choice(ops)
    seg_lists = ([role['prep']] if team == 'hider' else []) + [role['play']['segments']]
    segs = random.choice(seg_lists)
    if op == 'param':
        k = random.choice(list(PARAM_RANGES))
        lo, hi = PARAM_RANGES[k]
        g['params'][k] = float(np.clip(g['params'][k] + np.random.normal(0, (hi - lo) * 0.15), lo, hi))
    elif op == 'assign':
        g['assign'] = random.choice(ASSIGNS)
    elif op == 'play_behaviour':
        role['play']['behaviour'] = random.choice(BEHAVIOURS)
    elif op == 'play_target':
        role['play']['target'] = random.choice(TARGETS)
        role['play']['route'] = random.choice(ROUTES)
    elif op == 'seg_add' and len(segs) < 4:
        segs.insert(random.randint(0, len(segs)), random_segment(team))
    elif op == 'seg_del' and segs:
        segs.pop(random.randrange(len(segs)))
    elif op == 'seg_edit' and segs:
        s = random.choice(segs)
        field = random.choice(['acquire', 'deliver', 'lock', 'release', 'face', 'route', 'gate'])
        if field == 'acquire':
            s['acquire'] = random.choice(ACQUIRE)
        elif field == 'deliver':
            s['deliver'] = random.choice(TARGETS)
        elif field in ('lock', 'release'):
            s[field] = not s[field]
        elif field == 'face':
            s['face'] = random.choice(FACES)
        elif field == 'gate':
            s['gate'] = random.choice(GATES)
        else:
            s['route'] = random.choice(ROUTES)
        if s['acquire'] is None and s['deliver'] is None:
            s['deliver'] = 'wander'
    elif op == 'seg_swap' and len(segs) > 1:
        i, j = random.sample(range(len(segs)), 2)
        segs[i], segs[j] = segs[j], segs[i]
    else:
        return mutate(graph, blame)
    # occasionally copy a role to its sibling (symmetric strategies)
    if random.random() < 0.15:
        g['roles'][1 - ri] = copy.deepcopy(g['roles'][ri])
    return g


def compute_blame(results, team):
    """Associate nodes active at the first-detection moment / timed-out
    segments with lost instances (GaP's root-cause isolation, simplified)."""
    blame = defaultdict(float)
    key_nodes = 'hider_nodes' if team == 'hider' else 'seeker_nodes'
    key_trace = 'hider_trace' if team == 'hider' else 'seeker_trace'
    for r in results:
        if r is None:
            continue
        lost = (not r['hider_win']) if team == 'hider' else r['hider_win']
        for a, node in r[key_nodes].items():
            role = 'role%d' % (int(a) % 2)
            if lost:
                blame[role] += 1.0
            for (sid, status, step) in r[key_trace][a]:
                if status in ('timeout', 'no_target', 'no_object'):
                    blame[role] += 0.5
    n = max(1, sum(1 for r in results if r is not None))
    return {k: v / n for k, v in blame.items()}


def summarize(results):
    rs = [r for r in results if r is not None]
    if not rs:
        return {'n': 0, 'J_hider': 0.5, 'hider_winrate': 0.5, 'behaviours': {}, 'first_seen_step': None}
    beh = {}
    for k in rs[0]['behaviours']:
        app = [r for r in rs if r['applicable'][k]]
        beh[k] = float(np.mean([r['behaviours'][k] for r in app])) if app else 0.0
    fs = [r['first_seen']['step'] for r in rs if r['first_seen']]
    return {'n': len(rs), 'J_hider': float(np.mean([r['J_hider'] for r in rs])),
            'hider_winrate': float(np.mean([r['hider_win'] for r in rs])), 'behaviours': beh,
            'first_seen_step': float(np.mean(fs)) if fs else None,
            'door_block_rate': float(np.mean([np.mean(r['doors_locked']) if r['doors_locked'] else 0.0 for r in rs])),
            'ramp_inside_prep': float(np.mean([r['ramp_inside_prep'] for r in rs])),
            'seeker_entered': float(np.mean([r['seeker_entered'] for r in rs])),
            'seeker_max_z': float(np.mean([r['seeker_max_z'] for r in rs])),
            'boxes_moved': float(np.mean([np.mean(r['boxes_moved_prep']) for r in rs]))}


def feedback_markdown(team, graph, summary, results, iteration):
    """GaP 'Feedback.md': structured rehearsal feedback for the graph-update agent."""
    rs = [r for r in results if r is not None]
    lines = ['# Rehearsal feedback — iteration %d — learning team: %s' % (iteration, team), '',
             '## Current graph', '```', describe_graph(graph), '```', '',
             '## Aggregate (n=%d instances)' % summary['n'],
             '- hider objective J (fraction of play steps all hiders hidden): %.3f' % summary['J_hider'],
             '- hider win-rate: %.2f' % summary['hider_winrate'],
             '- behaviour detection rates: %s' % json.dumps({k: round(v, 2) for k, v in summary['behaviours'].items()}),
             '- mean first-seen play step: %s' % (round(summary['first_seen_step'], 1) if summary['first_seen_step'] else 'never'),
             '- doors sealed+locked at prep end: %.2f, ramp inside quadrant at prep end: %.2f' % (
                 summary.get('door_block_rate', 0), summary.get('ramp_inside_prep', 0)),
             '- seekers entered quadrant: %.2f, mean max seeker z: %.2f' % (
                 summary.get('seeker_entered', 0), summary.get('seeker_max_z', 0)), '',
             '## Failure analysis (lost instances)']
    lost = [r for r in rs if (not r['hider_win']) == (team == 'hider')]
    for r in lost[:8]:
        fs = r['first_seen']
        why = ('seeker %d saw hider %d at play step %d (hider %s quadrant, seeker %s, seeker z=%.2f)' % (
            fs['seeker'], fs['hider'], fs['step'], 'inside' if fs['hider_inside'] else 'outside',
            'inside' if fs['seeker_inside'] else 'outside', fs['seeker_z'])) if fs else 'hiders never seen'
        tr = r['hider_trace'] if team == 'hider' else r['seeker_trace']
        segs = '; '.join('%s:%s@%d' % (sid, status, step) for a in tr for (sid, status, step) in tr[a]) or 'no segments executed'
        lines.append('- p_door=%.2f doors=%d sealed=%s ramp_inside=%s boxes_moved=%s | %s | segments: %s' % (
            r['p_door'], r['n_doors'], r['doors_locked'], r['ramp_inside_prep'], r['boxes_moved_prep'], why, segs))
    return '\n'.join(lines)


def graph_json_schema(team):
    """JSON schema of a graph; constrained decoding then cannot emit out-of-vocabulary values."""
    seg = {'type': 'object', 'additionalProperties': False,
           'required': ['acquire', 'deliver', 'lock', 'release', 'face', 'route', 'gate'],
           'properties': {'acquire': {'enum': ACQUIRE}, 'deliver': {'enum': TARGETS + [None]},
                          'lock': {'type': 'boolean'}, 'release': {'type': 'boolean'},
                          'face': {'enum': FACES}, 'route': {'enum': ROUTES}, 'gate': {'enum': GATES}}}
    play = {'type': 'object', 'additionalProperties': False, 'required': ['behaviour', 'target', 'route', 'segments'],
            'properties': {'behaviour': {'enum': BEHAVIOURS}, 'target': {'enum': TARGETS}, 'route': {'enum': ROUTES},
                           'segments': {'type': 'array', 'items': seg, 'maxItems': 4}}}
    role = {'type': 'object', 'additionalProperties': False, 'required': ['prep', 'play'],
            'properties': {'prep': {'type': 'array', 'items': seg, 'maxItems': 0 if team == 'seeker' else 4},
                           'play': play}}
    params = {'type': 'object', 'additionalProperties': False, 'required': list(PARAM_RANGES),
              'properties': {k: {'type': 'number', 'minimum': lo, 'maximum': hi} for k, (lo, hi) in PARAM_RANGES.items()}}
    return {'type': 'object', 'additionalProperties': False, 'required': ['team', 'assign', 'params', 'roles'],
            'properties': {'team': {'enum': [team]}, 'assign': {'enum': ASSIGNS}, 'params': params,
                           'roles': {'type': 'array', 'items': role, 'minItems': 2, 'maxItems': 2}}}


_STRUCTURED_OUTPUT = [True]   # switched off if the endpoint rejects json_schema response formats


def llm_propose(team, graph, feedback, temperature=0.3):
    """Ask an LLM coding agent for an improved graph (GaP's Graph_Update).
    Returns a validated graph or None."""
    if not cfg.llm_api_key:
        return None
    example_behavior = 'stay'
    example_target = 'stay'
    example_segment = {'acquire': None, 'deliver': 'wander', 'lock': False,
                       'release': False, 'face': 'target', 'route': 'door', 'gate': None}
    schema = {'team': team, 'assign': 'fixed', 'params': default_params(),
              'roles': [{'prep': [example_segment],
                         'play': {'behaviour': example_behavior, 'target': example_target,
                                  'route': 'door', 'segments': []}},
                        {'prep': [],
                         'play': {'behaviour': example_behavior, 'target': example_target,
                                  'route': 'door', 'segments': []}}]}
    grammar = ('Return exactly one JSON object written compactly on a single line (no indentation, no newlines). '
               'No Markdown, prose, or extra keys. '
               'Boolean fields lock and release '
               'must be bare JSON booleans true or false (not strings or numbers). Use this valid '
               'example for the required structure, then change values only to improve the objective: '
               '%s. Allowed values: '
               'assign in %s; segment.acquire in %s; targets in %s; face in %s; route in %s; '
               'play.behaviour in %s; params ranges %s; segment.gate in %s. Gate meanings: '
               'teammate_inside=other teammate entered quadrant, ramp_inside=ramp is inside quadrant, '
               'opponent_visible=opponent currently visible, doors_sealed=all doors blocked, '
               'door=one teammate is near any doorway, null=no gate. Seekers cannot act in preparation. '
               'Field meanings: segment.acquire is the OBJECT to grab and may only be "box", "ramp" or null '
               '(doors and places are not objects). segment.deliver is the PLACE to bring the agent/object to and '
               'must come from the targets list (behaviours such as search/chase/flee are NOT places). '
               'route is only "door" or "direct". play.behaviour must come from the behaviour list. '
               'Gate rule: a gate must not depend on the result of its own segment, otherwise it never fires '
               '(e.g. do not gate "grab box to door_block" on doors_sealed, or "grab ramp to ramp_inside" on ramp_inside). '
               'Atomic skills only: compose them to improve the objective.' % (
                   json.dumps(schema), ASSIGNS, ACQUIRE, TARGETS, FACES, ROUTES, BEHAVIOURS, PARAM_RANGES, GATES))
    # qwen3 soft switch: skip the long hidden reasoning before the answer
    no_think = '\n/no_think' if 'qwen3' in cfg.llm_model.lower() else ''
    messages = [
        {'role': 'system', 'content': 'You are a robot skill-graph optimisation agent in a GaP harness. ' + grammar},
        {'role': 'user', 'content': feedback + '\n\n## Current graph JSON\n' + json.dumps(graph) +
         '\n\nReturn an improved graph for the %s team. Keep the team field exactly %r.' % (team, team) + no_think}]
    for attempt in range(1 + cfg.llm_repairs):
        fmt = ({'type': 'json_schema', 'json_schema': {'name': 'graph', 'strict': True, 'schema': graph_json_schema(team)}}
               if _STRUCTURED_OUTPUT[0] else {'type': 'json_object'})
        body = json.dumps({'model': cfg.llm_model, 'temperature': temperature, 'max_tokens': 2048,
                           'response_format': fmt, 'messages': messages}).encode()
        auth_value = ('Bearer ' + cfg.llm_api_key if cfg.llm_api_key_header.lower() == 'authorization'
                      else cfg.llm_api_key)
        req = urllib.request.Request(cfg.llm_base_url.rstrip('/') + '/chat/completions', data=body, headers={
            'Content-Type': 'application/json', cfg.llm_api_key_header: auth_value})
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                txt = json.loads(resp.read().decode())['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            if e.code == 400 and _STRUCTURED_OUTPUT[0]:
                _STRUCTURED_OUTPUT[0] = False
                print('  LLM endpoint rejected json_schema output; falling back to plain JSON mode', flush=True)
                continue
            print('  LLM proposal failed: %s' % e, flush=True)
            return None
        except Exception as e:
            print('  LLM proposal failed: %s' % e, flush=True)
            return None
        txt = re.sub(r'<think>.*?</think>', '', txt, flags=re.S).strip()
        errors = []
        try:
            g = json.loads(txt)
        except ValueError as e:
            g, errors = None, ['reply is not valid JSON: %s' % e]
        if g is not None and validate_graph(g, team, verbose=True, errors=errors):
            print('  LLM returned a valid %s graph proposal%s' % (
                team, ' (after %d repair%s)' % (attempt, 's' if attempt > 1 else '') if attempt else ''), flush=True)
            return g
        messages += [{'role': 'assistant', 'content': txt},
                     {'role': 'user', 'content': 'The graph is invalid: %s. Fix this problem (and any similar ones) '
                      'and return the full corrected JSON graph.%s' % (errors[0], no_think)}]
    print('  LLM returned an invalid %s graph proposal (after %d repairs)' % (team, cfg.llm_repairs), flush=True)
    return None


# ═════════════════════════════════════════════════════════════════════════════
# TRAINING LOOP  (two-team GaP self-learning)
# ═════════════════════════════════════════════════════════════════════════════

def sample_instances(n, rng):
    return [(float(rng.choice(TASK_SPACE)), int(rng.randint(0, 2 ** 31 - 1))) for _ in range(n)]


def save_plot(history, path):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except Exception:
        return
    if not history['iteration']:
        return
    fig, axes = plt.subplots(3, 1, figsize=(9, 9.5), sharex=True)
    x = np.array(history['episodes']) / 1e6
    J = np.array(history['J_hider'])
    play_steps = cfg.horizon - PREP_STEPS
    axes[0].plot(x, (2 * J - 1) * play_steps, label='hider mean episode reward', color='tab:blue')
    axes[0].plot(x, -(2 * J - 1) * play_steps, label='seeker mean episode reward', color='tab:red', alpha=0.7)
    axes[0].axhline(0, color='k', lw=0.5)
    axes[0].set_ylabel('episode reward (±%d max)' % play_steps)
    axes[0].legend(loc='best', fontsize=8)
    axes[1].plot(x, J, label='hider objective J (fraction of play steps hidden)')
    axes[1].plot(x, history['hider_winrate'], label='hider win-rate', alpha=0.7)
    axes[1].set_ylim(0, 1)
    axes[1].set_ylabel('hider performance')
    axes[1].legend(loc='best', fontsize=8)
    for k in ('chasing', 'door_blocking', 'ramp_use', 'ramp_defense'):
        axes[2].plot(x, history['beh_' + k], label=k)
    axes[2].set_ylim(0, 1)
    axes[2].set_ylabel('behaviour detection rate')
    axes[2].set_xlabel('cumulative rehearsal episodes (millions)')
    axes[2].legend(loc='best', fontsize=8)
    fig.suptitle('GaP two-graph self-learning — hide-and-seek quadrant (%.2fM episodes)' % (x[-1] if len(x) else 0))
    fig.tight_layout()
    fig.savefig(path, dpi=110)
    plt.close(fig)


def save_state(path, state):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(state, f)
    os.replace(tmp, path)


def save_csv(history, path):
    keys = ['iteration', 'episodes', 'learner', 'J_hider', 'hider_winrate',
            'beh_chasing', 'beh_door_blocking', 'beh_ramp_use', 'beh_ramp_defense']
    with open(path, 'w') as f:
        f.write(','.join(keys) + '\n')
        for i in range(len(history['iteration'])):
            f.write(','.join(str(history[k][i]) for k in keys) + '\n')


def oracle_test(pool):
    print('═' * 72)
    print('  ORACLE TEST — validating skill library + behaviour detectors')
    print('  (hand-written graphs; NOT used for training)')
    print('═' * 72)
    hider, seeker = oracle_graphs()
    assert validate_graph(hider, 'hider') and validate_graph(seeker, 'seeker')
    rng = np.random.RandomState(cfg.seed)
    n = 8 if SMOKE else 40
    insts = sample_instances(n, rng)
    for name, hg, sg in [('oracle hiders vs minimal seekers', hider, minimal_graph('seeker')),
                         ('minimal hiders vs oracle seekers', minimal_graph('hider'), seeker),
                         ('oracle hiders vs oracle seekers', hider, seeker),
                         ('minimal vs minimal', minimal_graph('hider'), minimal_graph('seeker'))]:
        t0 = time.time()
        res = pool.run([(hg, sg, p, s) for (p, s) in insts])
        s = summarize(res)
        print('\n%s  (%d instances, %.1fs)' % (name, s['n'], time.time() - t0))
        print('  J_hider=%.3f  hider_winrate=%.2f  behaviours=%s' % (
            s['J_hider'], s['hider_winrate'], {k: round(v, 2) for k, v in s['behaviours'].items()}))
        print('  doors sealed+locked=%.2f  boxes_moved=%.2f  ramp_inside_prep=%.2f  seekers_entered=%.2f  max_z=%.2f' % (
            s['door_block_rate'], s['boxes_moved'], s['ramp_inside_prep'], s['seeker_entered'], s['seeker_max_z']))
        rs = [r for r in res if r is not None]
        if rs:
            print('  sample trace (hiders):', rs[0]['hider_trace'])
            print('  sample trace (seekers):', rs[0]['seeker_trace'])
    print('\nORACLE_TEST_DONE')


def train():
    os.makedirs(cfg.output_dir, exist_ok=True)
    os.makedirs(os.path.join(cfg.output_dir, 'feedback'), exist_ok=True)
    random.seed(cfg.seed)
    np.random.seed(cfg.seed)
    rng = np.random.RandomState(cfg.seed)
    state_path = os.path.join(cfg.output_dir, 'gap_state.json')
    print('═' * 72)
    print('  Hide & Seek — Graph-as-Policy two-team self-learning')
    print('═' * 72)
    print('  workers=%d  budget=%s episodes  rehearsals/candidate=%d  both teams updated every round' % (
        cfg.n_workers, '{:,}'.format(cfg.total_episodes), cfg.rehearsals))
    print('  belief space: p_door ∈ %s, random spawns;  omniscient objects: %s' % (TASK_SPACE, cfg.omniscient_objects))
    if cfg.llm_only and not cfg.llm_api_key:
        sys.exit('GAP_LLM_ONLY=1 needs an LLM endpoint: set GAP_LLM_API_KEY (use "ollama" for local Ollama)')
    if not cfg.llm_api_key:
        agent = 'failure-weighted structural search (no GAP_LLM_API_KEY set)'
    elif cfg.llm_only:
        agent = ('LLM only (%s): %d continuous writers per team, temperature %.2f, %d repair retries, '
                 '%.0fs collection window per round, no structural search') % (
            cfg.llm_model, cfg.llm_proposals, cfg.llm_temperature, cfg.llm_repairs, cfg.round_window)
    else:
        agent = 'LLM (%s): %d proposal(s) per team per round + structural search' % (cfg.llm_model, cfg.llm_proposals)
    print('  graph-update agent: %s' % agent)
    print('  acceptance margin: %.3f' % cfg.accept_margin)
    print('  output: %s' % cfg.output_dir)
    pool = RehearsalPool(cfg.n_workers, cfg.seed)
    if ORACLE:
        oracle_test(pool)
        pool.close()
        return

    # ── state (resume if present) ─────────────────────────────────────────
    if os.path.exists(state_path):
        with open(state_path) as f:
            S = json.load(f)
        print('  resumed from iteration %d' % S['iteration'])
    else:
        S = {'iteration': 0, 'episodes': 0,
             'hider': minimal_graph('hider'), 'seeker': minimal_graph('seeker'),
             'hider_pool': [], 'seeker_pool': [],
             'best_J': {'hider': None, 'seeker': None}, 'since_improve': {'hider': 0, 'seeker': 0},
             'onsets': {}, 'history': defaultdict(list)}
    hist = defaultdict(list, S['history'])
    stop = {'flag': False}
    signal.signal(signal.SIGINT, lambda *a: stop.__setitem__('flag', True))
    signal.signal(signal.SIGTERM, lambda *a: stop.__setitem__('flag', True))

    t_start = time.time()
    ep_start = S['episodes']
    TEAMS = ('hider', 'seeker')
    n_llm = cfg.llm_proposals if cfg.llm_api_key else 0
    # writers always improve the latest graph using the latest report; finished proposals land in the inbox
    llm_ctx, ctx_lock, inbox, writers_stop = {}, threading.Lock(), queue.Queue(), threading.Event()

    def llm_writer(team, k):
        while not writers_stop.is_set():
            with ctx_lock:
                ctx = llm_ctx.get(team)
            if ctx is None:
                time.sleep(1)
                continue
            g = llm_propose(team, ctx[0], ctx[1], cfg.llm_temperature)
            if g is not None:
                inbox.put((team, g, 'LLM writer %d' % (k + 1)))

    writers_started = False
    # rehearsal results of each team's current graph from the previous round (feedback source)
    last_res = {'hider': None, 'seeker': None}
    while S['episodes'] < cfg.total_episodes and (cfg.iterations <= 0 or S['iteration'] < cfg.iterations) and not stop['flag']:
        it = S['iteration']
        instances = sample_instances(cfg.rehearsals, rng)
        orng = random.Random(instances[0][1])
        # one fixed opponent per instance, shared by the baseline and every candidate (paired comparison)
        opps = {}
        for team, other in (('hider', 'seeker'), ('seeker', 'hider')):
            past = S[other + '_pool']
            opps[team] = [orng.choice(past) if past and orng.random() < cfg.pool_prob else S[other]
                          for _ in instances]

        def jobs_for(team, g):
            return [((g, o) if team == 'hider' else (o, g)) + tuple(inst) for o, inst in zip(opps[team], instances)]

        # 1) baselines of both current graphs (instances where both face the current opponent are shared)
        shared = {i for i in range(len(instances)) if opps['hider'][i] is S['seeker'] and opps['seeker'][i] is S['hider']}
        base_s_jobs = [j for i, j in enumerate(jobs_for('seeker', S['seeker'])) if i not in shared]
        base_futs = {'hider': pool.submit(jobs_for('hider', S['hider'])), 'seeker': pool.submit(base_s_jobs)}
        n_eps = len(instances) + len(base_s_jobs)
        base = {}

        def collect_base():
            if not base:
                bh, bs = base_futs['hider'].result(), iter(base_futs['seeker'].result())
                base['hider'] = bh
                base['seeker'] = [bh[i] if i in shared else next(bs) for i in range(len(instances))]
            return base

        # feedback comes from last round's rehearsal of the current graphs, so the LLM starts right away
        fb_res = last_res if all(last_res[t] is not None for t in TEAMS) else collect_base()
        fbs, blames = {}, {}
        for team in TEAMS:
            blames[team] = compute_blame(fb_res[team], team)
            fbs[team] = feedback_markdown(team, S[team], summarize(fb_res[team]), fb_res[team], it)
            with open(os.path.join(cfg.output_dir, 'feedback', 'iter_%04d_%s.md' % (it, team)), 'w') as f:
                f.write(fbs[team])
        with ctx_lock:
            for team in TEAMS:
                llm_ctx[team] = (copy.deepcopy(S[team]), fbs[team])
        if n_llm and not writers_started:
            for team in TEAMS:
                for k in range(n_llm):
                    threading.Thread(target=llm_writer, args=(team, k), daemon=True).start()
            writers_started = True

        # 2) collect candidates for both teams during the window; each starts rehearsing as soon as it arrives
        cands = {t: [] for t in TEAMS}
        seen = {t: {graph_signature(S[t])} for t in TEAMS}

        def add(team, g, source):
            sig = graph_signature(g)
            if sig in seen[team]:
                return False
            seen[team].add(sig)
            cands[team].append((g, source, pool.submit(jobs_for(team, g))))
            return True

        if not cfg.llm_only:
            for team in TEAMS:
                extra_edits = min(3, S['since_improve'][team] // cfg.plateau_patience)
                added = tries = 0
                while added < cfg.candidates - n_llm and tries < 200:
                    tries += 1
                    g = mutate(S[team], blames[team])
                    for _ in range(random.choice([0, 0, 1, 2]) + extra_edits):
                        g = mutate(g, blames[team])
                    if validate_graph(g, team) and add(team, g, 'structural search'):
                        added += 1
        window_end = time.time() + (cfg.round_window if n_llm else 0)
        while True:
            try:
                team, g, src = inbox.get(timeout=max(0.0, window_end - time.time()))
            except queue.Empty:
                break
            if not add(team, g, src):
                print('  LLM proposal duplicates an existing %s graph; skipping' % team, flush=True)
        collect_base()

        # 3) accept, per team, the best candidate that beats its baseline on the same instances
        improved = {}
        for team in TEAMS:
            def score(summary):
                return summary['J_hider'] if team == 'hider' else 1.0 - summary['J_hider']
            best_c, best_res = None, base[team]
            best_score = score(summarize(base[team]))
            for g, src, fut in cands[team]:
                res = fut.result()
                n_eps += len(res)
                s_ = summarize(res)
                sc_ = score(s_) - 0.002 * sum(len(r['prep']) + len(r['play']['segments']) for r in g['roles'])
                if s_['n'] > 0 and sc_ > best_score + cfg.accept_margin:
                    best_c, best_res, best_score = (g, src), res, sc_
            improved[team] = best_c is not None
            if improved[team]:
                S[team + '_pool'].append(copy.deepcopy(S[team]))
                S[team + '_pool'] = S[team + '_pool'][-cfg.pool_size:]
                S[team] = best_c[0]
                print('  accepted %s candidate for %s' % (best_c[1], team), flush=True)
            else:
                print('  no candidate improved the %s graph' % team, flush=True)
            last_res[team] = best_res
            prev_best = S['best_J'][team]
            if prev_best is None or best_score > prev_best + 1e-6:
                S['best_J'][team] = best_score
            S['since_improve'][team] = 0 if improved[team] else S['since_improve'][team] + 1
        S['episodes'] += n_eps

        # 4) logging / behaviour onsets (measured on the round's baseline: current hiders vs current seekers)
        cur_s = summarize(base['hider'])
        hist['iteration'].append(it)
        hist['episodes'].append(S['episodes'])
        hist['learner'].append('both')
        hist['J_hider'].append(cur_s['J_hider'])
        hist['hider_winrate'].append(cur_s['hider_winrate'])
        for k in ('chasing', 'door_blocking', 'ramp_use', 'ramp_defense'):
            rate = cur_s['behaviours'].get(k, 0.0)
            hist['beh_' + k].append(rate)
            if k not in S['onsets'] and rate >= ONSET_THRESHOLD[k]:
                S['onsets'][k] = {'iteration': it, 'episodes': S['episodes'], 'rate': rate}
                print('  ★ emergent behaviour detected: %-13s at iteration %d (%.2fM rehearsal episodes, rate %.2f)' % (
                    k, it, S['episodes'] / 1e6, rate))
        S['iteration'] = it + 1
        S['history'] = dict(hist)
        elapsed = time.time() - t_start
        eps_rate = (S['episodes'] - ep_start) / max(elapsed, 1e-6)
        print('[it %5d | %6.3fM eps | %5.1f eps/s | %6.0fs] J_h=%.3f WR_h=%.2f H%s S%s beh=%s stale(h/s)=%d/%d' % (
            it, S['episodes'] / 1e6, eps_rate, elapsed, cur_s['J_hider'], cur_s['hider_winrate'],
            '+' if improved['hider'] else '.', '+' if improved['seeker'] else '.',
            {ABBR[k]: round(v, 2) for k, v in cur_s['behaviours'].items()},
            S['since_improve']['hider'], S['since_improve']['seeker']), flush=True)
        for team in TEAMS:
            if improved[team]:
                print('  new %s graph:\n%s' % (team, '\n'.join('    ' + l for l in describe_graph(S[team]).split('\n'))), flush=True)
        save_state(state_path, S)
        with open(os.path.join(cfg.output_dir, 'best_hider_graph.json'), 'w') as f:
            json.dump(S['hider'], f, indent=1)
        with open(os.path.join(cfg.output_dir, 'best_seeker_graph.json'), 'w') as f:
            json.dump(S['seeker'], f, indent=1)
        save_plot(hist, os.path.join(cfg.output_dir, 'learning_curve.png'))
        save_csv(hist, os.path.join(cfg.output_dir, 'history.csv'))
        if S['since_improve']['hider'] >= cfg.plateau_patience and S['since_improve']['seeker'] >= cfg.plateau_patience:
            if cfg.stop_on_plateau:
                print('  both teams plateaued for %d iterations — stopping (GaP plateau criterion)' % cfg.plateau_patience)
                break
            if S['since_improve']['hider'] % cfg.plateau_patience == 0:
                print('  both teams plateaued for %d iterations — boosting exploration' % S['since_improve']['hider'], flush=True)

    save_state(state_path, S)
    save_plot(hist, os.path.join(cfg.output_dir, 'learning_curve.png'))
    save_csv(hist, os.path.join(cfg.output_dir, 'history.csv'))
    writers_stop.set()
    pool.close()
    print('═' * 72)
    print('  DONE — %d iterations, %.3fM rehearsal episodes, %.0f s' % (S['iteration'], S['episodes'] / 1e6, time.time() - t_start))
    print('  behaviour onsets: %s' % json.dumps(S['onsets']))
    print('  final hider graph:\n%s' % describe_graph(S['hider']))
    print('  final seeker graph:\n%s' % describe_graph(S['seeker']))
    print('  artefacts: %s' % cfg.output_dir)


if __name__ == '__main__':
    mp.set_start_method('fork')
    train()
