#!/usr/bin/env python3
"""
Render a video using the AdA-trained policy.
Usage:
    python3 render_ada.py                              # uses final_policy.npz
    python3 render_ada.py path/to/checkpoint.npz       # uses a specific checkpoint
"""
import os, sys, pickle
import numpy as np
import torch

ADA_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(ADA_DIR)
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

import warnings
warnings.filterwarnings('ignore')

from train_ada import (
    OpenAIPolicy as AdAPolicy, Config,
    flatten_all_agents, obs_list_to_tensor,
    actions_to_env, make_single_env, load_npz,
    RunningMeanStd, TASK_SPACE,
)

import imageio
from mujoco_py import MjRenderContextOffscreen


def main():
    cfg = Config()
    # Force CPU so a live training run keeps full GPU ownership.
    dev = 'cpu'
    cfg.device = dev

    # ── Load policy ───────────────────────────────────────────────────────
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        ADA_DIR, 'checkpoints', 'final_policy.npz')
    print(f"Loading policy from: {path}")
    policy = AdAPolicy(cfg).to(dev)
    ep_num, _, normalizers = load_npz(path, policy)
    policy.eval()
    print(f"  Loaded (trained for {ep_num:,} episodes)")

    # Fallback normalizers if checkpoint didn't have them
    if normalizers is None:
        normalizers = {
            'self_obs':  RunningMeanStd((10,)),
            'agent_obs': RunningMeanStd((10,)),
            'box_obs':   RunningMeanStd((12,)),
            'ramp_obs':  RunningMeanStd((cfg.ramp_feat,)),
            'lidar':     RunningMeanStd((1,)),
        }

    # ── Create environment ──────────────────────────────────────────────
    # Run 3 uses TASK_SPACE (PLR sampler) instead of a hand-scheduled
    # curriculum.  Render with p_door_dropout=0.5 so the video shows a MIX of
    # 1-door and 2-door quadrants (door dropout is re-randomised on every reset).
    # Override: RENDER_P_DOOR=1.0 forces 1 door, 0.0 forces 2 doors.
    # The ramp now always spawns OUTSIDE the hider quadrant (ramp_outside_quadrant
    # is set in BASE_ENV_KWARGS and inherited here via make_single_env).
    p_door = float(os.environ.get('RENDER_P_DOOR', '0.5'))
    env = make_single_env({'p_door_dropout': p_door})
    obs = env.reset()

    N_EPISODES = int(os.environ.get('RENDER_EPISODES', '5'))
    W, H = 640, 480
    FPS = 20
    OUT = os.path.expanduser(os.environ.get('RENDER_OUTPUT', os.path.join(ADA_DIR, 'ada_hide_and_seek.mp4')))

    frames = []
    NA = cfg.n_agents
    print(f"\nRendering {N_EPISODES} episodes...")

    for ep in range(N_EPISODES):
        obs = env.reset()
        pi_hx, pi_cx, vf_hx, vf_cx = policy.init_hidden(NA, dev)
        ep_rew = np.zeros(NA)

        # Create fresh render context after each reset (sim changes)
        sim = env.unwrapped.sim
        render_ctx = MjRenderContextOffscreen(sim, device_id=-1)
        render_ctx.cam.distance   = 12
        render_ctx.cam.elevation  = -65
        render_ctx.cam.azimuth    = 90
        render_ctx.cam.lookat[:]  = [3, 3, 0]

        for step in range(cfg.horizon):
            render_ctx.render(W, H, camera_id=-1)
            frame = np.asarray(
                render_ctx.read_pixels(W, H, depth=False), dtype=np.uint8)
            frames.append(frame[::-1])

            agent_obs_list = flatten_all_agents(obs, NA)
            obs_t = obs_list_to_tensor(agent_obs_list, dev)

            # Normalize observations using trained normalizers
            norm_obs = {}
            for k in obs_t:
                if k in normalizers:
                    v = obs_t[k].cpu().numpy()
                    norm_obs[k] = torch.tensor(
                        normalizers[k].normalize(v),
                        dtype=torch.float32, device=dev)
                else:
                    norm_obs[k] = obs_t[k]

            with torch.no_grad():
                move, pull, glue, _, _, pi_hx, pi_cx, vf_hx, vf_cx = \
                    policy.act(norm_obs, pi_hx, pi_cx, vf_hx, vf_cx,
                               deterministic=True)

            env_action = actions_to_env(move, pull, glue, NA)
            obs, rewards, done, info = env.step(env_action)

            for i in range(NA):
                ep_rew[i] += float(rewards[i]) if hasattr(
                    rewards, '__len__') else float(rewards)
            if done:
                break

        h_r = np.mean(ep_rew[:cfg.n_hiders])
        s_r = np.mean(ep_rew[cfg.n_hiders:])
        print(f"  Episode {ep+1}: Hiders {h_r:+.0f}  Seekers {s_r:+.0f}")

        # Black frames between episodes
        for _ in range(15):
            frames.append(np.zeros((H, W, 3), dtype=np.uint8))

    print(f"\nSaving {len(frames)} frames → {OUT}")
    writer = imageio.get_writer(OUT, fps=FPS, codec='libx264',
                                quality=8, pixelformat='yuv420p')
    for f in frames:
        writer.append_data(f)
    writer.close()
    print(f"Done! {os.path.getsize(OUT) / 1024:.0f} KB")


if __name__ == '__main__':
    main()
