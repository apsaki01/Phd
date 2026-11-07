#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
  Hide & Seek Training — OpenAI Architecture + AdA Innovations
  ─────────────────────────────────────────────────────────────
  Policy architecture: EXACT match to OpenAI's pretrained policy
    - Circular Conv1D on lidar
    - Per-entity dense embeddings (128)
    - Entity self-attention (4 heads, 128 embd)
    - Entity pooling → Dense 256 → LSTM 256 → LayerNorm
    - Separate policy_net and vpred_net (not shared)
    - Observation normalization (running mean/std)

  AdA innovations (on top of OpenAI's architecture):
    1. Opponent pool   — seekers sometimes play against past snapshots
    2. Task curriculum  — progressive door-dropout difficulty

  PPO hyperparameters: Match OpenAI paper (Table S.1)
  Environment config:  EXACT match to hide_and_seek_quadrant.jsonnet

  Target: 3 M episodes, ~1.5 weeks on 12-core CPU (Rosetta)
  Speed:  Subprocess env workers (5× env speedup), LSTM (3× vs TXL)
═══════════════════════════════════════════════════════════════════════════════
"""

import os, sys, time, pickle, signal, threading, random
import multiprocessing as mp
from multiprocessing import shared_memory
from copy import deepcopy
from collections import deque

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

torch.set_num_threads(16)  # vast.ai 4090 box: 32+ cores available

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(REPO_DIR)  # shared env folders live at the Phd repo root
sys.path.insert(0, os.path.join(ROOT_DIR, 'mujoco-worldgen'))
sys.path.insert(0, os.path.join(ROOT_DIR, 'multi-agent-emergence-environments'))

os.environ.setdefault('MUJOCO_PY_MJPRO_PATH', os.path.expanduser('~/.mujoco/mjpro150'))
os.environ.setdefault('MUJOCO_PY_MJKEY_PATH', os.path.expanduser('~/.mujoco/mjkey.txt'))
os.environ.setdefault('MUJOCO_GL', 'osmesa')
ld = os.environ.get('LD_LIBRARY_PATH', '')
_mujoco_bin = os.path.join(os.environ['MUJOCO_PY_MJPRO_PATH'], 'bin')
if _mujoco_bin not in ld.split(os.pathsep):
    os.environ['LD_LIBRARY_PATH'] = _mujoco_bin + (os.pathsep + ld if ld else '')

import gym, gym.spaces
if not hasattr(gym.spaces, 'dict_space'):
    gym.spaces.dict_space = gym.spaces.dict
if not hasattr(gym.spaces, 'tuple_space'):
    gym.spaces.tuple_space = gym.spaces.tuple

from mae_envs.envs.hide_and_seek import make_env
from mae_envs.wrappers.util import normalize_action_dict

import warnings
warnings.filterwarnings('ignore')


# ═════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═════════════════════════════════════════════════════════════════════════════

class Config:
    # ── Training ──────────────────────────────────────────────────────────
    total_episodes       = 43_400_000  # Run 3 (adaptive): OpenAI's exact final (43.4M) — all 4 milestones
    n_envs               = 128         # OpenAI setting — full 128 workers on vast.ai RTX 4090
    horizon              = 80          # EXACT OpenAI
    prep_fraction        = 0.4         # EXACT OpenAI (32 prep + 48 play)
    n_hiders             = 2
    n_seekers            = 2
    n_agents             = 4
    seed                 = 0           # global RNG seed (numpy/torch/random/env); override with the SEED env var

    # ── PPO  (EXACT OpenAI paper Table S.1) ──────────────────────────────
    gamma                = 0.998       # OpenAI paper: 0.998
    gae_lambda           = 0.95        # OpenAI paper: 0.95
    clip_range           = 0.2         # OpenAI paper: 0.2
    lr                   = 5e-4        # OpenAI paper: 5e-4, linear decay → 0
    entropy_coef         = 0.012       # Run 3: nudged up from 0.01 — sustains exploration of the compound ramp-use skill at our smaller scale
    vf_coef              = 1.0         # OpenAI paper: 1.0
    max_grad_norm        = 0.5         # OpenAI paper: 0.5
    ppo_epochs           = 4           # EXACT OpenAI paper: 4
    n_minibatches        = 1           # OpenAI paper: full batch
    normalize_advantages = True

    # ── Architecture  (EXACT match to OpenAI pretrained policy) ───────────
    d_embed              = 128         # entity embedding dim
    sa_heads             = 4           # self-attention heads
    sa_embd              = 128         # self-attention n_embd
    lstm_hidden          = 256         # LSTM hidden size
    dense_hidden         = 256         # post-pooling dense
    lidar_filters        = 9           # circ conv1d filters
    lidar_kernel         = 3           # circ conv1d kernel size

    # ── Ramp locking  (DISABLED for run4 — ramp-defense = DRAG INSIDE, not lock) ─
    # We deliberately turn OFF ramp locking.  Locking is a denial mechanic that is
    # NOT required to move a ramp (that is the grab mechanic) or to climb it (pure
    # physics).  With locking off:
    #   • seekers can ALWAYS move the ramp to a wall and climb over it, and
    #   • hiders can never freeze it in the open — their only defense is to
    #     physically DRAG the ramp inside their quadrant and wall it off with the
    #     (still-lockable) boxes.
    # lock_ramp=True would append 3 lock dims (you_lock, team_lock, obj_lock) to
    # ramp_obs (ramp_feat 9 → 12); with it False, ramp_feat = 9.  The network +
    # normaliser both read ramp_feat so the obs shape stays consistent.
    # (Box locking stays ON — lock_box=True — so door-blocking is unaffected.)
    lock_ramp            = False
    ramp_feat            = 12 if lock_ramp else 9

    # ── Opponent Pool  (AdA Innovation 1) ─────────────────────────────────
    opponent_pool_size   = 10
    opponent_save_freq   = 100_000     # Run 2: was 50k → 100k (less frequent snapshots)
    opponent_sample_prob = 0.3         # 30 % chance seekers use past policy
    opponent_pool_start  = 100_000     # Run 2: was 10k → 100k (delay self-play until base skills emerge)

    # ── Adaptive Task Sampler  (PLR — replaces Run 2's hand-scheduled curriculum) ──
    # Focused, obs-shape-safe task space over p_door_dropout (1 vs 2 doors),
    # defined as TASK_SPACE below.  The sampler scores each config by an EMA of
    # mean |GAE advantage| (a positive-value-loss / regret proxy), NOT win-rate
    # variance — see PrioritizedTaskSampler for why that distinction is what
    # makes ramp-use emerge instead of stalling (the Run 3 failure mode).
    task_warmup_episodes = 2_000_000   # bootstrap door-blocking on the spine config first
    task_easy_idx        = 0           # TASK_SPACE[0] = p_door_dropout 1.0 (1 door, fully blockable)
    task_staleness_coef  = 0.3         # PLR staleness mixing (coverage / anti-forgetting)
    task_beta            = 0.5         # rank-based prioritisation sharpness (lower = sharper)
    task_ema_decay       = 0.9         # EMA decay for each config's learnability score
    task_floor_prob      = 0.15        # floor probability kept on the spine config (anti-forget)
    task_hold_batches    = 20          # batches to run per task before resampling (amortises remake)

    # ── Logging / checkpointing ──────────────────────────────────────────
    # Save a milestone .npz every 500k episodes and KEEP THEM ALL (~87 files ≈
    # 6.8 GB on the 190 GB disk) so every OpenAI-style phase can be rendered
    # later.  A separate resume_latest.npz (overwritten every resume_freq) gives
    # crash-recovery granularity finer than 500k without cluttering that set.
    checkpoint_freq      = 500_000     # milestone .npz every 500k eps
    keep_last_checkpoints = 0          # 0 = keep ALL milestone checkpoints
    resume_freq          = 250_000     # overwrite resume_latest.npz this often (crash safety)
    plot_freq            = 1_000       # update learning_curve.png every 1 k
    terminal_freq        = 32          # print line every N eps (= 1 batch)
    diagnostic_freq      = 10_000      # Run 2: was 5k → 10k (less log spam)
    early_export_ep      = 32          # one-time export after first batch

    # ── Paths  (Run 4 = fresh start with the fixed env: ramp always spawns
    #    OUTSIDE the hider quadrant.  Own dir so it never collides with Run 3) ──
    output_dir           = os.path.abspath(os.environ.get('OUTPUT_DIR', os.path.join(REPO_DIR, 'training_output')))
    checkpoint_dir       = os.path.join(output_dir, 'checkpoints')
    plot_path            = os.path.join(output_dir, 'learning_curve.png')
    final_npz_path       = os.path.join(output_dir, 'final_policy.npz')
    device               = 'cuda' if torch.cuda.is_available() else 'cpu'

cfg = Config()

# ── Smoke-test mode: SMOKE_TEST=1 runs a tiny end-to-end validation ────────
# Exercises the whole pipeline (env build w/ lock_ramp, policy fwd w/
# ramp_feat=12, PPO update, adaptive task sampling + env remake, checkpoint
# save+prune, diagnostics) in a few minutes before the multi-week real run.
if os.environ.get('SMOKE_TEST', '0') == '1':
    cfg.total_episodes       = 3_000
    cfg.task_warmup_episodes = 1_000
    cfg.task_hold_batches    = 3
    cfg.checkpoint_freq      = 1_024
    cfg.resume_freq          = 512
    cfg.diagnostic_freq      = 512
    cfg.plot_freq            = 512
    cfg.opponent_pool_start  = 512
    cfg.opponent_save_freq   = 1_024
    cfg.output_dir           = os.path.join(REPO_DIR, 'training_output_smoke')
    cfg.checkpoint_dir       = os.path.join(cfg.output_dir, 'checkpoints')
    cfg.plot_path            = os.path.join(cfg.output_dir, 'learning_curve.png')
    cfg.final_npz_path       = os.path.join(cfg.output_dir, 'final_policy.npz')
    print('>>> SMOKE_TEST mode: 3,000 episodes in a separate output dir <<<')

# ── Reproducibility: override the global seed via the SEED env var ─────────
# Used by the curriculum on/off x {0,1,2} ablation: run each with SEED=0/1/2.
if os.environ.get('SEED') is not None:
    cfg.seed = int(os.environ['SEED'])


def set_global_seed(seed):
    """Seed every RNG that drives the LEARNER process (task sampler, opponent
    sampling, minibatch permutation, action/parameter sampling). Worker envs are
    seeded separately (base seed + worker index) inside the vec-env classes."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)




# ═════════════════════════════════════════════════════════════════════════════
# ENVIRONMENT — EXACT match to OpenAI hide_and_seek_quadrant.jsonnet
# ═════════════════════════════════════════════════════════════════════════════

BASE_ENV_KWARGS = dict(
    n_hiders=cfg.n_hiders, n_seekers=cfg.n_seekers,
    grab_box=True, grab_out_of_vision=False,
    grab_selective=False, grab_exclusive=False,
    lock_box=True, lock_type='all_lock_team_specific',
    lock_out_of_vision=False,
    n_substeps=15, horizon=cfg.horizon, scenario='quadrant',
    prep_fraction=cfg.prep_fraction, rew_type='joint_zero_sum',
    restrict_rect=[0.1, 0.1, 5.9, 5.9], p_door_dropout=0.5,
    quadrant_game_hider_uniform_placement=True,
    # ramp_outside_quadrant=False  ->  uniform_placement (EXACTLY run3).
    # Forcing the ramp outside the quadrant (True) moved it away from the
    # door-fight, so neither team ever touched it and seekers never bootstrapped
    # ramp-use (the ~7M "dip" vanished, zero ramp interactions).  Uniform spawns
    # put the ramp in/near the quadrant often enough that accidental encounters
    # accumulate into ramp-use, then hiders must learn to DRAG it inside (lock off).
    ramp_outside_quadrant=False,
    n_boxes=2, box_only_z_rot=True, boxid_obs=False,
    n_ramps=1, lock_ramp=cfg.lock_ramp, penalize_objects_out=True,
    n_food=0,
    n_lidar_per_agent=30, prep_obs=True,
)

ACT_MOVE_BINS = 11
ACT_MOVE_DIM  = 3
ACT_PULL_DIM  = 2
ACT_GLUE_DIM  = 2


# ══════════════════════════════════════════════════════════════════════════
# ADAPTIVE TASK SAMPLER  (PLR — Prioritized Level Replay, Jiang et al. 2021)
#
# Replaces Run 2's hand-scheduled curriculum AND fixes the bug that stalled the
# failed Run 3.  Each task (a p_door_dropout setting) is scored by an EMA of the
# mean |GAE advantage| it produces — a positive-value-loss / regret proxy — NOT
# by win-rate variance p(1-p).
#
# Why this matters for ramp-use:
#   A fully-blocked 1-door quadrant has seeker win-rate ≈ 0, so p(1-p) ≈ 0 and a
#   variance sampler ABANDONS exactly the config where ramp-use must emerge.
#   Mean |advantage| stays HIGH there (the value net knows seekers *could* win
#   by going over the wall but they don't yet), so PLR keeps that config hot
#   until the compound skill crystallises.
#
# The task space is FOCUSED (5 configs) and obs-shape-SAFE so the ShmemVecEnv
# shared buffers never change shape across remake() (only p_door_dropout varies;
# entity counts / lock flags / lidar are fixed for the whole run).
# ══════════════════════════════════════════════════════════════════════════

# Ordered easy → hard.  Index 0 (1 door, fully blockable) is the bootstrap
# 'spine' config AND the strongest ramp-use pressure (once a single door is
# sealed the only way in is over the wall).
TASK_SPACE = [
    {'p_door_dropout': 1.0},   # 0: ~always 1 door  — easiest to fully block → forces ramp use
    {'p_door_dropout': 0.75},  # 1
    {'p_door_dropout': 0.50},  # 2
    {'p_door_dropout': 0.25},  # 3
    {'p_door_dropout': 0.0},   # 4: ~always 2 doors — hardest to fully block
]


class PrioritizedTaskSampler:
    """Rank-based PLR over TASK_SPACE.  Scale-invariant (ranks, not raw scores),
    with a warmup that bootstraps door-blocking on the spine config, staleness
    mixing for coverage, and a floor probability on the spine config so the
    door-blocking skill is never catastrophically forgotten."""

    def __init__(self, n_tasks, warmup_episodes, easy_idx=0,
                 staleness_coef=0.3, beta=0.5, ema_decay=0.9,
                 floor_prob=0.15, warmup_easy_prob=0.85):
        self.n = n_tasks
        self.warmup = warmup_episodes
        self.easy_idx = easy_idx
        self.rho = staleness_coef
        self.beta = beta
        self.ema = ema_decay
        self.floor = floor_prob
        self.warmup_easy_prob = warmup_easy_prob
        self.scores = np.full(n_tasks, np.nan)          # learnability EMA (mean|adv|)
        self.last_seen = np.zeros(n_tasks)              # episode last sampled
        self.sample_count = np.zeros(n_tasks, dtype=np.int64)
        self.win_h = [deque(maxlen=400) for _ in range(n_tasks)]  # per-config hider winrate

    def sample(self, episode):
        # Warmup: bootstrap door-blocking on the spine config, with a little
        # neighbour exploration so the sampler gathers data on the others too.
        if episode < self.warmup:
            if np.random.random() < self.warmup_easy_prob:
                return self.easy_idx
            return int(np.random.randint(self.n))
        # Force-sample any config we have no learnability score for yet.
        unseen = np.isnan(self.scores)
        if unseen.any():
            return int(np.random.choice(np.where(unseen)[0]))
        return int(np.random.choice(self.n, p=self._distribution(episode)))

    def _distribution(self, episode):
        s = np.nan_to_num(self.scores, nan=0.0)
        # Rank-based prioritisation (scale-invariant): rank 1 = highest score.
        order = np.argsort(-s, kind='stable')
        ranks = np.empty(self.n, dtype=np.float64)
        ranks[order] = np.arange(1, self.n + 1)
        p_learn = 1.0 / np.power(ranks, 1.0 / self.beta)
        p_learn /= p_learn.sum()
        # Staleness term (coverage / anti-forgetting).
        stale = episode - self.last_seen
        p_stale = stale / stale.sum() if stale.sum() > 0 else np.ones(self.n) / self.n
        p = (1.0 - self.rho) * p_learn + self.rho * p_stale
        # Floor on the spine config so door-blocking is never forgotten.
        p *= (1.0 - self.floor)
        p[self.easy_idx] += self.floor
        p /= p.sum()
        return p

    def update(self, idx, episode, mean_abs_adv, hider_wins):
        if np.isnan(self.scores[idx]):
            self.scores[idx] = mean_abs_adv
        else:
            self.scores[idx] = self.ema * self.scores[idx] + (1.0 - self.ema) * mean_abs_adv
        self.last_seen[idx] = episode
        self.sample_count[idx] += 1
        for w in hider_wins:
            self.win_h[idx].append(w)

    def report(self):
        tot = max(int(self.sample_count.sum()), 1)
        lines = []
        for i in range(self.n):
            share = 100.0 * self.sample_count[i] / tot
            wr = float(np.mean(self.win_h[i])) if len(self.win_h[i]) else float('nan')
            sc = 0.0 if np.isnan(self.scores[i]) else self.scores[i]
            pd = TASK_SPACE[i]['p_door_dropout']
            lines.append(
                f"  │   task#{i} p_door={pd:.2f}  share {share:4.1f}%  "
                f"hiderWR {wr:.2f}  |adv|EMA {sc:.3f}  n={int(self.sample_count[i])}")
        return "\n".join(lines)

    def get_state(self):
        return {
            'scores': self.scores.copy(),
            'last_seen': self.last_seen.copy(),
            'sample_count': self.sample_count.copy(),
            'win_h': [list(w) for w in self.win_h],
        }

    def set_state(self, state):
        self.scores = np.asarray(state['scores'], dtype=np.float64)
        self.last_seen = np.asarray(state['last_seen'], dtype=np.float64)
        self.sample_count = np.asarray(state['sample_count'], dtype=np.int64)
        self.win_h = [deque(w, maxlen=400) for w in state['win_h']]


def make_single_env(overrides=None):
    kw = dict(BASE_ENV_KWARGS)
    if overrides:
        kw.update(overrides)
    return make_env(**kw)


# ═════════════════════════════════════════════════════════════════════════════
# SUBPROCESS VECTORISED ENVIRONMENT
# ═════════════════════════════════════════════════════════════════════════════

def _env_worker(pipe, env_kwargs, seed=None):
    """Runs in a subprocess."""
    env = make_env(**env_kwargs)
    if seed is not None and hasattr(env, 'seed'):
        try:
            env.seed(seed)
        except Exception:
            pass
    try:
        while True:
            cmd, data = pipe.recv()
            if cmd == 'reset':
                pipe.send(env.reset())
            elif cmd == 'step':
                obs, rew, done, info = env.step(data)
                pipe.send((obs, rew, done))
            elif cmd == 'remake':
                env = make_env(**data)
                if seed is not None and hasattr(env, 'seed'):
                    try:
                        env.seed(seed)
                    except Exception:
                        pass
                pipe.send(True)
            elif cmd == 'close':
                break
    except (EOFError, BrokenPipeError):
        pass
    finally:
        pipe.close()


class SubprocVecEnv:
    """N envs in subprocesses, async step / reset."""

    def __init__(self, n, env_kwargs, seed=None):
        self.n = n
        self.pipes = []
        self.procs = []
        for i in range(n):
            parent, child = mp.Pipe()
            worker_seed = None if seed is None else seed + i
            p = mp.Process(target=_env_worker, args=(child, env_kwargs, worker_seed),
                           daemon=True)
            p.start()
            child.close()
            self.pipes.append(parent)
            self.procs.append(p)

    def reset_all(self):
        for p in self.pipes:
            p.send(('reset', None))
        return [p.recv() for p in self.pipes]

    def step_async(self, actions_list):
        for p, a in zip(self.pipes, actions_list):
            p.send(('step', a))

    def step_wait(self):
        return [p.recv() for p in self.pipes]

    def step(self, actions_list):
        self.step_async(actions_list)
        return self.step_wait()

    def remake(self, env_kwargs):
        for p in self.pipes:
            p.send(('remake', env_kwargs))
        for p in self.pipes:
            p.recv()

    def close(self):
        for p in self.pipes:
            try:
                p.send(('close', None))
            except Exception:
                pass
        for p in self.procs:
            p.join(timeout=3)
            if p.is_alive():
                p.terminate()


# ═════════════════════════════════════════════════════════════════════════════
# SHARED-MEMORY VECTORISED ENVIRONMENT  (Option C optimization)
#   Same public interface as SubprocVecEnv, but moves the large observation
#   arrays through POSIX shared memory instead of pickling them over pipes.
#   Pipes are still used for tiny command/ack signaling (so synchronization
#   semantics are identical to SubprocVecEnv — no semaphore races possible).
# ═════════════════════════════════════════════════════════════════════════════

def _shmem_env_worker(pipe, env_kwargs, my_idx, shm_info, n_envs, seed=None):
    """Worker that writes obs directly into shared-memory buffers.

    shm_info: dict {key: (shm_name, per_env_shape, dtype_str)}
    Worker attaches to each shm by name and owns slot [my_idx].
    """
    # Attach to shared memory created by parent
    shms = {}
    arrs = {}
    for k, (name, shape, dtype_str) in shm_info.items():
        shm = shared_memory.SharedMemory(name=name)
        shms[k] = shm
        arrs[k] = np.ndarray((n_envs,) + tuple(shape),
                             dtype=np.dtype(dtype_str), buffer=shm.buf)

    env = make_env(**env_kwargs)
    if seed is not None and hasattr(env, 'seed'):
        try:
            env.seed(seed)
        except Exception:
            pass

    def _write_obs(obs):
        for k in arrs:
            if k in obs:
                arrs[k][my_idx] = obs[k]

    try:
        while True:
            cmd, data = pipe.recv()
            if cmd == 'reset':
                obs = env.reset()
                _write_obs(obs)
                pipe.send('ok')
            elif cmd == 'step':
                obs, rew, done, info = env.step(data)
                _write_obs(obs)
                # rewards/done are tiny → stay in pipe
                pipe.send((rew, done))
            elif cmd == 'remake':
                env = make_env(**data)
                if seed is not None and hasattr(env, 'seed'):
                    try:
                        env.seed(seed)
                    except Exception:
                        pass
                pipe.send(True)
            elif cmd == 'close':
                break
    except (EOFError, BrokenPipeError):
        pass
    finally:
        for shm in shms.values():
            try:
                shm.close()
            except Exception:
                pass
        pipe.close()


class ShmemVecEnv:
    """N envs in subprocesses; observations shared via POSIX shared memory.

    Identical public interface to SubprocVecEnv so collect_vectorized() does
    not need to change. Actions / rewards / done still go through pipes
    (they are tiny; pickling cost is negligible).
    """

    def __init__(self, n, env_kwargs, seed=None):
        self.n = n
        # 1) Probe one env to discover exact obs keys / shapes / dtypes.
        probe = make_env(**env_kwargs)
        probe_obs = probe.reset()
        # Only share keys that are ndarrays (skip any scalars / non-array keys)
        self.obs_keys = [k for k, v in probe_obs.items()
                         if isinstance(v, np.ndarray)]
        self.obs_shapes = {k: probe_obs[k].shape for k in self.obs_keys}
        self.obs_dtypes = {k: probe_obs[k].dtype for k in self.obs_keys}
        # Release probe env memory before launching workers
        try:
            if hasattr(probe, 'close'):
                probe.close()
        except Exception:
            pass
        del probe, probe_obs

        # 2) Allocate shared memory: one block per obs key, shape (n, *per_env).
        self.shms = {}
        self.arrs = {}
        for k in self.obs_keys:
            shape = (n,) + tuple(self.obs_shapes[k])
            nbytes = int(np.prod(shape)) * np.dtype(self.obs_dtypes[k]).itemsize
            if nbytes == 0:
                # Skip zero-size obs (e.g. unused 'food_obs' when n_food=0)
                continue
            shm = shared_memory.SharedMemory(create=True, size=nbytes)
            self.shms[k] = shm
            self.arrs[k] = np.ndarray(shape, dtype=self.obs_dtypes[k],
                                      buffer=shm.buf)
        # Final list of keys that actually have shmem backing
        self.obs_keys = list(self.arrs.keys())

        # 3) Launch workers.
        shm_info = {k: (self.shms[k].name,
                        tuple(self.obs_shapes[k]),
                        str(self.obs_dtypes[k]))
                    for k in self.obs_keys}
        self.pipes = []
        self.procs = []
        for i in range(n):
            parent, child = mp.Pipe()
            worker_seed = None if seed is None else seed + i
            p = mp.Process(target=_shmem_env_worker,
                           args=(child, env_kwargs, i, shm_info, n, worker_seed),
                           daemon=True)
            p.start()
            child.close()
            self.pipes.append(parent)
            self.procs.append(p)

    def _snapshot_obs(self, ei):
        """Copy one env's obs out of shared memory so the worker can safely
        overwrite the slot on the next step."""
        return {k: self.arrs[k][ei].copy() for k in self.obs_keys}

    def reset_all(self):
        for p in self.pipes:
            p.send(('reset', None))
        # Wait for all workers to finish writing obs into shmem
        for p in self.pipes:
            p.recv()
        return [self._snapshot_obs(ei) for ei in range(self.n)]

    def step_async(self, actions_list):
        for p, a in zip(self.pipes, actions_list):
            p.send(('step', a))

    def step_wait(self):
        # Pipe recv order matches send order, and we wait for every worker
        # before reading shmem — so no race on the buffer.
        results = []
        for ei, p in enumerate(self.pipes):
            rew, done = p.recv()
            obs = self._snapshot_obs(ei)
            results.append((obs, rew, done))
        return results

    def step(self, actions_list):
        self.step_async(actions_list)
        return self.step_wait()

    def remake(self, env_kwargs):
        for p in self.pipes:
            p.send(('remake', env_kwargs))
        for p in self.pipes:
            p.recv()

    def close(self):
        for p in self.pipes:
            try:
                p.send(('close', None))
            except Exception:
                pass
        for p in self.procs:
            p.join(timeout=3)
            if p.is_alive():
                p.terminate()
        for shm in self.shms.values():
            try:
                shm.close()
                shm.unlink()
            except Exception:
                pass


# ═════════════════════════════════════════════════════════════════════════════
# OBSERVATION HELPERS
# ═════════════════════════════════════════════════════════════════════════════

OBS_KEYS = ['observation_self', 'agent_qpos_qvel', 'box_obs', 'ramp_obs',
            'lidar', 'mask_aa_obs', 'mask_ab_obs', 'mask_ar_obs']


def flatten_obs_for_agent(obs_dict, agent_idx):
    return {
        'self_obs':  obs_dict['observation_self'][agent_idx].astype(np.float32),
        'agent_obs': obs_dict['agent_qpos_qvel'][agent_idx].astype(np.float32),
        'box_obs':   obs_dict['box_obs'][agent_idx].astype(np.float32),
        'ramp_obs':  obs_dict['ramp_obs'][agent_idx].astype(np.float32),
        'mask_aa':   obs_dict['mask_aa_obs'][agent_idx].astype(np.float32),
        'mask_ab':   obs_dict['mask_ab_obs'][agent_idx].astype(np.float32),
        'mask_ar':   obs_dict['mask_ar_obs'][agent_idx].astype(np.float32),
        'lidar':     obs_dict['lidar'][agent_idx].astype(np.float32),
    }


def flatten_all_agents(obs_dict, n_agents):
    return [flatten_obs_for_agent(obs_dict, i) for i in range(n_agents)]


def obs_list_to_tensor(obs_list, device='cpu'):
    return {k: torch.tensor(np.stack([o[k] for o in obs_list]),
                            dtype=torch.float32, device=device)
            for k in obs_list[0]}


# ═════════════════════════════════════════════════════════════════════════════
# RUNNING MEAN/STD  (matches OpenAI's EMAMeanStd normalizer)
# ═════════════════════════════════════════════════════════════════════════════

class RunningMeanStd:
    """Welford's online algorithm for streaming mean/std."""
    def __init__(self, shape):
        self.mean = np.zeros(shape, dtype=np.float64)
        self.var  = np.ones(shape, dtype=np.float64)
        self.count = 1e-4

    def update(self, x):
        batch_mean = np.mean(x, axis=0)
        batch_var  = np.var(x, axis=0)
        batch_count = x.shape[0]
        self._update_from_moments(batch_mean, batch_var, batch_count)

    def _update_from_moments(self, bm, bv, bc):
        delta = bm - self.mean
        tot = self.count + bc
        new_mean = self.mean + delta * bc / tot
        m_a = self.var * self.count
        m_b = bv * bc
        m2 = m_a + m_b + delta ** 2 * self.count * bc / tot
        self.mean = new_mean
        self.var = m2 / tot
        self.count = tot

    def normalize(self, x):
        return (x - self.mean.astype(np.float32)) / (np.sqrt(self.var).astype(np.float32) + 1e-5)


# ═════════════════════════════════════════════════════════════════════════════
# POLICY NETWORK — EXACT match to OpenAI architecture
#
# OpenAI's network_spec (from pretrained npz):
#   0. circ_conv1d on lidar (filters=9, kernel=3, relu)
#   1. flatten_outer on lidar
#   2. concat main+lidar → main
#   3-5. concat main with each entity type
#   6. dense 128 relu on all 4 streams (agent, box, ramp, main)
#   7. entity_concat → objects
#   8. residual_sa_block (4 heads, 128 embd, 1 mlp)
#   9. entity_pooling (avg) → objects_pooled
#  10. concat main + objects_pooled
#  11. dense 256 relu
#  12. lstm 256
#  13. layernorm
#
# Policy net uses masks (mask_aa, mask_ab, mask_ar) for attention.
# Value net uses all-ones masks (can see everything).
# Both nets are SEPARATE (not shared).
# ═════════════════════════════════════════════════════════════════════════════

class CircConv1d(nn.Module):
    """Circular 1D convolution (wraps around edges), matches OpenAI's circ_conv1d."""
    def __init__(self, in_channels, out_channels, kernel_size):
        super().__init__()
        self.pad = kernel_size // 2
        self.conv = nn.Conv1d(in_channels, out_channels, kernel_size)

    def forward(self, x):
        # x: (B, C, L)
        x = F.pad(x, (self.pad, self.pad), mode='circular')
        return self.conv(x)


class EntityEncoder(nn.Module):
    """
    Matches OpenAI's entity encoder exactly:
      - Per-type dense embedding (concat self_obs to each entity first)
      - Entity concat with masks
      - Residual self-attention block
      - Average pooling
    """
    def __init__(self, d_embed=128, sa_heads=4, sa_embd=128, lidar_filters=9,
                 lidar_kernel=3, self_dim=10, agent_feat=10, box_feat=12,
                 ramp_feat=9, lidar_bins=30):
        super().__init__()
        # Lidar: circ_conv1d → flatten → produces lidar_filters * lidar_bins features
        # But OpenAI does conv on (B, 1, 30) → (B, 9, 30) → flatten → (B, 270)
        self.lidar_conv = CircConv1d(1, lidar_filters, lidar_kernel)
        lidar_flat = lidar_filters * lidar_bins  # 270

        # After concat with self_obs, each entity gets:
        # main: self_dim + lidar_flat = 10 + 270 = 280
        # agent: self_dim + lidar_flat + agent_feat = 10 + 270 + 10 = 290
        # box:   self_dim + lidar_flat + box_feat   = 10 + 270 + 12 = 292
        # ramp:  self_dim + lidar_flat + ramp_feat   = 10 + 270 + 9  = 289
        # Wait — from the weights: main input=280, agent=290, box=292, ramp=289
        # main = self(10) + lidar(270) = 280 ✓
        # agent = main(10+270=280) concat agent(10) = 290 ✓  — NO
        # Actually the concat prepends self_obs to each entity:
        # agent = self(10) + agent(10) per entity → but that's only 20 per entity...
        # Let me re-read: concat main+agent_qpos_qvel means concat(main, agent) along last dim
        # main is (B, 280), agent is (B, n_agents, 10)
        # concat broadcasts main along entity dim: (B, n_agents, 280+10=290) ✓
        self.main_dense  = nn.Linear(self_dim + lidar_flat, d_embed)  # 280→128
        self.agent_dense = nn.Linear(self_dim + lidar_flat + agent_feat, d_embed)  # 290→128
        self.box_dense   = nn.Linear(self_dim + lidar_flat + box_feat, d_embed)    # 292→128
        self.ramp_dense  = nn.Linear(self_dim + lidar_flat + ramp_feat, d_embed)   # 289→128

        # Self-attention: residual_sa_block
        # QKV embed + attention + post-SA MLP
        self.qk_proj = nn.Linear(sa_embd, sa_embd * 2)
        self.v_proj  = nn.Linear(sa_embd, sa_embd)
        self.sa_post = nn.Linear(sa_embd, sa_embd)
        self.sa_mlp  = nn.Linear(sa_embd, sa_embd)
        self.sa_heads = sa_heads
        self.sa_embd  = sa_embd

    def _self_attention(self, ent, mask):
        """Residual self-attention block matching OpenAI's."""
        B, NE, D = ent.shape
        H = self.sa_heads
        Dh = D // H

        # QKV
        qk = self.qk_proj(ent).view(B, NE, H, Dh, 2)
        q, k = qk[..., 0], qk[..., 1]  # (B, NE, H, Dh)
        v = self.v_proj(ent).view(B, NE, H, Dh)

        # (B, H, NE, Dh)
        q = q.permute(0, 2, 1, 3)
        k = k.permute(0, 2, 3, 1)  # (B, H, Dh, NE)
        v = v.permute(0, 2, 1, 3)

        logits = torch.matmul(q, k) / (Dh ** 0.5)  # (B, H, NE, NE)

        if mask is not None:
            # mask: (B, NE), expand to (B, 1, 1, NE)
            m = mask.unsqueeze(1).unsqueeze(2)
            logits = logits + (1.0 - m) * (-1e9)

        attn = F.softmax(logits, dim=-1)
        out = torch.matmul(attn, v)  # (B, H, NE, Dh)
        out = out.permute(0, 2, 1, 3).reshape(B, NE, D)

        # Post-SA linear + residual
        out = ent + self.sa_post(out)

        # MLP + residual
        out = out + self.sa_mlp(F.relu(out))

        return out

    def forward(self, obs, use_masks=True):
        B = obs['self_obs'].shape[0]

        # Lidar: (B, 30, 1) → (B, 1, 30) → conv → (B, 9, 30) → flatten → (B, 270)
        lidar = obs['lidar']  # (B, 30, 1)
        lidar = lidar.permute(0, 2, 1)  # (B, 1, 30)
        lidar = F.relu(self.lidar_conv(lidar))  # (B, 9, 30)
        lidar_flat = lidar.reshape(B, -1)  # (B, 270)

        # Main = self_obs + lidar_flat
        main = torch.cat([obs['self_obs'], lidar_flat], -1)  # (B, 280)

        # Per-entity: broadcast main along entity dim, concat
        n_a = obs['agent_obs'].shape[1]
        n_b = obs['box_obs'].shape[1]
        n_r = obs['ramp_obs'].shape[1]
        main_exp = main.unsqueeze(1)

        agent_in = torch.cat([main_exp.expand(-1, n_a, -1), obs['agent_obs']], -1)
        box_in   = torch.cat([main_exp.expand(-1, n_b, -1), obs['box_obs']], -1)
        ramp_in  = torch.cat([main_exp.expand(-1, n_r, -1), obs['ramp_obs']], -1)

        # Dense 128 relu on each stream
        main_e  = F.relu(self.main_dense(main)).unsqueeze(1)    # (B, 1, 128)
        agent_e = F.relu(self.agent_dense(agent_in))             # (B, n_a, 128)
        box_e   = F.relu(self.box_dense(box_in))                 # (B, n_b, 128)
        ramp_e  = F.relu(self.ramp_dense(ramp_in))               # (B, n_r, 128)

        # Entity concat: [agent, box, ramp, main]
        entities = torch.cat([agent_e, box_e, ramp_e, main_e], 1)  # (B, n_a+n_b+n_r+1, 128)

        # Build mask
        if use_masks:
            mask = torch.cat([
                obs['mask_aa'], obs['mask_ab'], obs['mask_ar'],
                torch.ones(B, 1, device=main.device)
            ], 1)  # (B, n_a+n_b+n_r+1)
        else:
            NE = entities.shape[1]
            mask = torch.ones(B, NE, device=main.device)

        # Residual self-attention
        entities = self._self_attention(entities, mask)

        # Average pooling (masked)
        m = mask.unsqueeze(-1)  # (B, NE, 1)
        pooled = (entities * m).sum(1) / (m.sum(1) + 1e-5)  # (B, 128)

        # Concat main + pooled → (B, 256)
        return torch.cat([main_e.squeeze(1), pooled], -1)


class OpenAIPolicy(nn.Module):
    """
    EXACT match to OpenAI's policy architecture:
      - Separate policy_net and vpred_net (NOT shared)
      - Each: EntityEncoder → Dense 256 → LSTM 256 → LayerNorm
      - Policy net uses observation masks, value net sees everything
    """
    def __init__(self, cfg):
        super().__init__()

        # Policy network
        self.pi_encoder = EntityEncoder(
            d_embed=cfg.d_embed, sa_heads=cfg.sa_heads, sa_embd=cfg.sa_embd,
            lidar_filters=cfg.lidar_filters, lidar_kernel=cfg.lidar_kernel,
            ramp_feat=cfg.ramp_feat)
        self.pi_dense = nn.Linear(cfg.d_embed * 2, cfg.dense_hidden)  # 256→256
        self.pi_lstm  = nn.LSTMCell(cfg.dense_hidden, cfg.lstm_hidden)
        self.pi_ln    = nn.LayerNorm(cfg.lstm_hidden)

        # Value network (separate)
        self.vf_encoder = EntityEncoder(
            d_embed=cfg.d_embed, sa_heads=cfg.sa_heads, sa_embd=cfg.sa_embd,
            lidar_filters=cfg.lidar_filters, lidar_kernel=cfg.lidar_kernel,
            ramp_feat=cfg.ramp_feat)
        self.vf_dense = nn.Linear(cfg.d_embed * 2, cfg.dense_hidden)
        self.vf_lstm  = nn.LSTMCell(cfg.dense_hidden, cfg.lstm_hidden)
        self.vf_ln    = nn.LayerNorm(cfg.lstm_hidden)

        # Action heads (from policy net)
        self.move_head = nn.Linear(cfg.lstm_hidden, ACT_MOVE_DIM * ACT_MOVE_BINS)  # 256→33
        self.pull_head = nn.Linear(cfg.lstm_hidden, ACT_PULL_DIM)                   # 256→2
        self.glue_head = nn.Linear(cfg.lstm_hidden, ACT_GLUE_DIM)                   # 256→2

        # Value head (from vpred net)
        self.v_head = nn.Linear(cfg.lstm_hidden, 1)  # 256→1

        self.lstm_hidden = cfg.lstm_hidden
        self._init_weights()

    def _init_weights(self):
        for n, p in self.named_parameters():
            if 'weight' in n and p.dim() >= 2:
                if 'head' in n:
                    nn.init.orthogonal_(p, gain=0.01)
                else:
                    nn.init.xavier_uniform_(p)
            elif 'bias' in n:
                nn.init.zeros_(p)

    def forward(self, obs, pi_hx=None, pi_cx=None, vf_hx=None, vf_cx=None):
        # Policy stream (uses observation masks)
        pi_enc = self.pi_encoder(obs, use_masks=True)        # (B, 256)
        pi_h = F.relu(self.pi_dense(pi_enc))                  # (B, 256)
        pi_hx, pi_cx = self.pi_lstm(pi_h, (pi_hx, pi_cx))    # (B, 256)
        pi_out = self.pi_ln(pi_hx)                             # (B, 256)

        # Value stream (sees everything — no masks)
        vf_enc = self.vf_encoder(obs, use_masks=False)        # (B, 256)
        vf_h = F.relu(self.vf_dense(vf_enc))                  # (B, 256)
        vf_hx, vf_cx = self.vf_lstm(vf_h, (vf_hx, vf_cx))    # (B, 256)
        vf_out = self.vf_ln(vf_hx)                             # (B, 256)

        # Action distributions
        ml = self.move_head(pi_out).view(-1, ACT_MOVE_DIM, ACT_MOVE_BINS)
        move_d = [Categorical(logits=ml[:, i]) for i in range(ACT_MOVE_DIM)]
        pull_d = Categorical(logits=self.pull_head(pi_out))
        glue_d = Categorical(logits=self.glue_head(pi_out))

        # Value
        value = self.v_head(vf_out).squeeze(-1)

        return move_d, pull_d, glue_d, value, pi_hx, pi_cx, vf_hx, vf_cx

    @torch.no_grad()
    def act(self, obs, pi_hx=None, pi_cx=None, vf_hx=None, vf_cx=None,
            deterministic=False):
        move_d, pull_d, glue_d, value, pi_hx, pi_cx, vf_hx, vf_cx = \
            self.forward(obs, pi_hx, pi_cx, vf_hx, vf_cx)
        if deterministic:
            m = [d.probs.argmax(-1) for d in move_d]
            p = pull_d.probs.argmax(-1)
            g = glue_d.probs.argmax(-1)
        else:
            m = [d.sample() for d in move_d]
            p = pull_d.sample()
            g = glue_d.sample()
        logp = (sum(d.log_prob(a) for d, a in zip(move_d, m))
                + pull_d.log_prob(p) + glue_d.log_prob(g))
        return (torch.stack(m, -1), p, g, logp, value,
                pi_hx, pi_cx, vf_hx, vf_cx)

    def evaluate(self, obs, move_a, pull_a, glue_a,
                 pi_hx=None, pi_cx=None, vf_hx=None, vf_cx=None):
        move_d, pull_d, glue_d, value, pi_hx, pi_cx, vf_hx, vf_cx = \
            self.forward(obs, pi_hx, pi_cx, vf_hx, vf_cx)
        logp = (sum(move_d[i].log_prob(move_a[:, i])
                    for i in range(ACT_MOVE_DIM))
                + pull_d.log_prob(pull_a) + glue_d.log_prob(glue_a))
        ent = (sum(d.entropy() for d in move_d)
               + pull_d.entropy() + glue_d.entropy())
        return logp, value, ent, pi_hx, pi_cx, vf_hx, vf_cx

    def init_hidden(self, B, device='cpu'):
        z = torch.zeros(B, self.lstm_hidden, device=device)
        return z.clone(), z.clone(), z.clone(), z.clone()

    def param_count(self):
        return sum(p.numel() for p in self.parameters())


# Alias for render_ada.py compatibility
AdAPolicy = OpenAIPolicy


# ═════════════════════════════════════════════════════════════════════════════
# OPPONENT POOL  (AdA Innovation 1)
# ═════════════════════════════════════════════════════════════════════════════

class OpponentPool:
    def __init__(self, max_size=10):
        self.pool = deque(maxlen=max_size)

    def add(self, state_dict):
        self.pool.append(
            {k: v.clone().cpu() for k, v in state_dict.items()})

    def sample(self):
        if self.pool:
            return self.pool[np.random.randint(len(self.pool))]
        return None

    def size(self):
        return len(self.pool)


# ═════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═════════════════════════════════════════════════════════════════════════════

def actions_to_env(move_t, pull_t, glue_t, n_agents):
    return normalize_action_dict({
        'action_movement': tuple(move_t[a].cpu().numpy() for a in range(n_agents)),
        'action_pull':     tuple(int(pull_t[a].item()) for a in range(n_agents)),
        'action_glueall':  tuple(int(glue_t[a].item()) for a in range(n_agents)),
    })


def actions_to_env_np(move_np, pull_np, glue_np, n_agents):
    """Same as actions_to_env, but accepts numpy slices — avoids per-agent
    GPU→CPU syncs inside the rollout hot loop."""
    return normalize_action_dict({
        'action_movement': tuple(move_np[a] for a in range(n_agents)),
        'action_pull':     tuple(int(pull_np[a]) for a in range(n_agents)),
        'action_glueall':  tuple(int(glue_np[a]) for a in range(n_agents)),
    })


def compute_gae(rewards, values, dones, gamma, lam):
    T = len(rewards)
    adv = np.zeros(T, dtype=np.float32)
    gae = 0.0
    for t in reversed(range(T)):
        nv = values[t + 1] if t + 1 < T else 0.0
        nt = 1.0 - float(dones[t])
        delta = rewards[t] + gamma * nv * nt - values[t]
        gae = delta + gamma * lam * nt * gae
        adv[t] = gae
    return adv + np.array(values[:T], dtype=np.float32), adv


# ═════════════════════════════════════════════════════════════════════════════
# PLOTTING  (background thread)
# ═════════════════════════════════════════════════════════════════════════════

def save_plot(history, path):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        ep = history['episodes']
        if len(ep) < 2:
            return
        fig, axes = plt.subplots(3, 1, figsize=(14, 13), dpi=100)

        w = min(500, len(ep) // 2) if len(ep) > 10 else 1   # Run 2: 100→500 for smoother long-run curves
        hr = history['hider_rewards']
        sr = history['seeker_rewards']

        ax = axes[0]
        ax.plot(ep, hr, color='blue', alpha=0.15, lw=0.5)
        ax.plot(ep, sr, color='red',  alpha=0.15, lw=0.5)
        if w > 1:
            ax.plot(ep[w-1:], np.convolve(hr, np.ones(w)/w, 'valid'),
                    color='blue', lw=2, label='Hiders (MA)')
            ax.plot(ep[w-1:], np.convolve(sr, np.ones(w)/w, 'valid'),
                    color='red', lw=2, label='Seekers (MA)')
        ax.axhline(0, color='gray', ls='-', alpha=0.3)
        ax.set_ylabel('Avg Reward')
        ax.set_title('Hide & Seek — OpenAI Arch + AdA (Opponent Pool + Curriculum)')
        if w > 1:
            ax.legend()
        ax.grid(True, alpha=0.3); ax.set_ylim(-55, 55)

        ax2 = axes[1]
        if 'hider_winrate' in history and history['hider_winrate']:
            wr = history['hider_winrate']
            ax2.plot(ep, wr, color='green', alpha=0.2, lw=0.5)
            if w > 1 and len(wr) >= w:
                ax2.plot(ep[w-1:],
                         np.convolve(wr, np.ones(w)/w, 'valid'),
                         color='green', lw=2, label='Hider WR (MA)')
                ax2.legend()
            ax2.axhline(0.5, color='gray', ls='--', alpha=0.4)
            ax2.set_ylim(0, 1)
        ax2.set_ylabel('Win Rate'); ax2.set_title('Hider Win Rate')
        ax2.grid(True, alpha=0.3)

        ax3 = axes[2]
        if history.get('curriculum_phase'):
            ax3.plot(ep, history['curriculum_phase'],
                     color='orange', lw=2, label='Phase')
        if history.get('pool_size'):
            ax3b = ax3.twinx()
            ax3b.plot(ep, history['pool_size'],
                      color='purple', lw=2, label='Pool')
            ax3b.set_ylabel('Pool Size', color='purple')
        ax3.set_xlabel('Episode'); ax3.set_ylabel('Phase', color='orange')
        ax3.set_title('Curriculum & Opponent Pool')
        ax3.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(path, bbox_inches='tight')
        plt.close(fig)
    except Exception:
        pass


# ═════════════════════════════════════════════════════════════════════════════
# CHECKPOINT I/O
# ═════════════════════════════════════════════════════════════════════════════

def save_npz(policy, optimizer, episode, history, normalizers, path,
             opponent_pool=None, task_sampler=None):
    np.savez_compressed(path,
        policy_state_dict=pickle.dumps(
            {k: v.cpu().numpy() for k, v in policy.state_dict().items()}),
        optimizer_state=pickle.dumps(optimizer.state_dict()),
        episode=np.array(episode),
        config=pickle.dumps(vars(cfg)),
        history=pickle.dumps(history),
        normalizers=pickle.dumps(normalizers),
        architecture=np.array('openai_lstm_ada'),
        opponent_pool=pickle.dumps(
            list(opponent_pool.pool) if opponent_pool else []),
        task_sampler=pickle.dumps(
            task_sampler.get_state() if task_sampler else None),
    )


def load_npz(path, policy, optimizer=None, opponent_pool=None, task_sampler=None):
    d = np.load(path, allow_pickle=True)
    sd = pickle.loads(d['policy_state_dict'].item())
    policy.load_state_dict({k: torch.tensor(v) for k, v in sd.items()})
    if optimizer and 'optimizer_state' in d:
        try:
            optimizer.load_state_dict(
                pickle.loads(d['optimizer_state'].item()))
        except Exception:
            pass
    ep = int(d['episode'])
    hist = pickle.loads(d['history'].item()) if 'history' in d else None
    norms = pickle.loads(d['normalizers'].item()) if 'normalizers' in d else None
    # Restore opponent pool if saved
    if opponent_pool is not None and 'opponent_pool' in d:
        try:
            saved_pool = pickle.loads(d['opponent_pool'].item())
            for entry in saved_pool:
                opponent_pool.pool.append(entry)
        except Exception:
            pass
    # Restore PLR sampler state if present (older checkpoints omit this key).
    if task_sampler is not None and 'task_sampler' in d:
        try:
            st = pickle.loads(d['task_sampler'].item())
            if st is not None:
                task_sampler.set_state(st)
        except Exception:
            pass
    return ep, hist, norms


load_checkpoint_npz = load_npz


# ═════════════════════════════════════════════════════════════════════════════
# PPO UPDATE
# ═════════════════════════════════════════════════════════════════════════════

def ppo_update(policy, optimizer, trajectories):
    """PPO update with sequential LSTM processing (truncated BPTT, chunk=10).

    Each trajectory is a dict with keys:
        obs:  {key: (T, ...)}   move: (T, 3)   pull: (T,)   glue: (T,)
        logp: (T,)              ret:  (T,)      adv:  (T,)
    Trajectories are processed sequentially through the LSTM so it can
    learn to use memory across timesteps within an episode.
    """
    if not trajectories:
        return {}

    n_traj = len(trajectories)
    T = trajectories[0]['ret'].shape[0]
    CHUNK = 10  # truncated BPTT window

    # Stack all trajectories → (n_traj, T, ...)
    # Trajectories are collected on CPU now (for IPC efficiency); move the
    # whole batch to the training device once up front.
    all_obs = {}
    for k in trajectories[0]['obs']:
        all_obs[k] = torch.stack([tr['obs'][k] for tr in trajectories]).to(cfg.device)
    all_move     = torch.stack([tr['move'] for tr in trajectories]).to(cfg.device)
    all_pull     = torch.stack([tr['pull'] for tr in trajectories]).to(cfg.device)
    all_glue     = torch.stack([tr['glue'] for tr in trajectories]).to(cfg.device)
    all_logp_old = torch.stack([tr['logp'] for tr in trajectories]).to(cfg.device)
    all_ret      = torch.stack([tr['ret']  for tr in trajectories]).to(cfg.device)
    all_adv      = torch.stack([tr['adv']  for tr in trajectories]).to(cfg.device)

    if cfg.normalize_advantages:
        all_adv = (all_adv - all_adv.mean()) / (all_adv.std() + 1e-8)

    pg_sum = vf_sum = ent_sum = 0.0
    cnt = 0

    for _ in range(cfg.ppo_epochs):
        # Shuffle trajectory order (but keep timesteps sequential)
        perm = np.random.permutation(n_traj)
        b_obs    = {k: all_obs[k][perm] for k in all_obs}
        b_move   = all_move[perm]
        b_pull   = all_pull[perm]
        b_glue   = all_glue[perm]
        b_logp   = all_logp_old[perm]
        b_ret    = all_ret[perm]
        b_adv    = all_adv[perm]

        # Fresh LSTM state at episode start
        pi_hx, pi_cx, vf_hx, vf_cx = policy.init_hidden(n_traj, cfg.device)

        optimizer.zero_grad()
        epoch_pg = epoch_vf = epoch_ent = 0.0

        for t0 in range(0, T, CHUNK):
            t1 = min(t0 + CHUNK, T)
            chunk_logp, chunk_val, chunk_ent = [], [], []

            for t in range(t0, t1):
                obs_t = {k: b_obs[k][:, t] for k in b_obs}
                logp_t, val_t, ent_t, pi_hx, pi_cx, vf_hx, vf_cx = \
                    policy.evaluate(obs_t, b_move[:, t], b_pull[:, t],
                                    b_glue[:, t],
                                    pi_hx, pi_cx, vf_hx, vf_cx)
                chunk_logp.append(logp_t)
                chunk_val.append(val_t)
                chunk_ent.append(ent_t)

            # Detach hidden state at chunk boundary (truncated BPTT)
            pi_hx = pi_hx.detach()
            pi_cx = pi_cx.detach()
            vf_hx = vf_hx.detach()
            vf_cx = vf_cx.detach()

            logp_c = torch.stack(chunk_logp, 1)   # (B, chunk_len)
            val_c  = torch.stack(chunk_val, 1)
            ent_c  = torch.stack(chunk_ent, 1)

            ratio = torch.exp(logp_c - b_logp[:, t0:t1])
            adv_c = b_adv[:, t0:t1]
            pg = -torch.min(
                ratio * adv_c,
                torch.clamp(ratio, 1 - cfg.clip_range,
                            1 + cfg.clip_range) * adv_c).mean()
            vf = F.mse_loss(val_c, b_ret[:, t0:t1])
            ent_loss = -ent_c.mean()

            chunk_loss = pg + cfg.vf_coef * vf + cfg.entropy_coef * ent_loss
            # Scale gradient by chunk fraction so total gradient is correct
            (chunk_loss * (t1 - t0) / T).backward()

            epoch_pg  += pg.item() * (t1 - t0)
            epoch_vf  += vf.item() * (t1 - t0)
            epoch_ent += ent_c.mean().item() * (t1 - t0)

        nn.utils.clip_grad_norm_(policy.parameters(), cfg.max_grad_norm)
        optimizer.step()

        pg_sum  += epoch_pg / T
        vf_sum  += epoch_vf / T
        ent_sum += epoch_ent / T
        cnt += 1

    n = max(cnt, 1)
    return {'pg': pg_sum / n, 'vf': vf_sum / n, 'ent': ent_sum / n}


# ═════════════════════════════════════════════════════════════════════════════
# VECTORISED ROLLOUT
# ═════════════════════════════════════════════════════════════════════════════

@torch.no_grad()
def collect_vectorized(vec_env, policy, cfg, dev, normalizers,
                       use_opp=False, opp_policy=None):
    N_ENVS = vec_env.n
    NA = cfg.n_agents
    TOTAL = N_ENVS * NA

    obs_list = vec_env.reset_all()

    pi_hx, pi_cx, vf_hx, vf_cx = policy.init_hidden(TOTAL, dev)
    if use_opp and opp_policy is not None:
        o_pi_hx, o_pi_cx, o_vf_hx, o_vf_cx = opp_policy.init_hidden(TOTAL, dev)

    ag_obs  = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_move = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_pull = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_glue = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_logp = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_val  = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_rew  = [[[] for _ in range(NA)] for _ in range(N_ENVS)]
    ag_done = [[[] for _ in range(NA)] for _ in range(N_ENVS)]

    ep_rewards = np.zeros((N_ENVS, NA))
    env_done = [False] * N_ENVS

    for step in range(cfg.horizon):
        # Flatten obs
        all_agent_obs = []
        for ei in range(N_ENVS):
            all_agent_obs.extend(flatten_all_agents(obs_list[ei], NA))

        # Normalize observations
        # raw_obs is built on CPU so we can call .numpy() on it below to feed
        # the RunningMeanStd normalizer; normalized tensor is then moved to dev.
        raw_obs = obs_list_to_tensor(all_agent_obs, 'cpu')
        norm_obs = {}
        for k in raw_obs:
            if k in normalizers:
                v = raw_obs[k].numpy()
                normalizers[k].update(v.reshape(-1, *v.shape[1:]) if v.ndim > 2
                                       else v)
                norm_obs[k] = torch.tensor(normalizers[k].normalize(v),
                                           dtype=torch.float32, device=dev)
            else:
                norm_obs[k] = raw_obs[k].to(dev)

        # Policy forward
        move_a, pull_a, glue_a, logp, val, pi_hx, pi_cx, vf_hx, vf_cx = \
            policy.act(norm_obs, pi_hx, pi_cx, vf_hx, vf_cx)

        # Opponent override
        if use_opp and opp_policy is not None:
            om, op, og, _, _, o_pi_hx, o_pi_cx, o_vf_hx, o_vf_cx = \
                opp_policy.act(norm_obs, o_pi_hx, o_pi_cx, o_vf_hx, o_vf_cx)
            for ei in range(N_ENVS):
                base = ei * NA
                for si in range(cfg.n_hiders, NA):
                    idx = base + si
                    move_a[idx] = om[idx]
                    pull_a[idx] = op[idx]
                    glue_a[idx] = og[idx]

        # ── Batched GPU→CPU transfers (once per step, not per agent) ─────
        # This is the key optimization: avoids ~2000 GPU syncs per step that
        # the original per-agent .item()/.cpu() calls were causing.
        move_a_cpu = move_a.detach().cpu()              # (TOTAL, ACT_MOVE_DIM)
        pull_a_cpu = pull_a.detach().cpu()              # (TOTAL,)
        glue_a_cpu = glue_a.detach().cpu()              # (TOTAL,)
        logp_np    = logp.detach().cpu().numpy()        # (TOTAL,)
        val_np     = val.detach().cpu().numpy()         # (TOTAL,)
        move_a_np  = move_a_cpu.numpy()
        pull_a_np  = pull_a_cpu.numpy()
        glue_a_np  = glue_a_cpu.numpy()
        # Fresh per-step CPU copy of normalized obs — next step overwrites
        # `norm_obs` on the GPU, so we need our own CPU snapshot to keep
        # references alive for the trajectory buffer. Slicing views into
        # these tensors is safe (nothing mutates them afterwards).
        step_obs_cpu = {k: norm_obs[k].detach().cpu() for k in norm_obs}

        # Build actions & dispatch  (numpy, no GPU syncs)
        action_dicts = []
        for ei in range(N_ENVS):
            base = ei * NA
            action_dicts.append(actions_to_env_np(
                move_a_np[base:base + NA], pull_a_np[base:base + NA],
                glue_a_np[base:base + NA], NA))
        vec_env.step_async(action_dicts)
        results = vec_env.step_wait()

        for ei, (new_obs, rewards, done) in enumerate(results):
            if env_done[ei]:
                continue
            base = ei * NA
            for a in range(NA):
                is_opp = use_opp and a >= cfg.n_hiders
                r = float(rewards[a]) if hasattr(rewards, '__len__') \
                    else float(rewards)
                ep_rewards[ei, a] += r
                if not is_opp:
                    # Store CPU views — no .clone(), no .item(), no GPU syncs
                    ag_obs[ei][a].append({k: step_obs_cpu[k][base + a]
                                          for k in step_obs_cpu})
                    ag_move[ei][a].append(move_a_cpu[base + a])
                    ag_pull[ei][a].append(pull_a_cpu[base + a])
                    ag_glue[ei][a].append(glue_a_cpu[base + a])
                    ag_logp[ei][a].append(float(logp_np[base + a]))
                    ag_val[ei][a].append(float(val_np[base + a]))
                    ag_rew[ei][a].append(r)
                    ag_done[ei][a].append(done)
            obs_list[ei] = new_obs
            if done:
                env_done[ei] = True

    # GAE + build trajectories (keep timesteps sequential per trajectory)
    trajectories = []

    for ei in range(N_ENVS):
        for a in range(NA):
            is_opp = use_opp and a >= cfg.n_hiders
            if is_opp or len(ag_rew[ei][a]) == 0:
                continue
            ret, adv = compute_gae(ag_rew[ei][a], ag_val[ei][a],
                                   ag_done[ei][a], cfg.gamma, cfg.gae_lambda)
            T = len(ag_rew[ei][a])
            traj_obs = {}
            for k in ag_obs[ei][a][0]:
                traj_obs[k] = torch.stack(
                    [ag_obs[ei][a][t][k] for t in range(T)])
            trajectories.append({
                'obs':  traj_obs,
                'move': torch.stack(ag_move[ei][a]),
                'pull': torch.stack(ag_pull[ei][a]),
                'glue': torch.stack(ag_glue[ei][a]),
                'logp': torch.tensor(ag_logp[ei][a], dtype=torch.float32),
                'ret':  torch.tensor(ret, dtype=torch.float32),
                'adv':  torch.tensor(adv, dtype=torch.float32),
            })

    h_rews = [np.mean(ep_rewards[ei, :cfg.n_hiders]) for ei in range(N_ENVS)]
    s_rews = [np.mean(ep_rewards[ei, cfg.n_hiders:]) for ei in range(N_ENVS)]
    h_wins = [1.0 if ep_rewards[ei, 0] > 0 else 0.0 for ei in range(N_ENVS)]

    return trajectories, h_rews, s_rews, h_wins


# ═════════════════════════════════════════════════════════════════════════════
# MAIN TRAINING LOOP
# ═════════════════════════════════════════════════════════════════════════════

def train():
    dev = cfg.device
    set_global_seed(cfg.seed)
    print("═" * 72)
    print("  Hide & Seek — OpenAI Architecture + AdA Innovations (Headless)")
    print("═" * 72)
    print(f"  Target:         {cfg.total_episodes:,} episodes")
    print(f"  Worker envs:    {cfg.n_envs}"
          f"  ({cfg.n_envs * cfg.n_agents} agents/fwd pass)")
    print(f"  Horizon:        {cfg.horizon}"
          f" ({int(cfg.horizon * cfg.prep_fraction)} prep"
          f" + {int(cfg.horizon * (1 - cfg.prep_fraction))} play)")
    print(f"  PPO:            lr={cfg.lr}  γ={cfg.gamma}"
          f"  λ={cfg.gae_lambda}  ε={cfg.clip_range}"
          f"  epochs={cfg.ppo_epochs}  mb={cfg.n_minibatches}")
    print(f"  Architecture:   EntityEncoder → Dense {cfg.dense_hidden}"
          f" → LSTM {cfg.lstm_hidden} → LayerNorm  (×2 separate nets)")
    print(f"  Self-attention: {cfg.sa_heads} heads, {cfg.sa_embd} embd")
    print(f"  Opponent pool:  size={cfg.opponent_pool_size}"
          f"  p={cfg.opponent_sample_prob}"
          f"  start={cfg.opponent_pool_start:,}")
    print(f"  Task sampler:   PLR over {len(TASK_SPACE)} p_door configs"
          f"  warmup={cfg.task_warmup_episodes:,}  hold={cfg.task_hold_batches} batches")
    print(f"  Ramp lock:      {cfg.lock_ramp}  (ramp_feat={cfg.ramp_feat})"
          f"   entropy={cfg.entropy_coef}")
    print(f"  Seed:           {cfg.seed}  (numpy/torch/random + env base seed)")
    print(f"  Checkpoints:    milestone every {cfg.checkpoint_freq:,} eps (keep ALL)"
          f"   resume_latest every {cfg.resume_freq:,}")

    policy = OpenAIPolicy(cfg).to(dev)
    print(f"  Parameters:     {policy.param_count():,}")
    print("═" * 72)

    optimizer = optim.Adam(policy.parameters(), lr=cfg.lr, eps=1e-5)
    total_updates = cfg.total_episodes // cfg.n_envs
    # Linear decay: lr → 0 over training (exact OpenAI schedule)
    scheduler = optim.lr_scheduler.LinearLR(
        optimizer,
        start_factor=1.0,
        end_factor=0.0,
        total_iters=total_updates)

    opponent_pool = OpponentPool(cfg.opponent_pool_size)
    opp_policy = None

    # ── Adaptive task sampler (PLR) — replaces hand-scheduled curriculum ───
    # Created before resume so its state can be restored in-place from a checkpoint.
    task_sampler = PrioritizedTaskSampler(
        n_tasks=len(TASK_SPACE),
        warmup_episodes=cfg.task_warmup_episodes,
        easy_idx=cfg.task_easy_idx,
        staleness_coef=cfg.task_staleness_coef,
        beta=cfg.task_beta,
        ema_decay=cfg.task_ema_decay,
        floor_prob=cfg.task_floor_prob)

    # Observation normalizers (matches OpenAI's normalize=True)
    normalizers = {
        'self_obs':  RunningMeanStd((10,)),
        'agent_obs': RunningMeanStd((10,)),
        'box_obs':   RunningMeanStd((12,)),
        'ramp_obs':  RunningMeanStd((cfg.ramp_feat,)),
        'lidar':     RunningMeanStd((1,)),
    }

    # ── Resume ────────────────────────────────────────────────────────────
    start_ep = 0
    history = {'episodes': [], 'hider_rewards': [], 'seeker_rewards': [],
               'hider_winrate': [], 'curriculum_phase': [], 'pool_size': []}

    existing = sorted(
        [f for f in os.listdir(cfg.checkpoint_dir)
         if f.startswith('checkpoint_') and f.endswith('.npz')]
    ) if os.path.isdir(cfg.checkpoint_dir) else []
    # Resume candidates: newest 1M milestone + the rolling resume file.  After a
    # hard crash the rolling file may be ahead of the last milestone, so pick
    # whichever has the higher stored episode count.
    candidates = []
    if existing:
        candidates.append(os.path.join(cfg.checkpoint_dir, existing[-1]))
    _rpath = os.path.join(cfg.checkpoint_dir, 'resume_latest.npz')
    if os.path.exists(_rpath):
        candidates.append(_rpath)
    def _ckpt_ep(p):
        try:
            return int(np.load(p, allow_pickle=True)['episode'])
        except Exception:
            return -1
    if candidates:
        latest = max(candidates, key=_ckpt_ep)
        print(f"\n  ► Resuming from {latest}")
        start_ep, h, norms = load_npz(latest, policy, optimizer,
                                       opponent_pool=opponent_pool,
                                       task_sampler=task_sampler)
        if h:
            history = h
            if 'hider_winrate' not in history:
                history['hider_winrate'] = []
        if norms:
            normalizers = norms
        # Advance LR scheduler to the correct step
        steps_done = start_ep // cfg.n_envs
        for _ in range(steps_done):
            scheduler.step()
        print(f"    episode {start_ep:,}  |  pool restored: {opponent_pool.size()} snapshots"
              f"  |  LR scheduler advanced {steps_done:,} steps\n")

    # ── Launch subprocess environments (start on the spine config) ─────────
    cur_phase = cfg.task_easy_idx          # current task index (kept name for history/plots)
    cur_kw    = TASK_SPACE[cur_phase]
    env_kwargs = dict(BASE_ENV_KWARGS)
    env_kwargs.update(cur_kw)
    vec_env = ShmemVecEnv(cfg.n_envs, env_kwargs, seed=cfg.seed)
    print(f"  Launched {cfg.n_envs} subprocess workers (shmem transport)")

    ep_count  = start_ep
    t_start   = time.time()
    recent_h  = deque(maxlen=500)
    recent_s  = deque(maxlen=500)
    recent_wr = deque(maxlen=500)
    last_ckpt = start_ep
    last_plot = start_ep
    last_resume = start_ep
    early_exported = (start_ep > 0)
    batches_since_resample = 0

    shutdown = False
    def _sig(s, f):
        nonlocal shutdown; shutdown = True
        # Emergency save on first signal
        if ep_count > start_ep:
            epath = os.path.join(cfg.checkpoint_dir,
                                 f'checkpoint_{ep_count:08d}.npz')
            try:
                save_npz(policy, optimizer, ep_count, history, normalizers,
                         epath, opponent_pool=opponent_pool,
                         task_sampler=task_sampler)
                print(f"\n  ⚠ Emergency save: {epath}")
            except Exception:
                pass
    signal.signal(signal.SIGINT, _sig)
    signal.signal(signal.SIGTERM, _sig)

    # Background thread: delete tmp*.xml files leaked by mujoco_py every 10 min
    def _xml_cleanup_loop():
        import glob, tempfile
        while not shutdown:
            time.sleep(600)
            for f in glob.glob(os.path.join(tempfile.gettempdir(), 'tmp*.xml')):
                try:
                    os.remove(f)
                except OSError:
                    pass
    _cleanup_thread = threading.Thread(target=_xml_cleanup_loop, daemon=True)
    _cleanup_thread.start()

    print(f"\n  Training started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        while ep_count < cfg.total_episodes and not shutdown:

            # ── Adaptive task sampling (PLR — replaces hand-scheduled curriculum) ──
            # Hold each task for task_hold_batches batches so env remake() cost
            # is amortised, then resample by learnability + staleness.
            if batches_since_resample >= cfg.task_hold_batches:
                new_task = task_sampler.sample(ep_count)
                batches_since_resample = 0
                if new_task != cur_phase:
                    cur_phase = new_task
                    cur_kw = TASK_SPACE[cur_phase]
                    env_kwargs = dict(BASE_ENV_KWARGS)
                    env_kwargs.update(cur_kw)
                    vec_env.remake(env_kwargs)
                    print(f"\n  ▸ Task → #{cur_phase}  "
                          f"p_door_dropout={cur_kw['p_door_dropout']:.2f}  "
                          f"at ep {ep_count:,}")
            batches_since_resample += 1

            # ── Opponent pool (AdA Innovation 1) ──────────────────────────
            use_opp = (ep_count >= cfg.opponent_pool_start
                       and opponent_pool.size() > 0
                       and np.random.random() < cfg.opponent_sample_prob)
            if use_opp:
                if opp_policy is None:
                    opp_policy = OpenAIPolicy(cfg).to(dev)
                opp_sd = opponent_pool.sample()
                opp_policy.load_state_dict(
                    {k: v.to(dev) for k, v in opp_sd.items()})
                opp_policy.eval()

            # ── Vectorised rollout ────────────────────────────────────────
            result = collect_vectorized(
                vec_env, policy, cfg, dev, normalizers,
                use_opp=use_opp, opp_policy=opp_policy)
            (trajectories, h_rews, s_rews, h_wins) = result

            ep_count += cfg.n_envs
            for h_r, s_r, hw in zip(h_rews, s_rews, h_wins):
                recent_h.append(h_r)
                recent_s.append(s_r)
                recent_wr.append(hw)

            # ── Update task sampler (PLR learnability = mean |GAE advantage|) ──
            # Raw GAE advantages, computed BEFORE PPO normalises its own copy.
            if trajectories:
                mean_abs_adv = float(
                    torch.cat([t['adv'] for t in trajectories]).abs().mean())
            else:
                mean_abs_adv = 0.0
            task_sampler.update(cur_phase, ep_count, mean_abs_adv, h_wins)

            # ── PPO update ────────────────────────────────────────────────
            if trajectories:
                ppo_stats = ppo_update(policy, optimizer, trajectories)
                scheduler.step()
            else:
                ppo_stats = None

            # ── Opponent pool snapshot ────────────────────────────────────
            if ep_count % cfg.opponent_save_freq < cfg.n_envs:
                opponent_pool.add(policy.state_dict())
                print(f"\n  ▸ Opponent pool snapshot added at ep {ep_count:,}"
                      f"  (pool size: {opponent_pool.size()}/{cfg.opponent_pool_size})")

            # ── Early one-time export ─────────────────────────────────────
            if not early_exported and ep_count >= cfg.early_export_ep:
                early_exported = True
                epath = os.path.join(cfg.checkpoint_dir,
                                     f'checkpoint_{ep_count:08d}.npz')
                save_npz(policy, optimizer, ep_count, history, normalizers,
                         epath, opponent_pool=opponent_pool,
                         task_sampler=task_sampler)
                history['episodes'].append(ep_count)
                history['hider_rewards'].append(
                    np.mean(recent_h) if recent_h else 0)
                history['seeker_rewards'].append(
                    np.mean(recent_s) if recent_s else 0)
                history['hider_winrate'].append(
                    np.mean(recent_wr) if recent_wr else 0)
                history['curriculum_phase'].append(cur_phase)
                history['pool_size'].append(opponent_pool.size())
                save_plot(history, cfg.plot_path)
                sz = os.path.getsize(epath)
                print(f"\n  ★ Early export: {epath}  ({sz/1024:.0f} KB)")
                print(f"  ★ Early export: {cfg.plot_path}")

            # ── Periodic checkpoint ───────────────────────────────────────
            if ep_count - last_ckpt >= cfg.checkpoint_freq:
                last_ckpt = ep_count
                cpath = os.path.join(cfg.checkpoint_dir,
                                     f'checkpoint_{ep_count:08d}.npz')
                save_npz(policy, optimizer, ep_count, history, normalizers,
                         cpath, opponent_pool=opponent_pool,
                         task_sampler=task_sampler)
                sz = os.path.getsize(cpath)
                print(f"\n  ✓ Saved {cpath}  ({sz/1024:.0f} KB)")
                # Prune old checkpoints — keep only the last N (0 = keep all)
                if cfg.keep_last_checkpoints > 0:
                    all_ckpts = sorted(
                        f for f in os.listdir(cfg.checkpoint_dir)
                        if f.startswith('checkpoint_') and f.endswith('.npz')
                    )
                    to_delete = all_ckpts[:-cfg.keep_last_checkpoints]
                    for old in to_delete:
                        try:
                            os.remove(os.path.join(cfg.checkpoint_dir, old))
                        except OSError:
                            pass

            # ── Rolling resume checkpoint (crash safety, single file) ──────
            # Hard crashes (segfault / OOM-kill / power loss) bypass the SIGTERM
            # emergency save, so keep a frequently-overwritten resume point.
            # It is NOT in the checkpoint_*.npz milestone set, so it never
            # clutters the per-phase snapshots the user renders.
            if ep_count - last_resume >= cfg.resume_freq:
                last_resume = ep_count
                rpath = os.path.join(cfg.checkpoint_dir, 'resume_latest.npz')
                try:
                    save_npz(policy, optimizer, ep_count, history,
                             normalizers, rpath, opponent_pool=opponent_pool,
                             task_sampler=task_sampler)
                except Exception:
                    pass

            # ── Periodic plot ─────────────────────────────────────────────
            if ep_count - last_plot >= cfg.plot_freq:
                last_plot = ep_count
                history['episodes'].append(ep_count)
                history['hider_rewards'].append(
                    np.mean(recent_h) if recent_h else 0)
                history['seeker_rewards'].append(
                    np.mean(recent_s) if recent_s else 0)
                history['hider_winrate'].append(
                    np.mean(recent_wr) if recent_wr else 0)
                history['curriculum_phase'].append(cur_phase)
                history['pool_size'].append(opponent_pool.size())
                threading.Thread(
                    target=save_plot,
                    args=(deepcopy(history), cfg.plot_path),
                    daemon=True).start()

            # ── Periodic diagnostic report (multi-line health check) ─────
            if ep_count % cfg.diagnostic_freq < cfg.n_envs:
                ah  = np.mean(recent_h) if recent_h else 0
                a_s = np.mean(recent_s) if recent_s else 0
                wr  = np.mean(recent_wr) if recent_wr else 0
                elapsed = time.time() - t_start
                eps = max((ep_count - start_ep) / max(elapsed, 1), 0.001)

                # Milestone hints from the spine config (task#0 = 1 door, fully
                # blockable).  DOOR-BLOCKING shows as its hider WR climbing high;
                # once seekers discover RAMP-USE they break into the sealed room
                # so that WR DIPS; RAMP-DEFENSE (hiders move/lock the ramp away)
                # then recovers it.  Watching task#0's hiderWR over time traces
                # the whole OpenAI milestone sequence.
                ew = task_sampler.win_h[cfg.task_easy_idx]
                spine_wr = float(np.mean(ew)) if len(ew) else float('nan')
                milestone = ""
                if not np.isnan(spine_wr):
                    if spine_wr >= 0.70:
                        milestone = ("  🎯 Door-blocking solid on 1-door config "
                                     f"(spine hiderWR {spine_wr:.0%}) — watch for a DIP = seekers learning RAMP-USE")
                    elif spine_wr <= 0.55 and ep_count >= cfg.task_warmup_episodes:
                        milestone = (f"  🧗 Spine hiderWR dipped to {spine_wr:.0%} "
                                     "— seekers may be breaking in via RAMP-USE (recovery later = RAMP-DEFENSE)")
                    elif ep_count >= 200_000 and wr < 0.20:
                        milestone = "  ⚠ Hider WR very low — check for instability"

                pg = ppo_stats['pg'] if ppo_stats else float('nan')
                vf = ppo_stats['vf'] if ppo_stats else float('nan')
                et = ppo_stats['ent'] if ppo_stats else float('nan')

                print(
                    f"\n  ┌─ Diagnostic @ ep {ep_count:,} "
                    f"({eps:.1f} ep/s, {elapsed/3600:.1f} h elapsed) ─\n"
                    f"  │ Rewards    H:{ah:+6.2f}  S:{a_s:+6.2f}   "
                    f"Hider WR: {wr:.1%}\n"
                    f"  │ PPO losses pg:{pg:+.4f}  vf:{vf:.4f}  ent:{et:+.3f}\n"
                    f"  │ Current task#{cur_phase} "
                    f"(p_door_dropout={cur_kw.get('p_door_dropout', 0):.2f})   "
                    f"Pool: {opponent_pool.size()}/{cfg.opponent_pool_size}\n"
                    f"  │ Task sampler (PLR) — share / hiderWR / learnability:\n"
                    f"{task_sampler.report()}\n"
                    f"  │ LR: {optimizer.param_groups[0]['lr']:.2e}"
                    f"{milestone}\n"
                    f"  └─"
                )

            # ── Terminal output (single overwriting line) ────────────────
            if ep_count % cfg.terminal_freq < cfg.n_envs:
                elapsed = time.time() - t_start
                eps = max((ep_count - start_ep) / max(elapsed, 1), 0.001)
                eta = (cfg.total_episodes - ep_count) / eps
                pct = 100.0 * ep_count / cfg.total_episodes
                ah  = np.mean(recent_h) if recent_h else 0
                a_s = np.mean(recent_s) if recent_s else 0
                wr  = np.mean(recent_wr) if recent_wr else 0

                eta_d = int(eta // 86400)
                eta_h = int(eta % 86400 // 3600)
                eta_m = int(eta % 3600 // 60)

                # Progress bar (20 chars wide)
                bar_len = 20
                filled = int(bar_len * pct / 100)
                bar = '█' * filled + '░' * (bar_len - filled)

                line = (
                    f"\r  {bar} {pct:5.1f}% "
                    f"Ep {ep_count:>9,}/{cfg.total_episodes:,}"
                    f" | H:{ah:+6.1f} S:{a_s:+6.1f} WR:{wr:.0%}"
                    f" | Ph:{cur_phase} Pool:{opponent_pool.size():>2}"
                    f" | ETA:{eta_d}d{eta_h:02d}h{eta_m:02d}m"
                    f" | {eps:.1f}ep/s")
                sys.stdout.write(line)
                sys.stdout.flush()

    finally:
        vec_env.close()

    # ── Finish ────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    print("\n" + "═" * 72)
    if shutdown:
        print("  Training interrupted (Ctrl+C) — saving checkpoint …")
    else:
        print("  Training complete!")
    print(f"  Episodes: {ep_count:,}   Time: {elapsed/3600:.1f} h"
          f"   ({ep_count/max(elapsed,1):.1f} ep/s avg)")

    save_npz(policy, optimizer, ep_count, history, normalizers,
             cfg.final_npz_path, opponent_pool=opponent_pool,
             task_sampler=task_sampler)
    print(f"  ✓ {cfg.final_npz_path}"
          f"  ({os.path.getsize(cfg.final_npz_path)/1024:.0f} KB)")
    save_plot(history, cfg.plot_path)
    print(f"  ✓ {cfg.plot_path}")
    print("═" * 72)


if __name__ == '__main__':
    train()
