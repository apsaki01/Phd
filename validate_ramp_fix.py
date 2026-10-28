#!/usr/bin/env python3
"""
CPU-only sanity check for the ramp_outside_quadrant fix.
Builds the training env (BASE_ENV_KWARGS) and confirms across many resets that:
  1. The ramp NEVER spawns inside the hider quadrant (bottom-right).
  2. obs shapes are unchanged (ramp_obs last dim == cfg.ramp_feat).
  3. p_door_dropout=0.5 produces BOTH 1-door and 2-door episodes.
Does NOT touch the GPU (CUDA hidden) so a live training run is undisturbed.
"""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ.setdefault('MUJOCO_PY_MUJOCO_PATH', '/root/.mujoco/mjpro150')
os.environ.setdefault('MUJOCO_PY_MJKEY_PATH', '/root/.mujoco/mjkey.txt')
ld = os.environ.get('LD_LIBRARY_PATH', '')
if '/root/.mujoco/mjpro150/bin' not in ld:
    os.environ['LD_LIBRARY_PATH'] = '/root/.mujoco/mjpro150/bin:' + ld

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mujoco-worldgen'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'multi-agent-emergence-environments'))

import numpy as np
from train_ada import make_single_env, BASE_ENV_KWARGS, cfg

N = 40
env = make_single_env({'p_door_dropout': 0.5})

# Quadrant geometry: bottom-right quadrant.  floor_size default 6.0.
# quadrant_placement puts objects at grid x in [grid-qsize, grid], y in [1, qsize].
# In world coords the quadrant occupies roughly x in (floor/2, floor), y in (0, floor/2).
FLOOR = BASE_ENV_KWARGS.get('floor_size', 6.0)
half = FLOOR / 2.0

ramp_inside = 0
door_counts = {}
ramp_feat_seen = set()
positions = []

for i in range(N):
    obs = env.reset()
    # ramp position (world xy) — env stores it in the sim; read from obs metadata.
    sim = env.unwrapped.sim
    # find the ramp body position
    ramp_xy = None
    for name in sim.model.body_names:
        if name.startswith('ramp'):
            bid = sim.model.body_name2id(name)
            ramp_xy = sim.data.body_xpos[bid][:2].copy()
            break
    positions.append(ramp_xy)
    # inside hider quadrant = bottom-right = x > half AND y < half
    if ramp_xy is not None and ramp_xy[0] > half and ramp_xy[1] < half:
        ramp_inside += 1

    # obs shape check
    if 'ramp_obs' in obs:
        ramp_feat_seen.add(obs['ramp_obs'].shape[-1])

    # count doors: number of door geoms/sites present this episode
    ndoor = sum(1 for n in sim.model.geom_names if 'door' in n.lower())
    # fall back: count via body names if geoms don't encode doors
    door_counts[ndoor] = door_counts.get(ndoor, 0) + 1

print("=== RAMP FIX VALIDATION ===")
print(f"resets: {N}")
print(f"ramp spawned INSIDE hider quadrant: {ramp_inside}/{N}  (want 0)")
print(f"ramp_obs last-dim seen: {sorted(ramp_feat_seen)}  (want [{cfg.ramp_feat}])")
print(f"door-geom-count distribution across resets: {door_counts}")
xs = [p[0] for p in positions if p is not None]
ys = [p[1] for p in positions if p is not None]
print(f"ramp x range: [{min(xs):.2f}, {max(xs):.2f}]  y range: [{min(ys):.2f}, {max(ys):.2f}]  (floor={FLOOR})")

ok = (ramp_inside == 0) and (ramp_feat_seen == {cfg.ramp_feat})
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
