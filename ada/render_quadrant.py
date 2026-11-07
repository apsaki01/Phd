#!/usr/bin/env python3
"""
Render the Hide and Seek quadrant scenario with a TRAINED policy to video.
Uses offscreen rendering for Docker container.
"""
import os
os.environ['MUJOCO_GL'] = 'osmesa'

import numpy as np
import imageio
from operator import itemgetter

from mujoco_py import MjRenderContextOffscreen
from mujoco_worldgen.util.envs import load_env
from mae_envs.wrappers.multi_agent import JoinMultiAgentActions
from ma_policy.load_policy import load_policy
from ma_policy.util import listdict2dictnp
from gym.spaces import Tuple

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(os.path.dirname(PROJECT_DIR), 'multi-agent-emergence-environments')


def splitobs(obs, keepdims=True):
    n_agents = obs[list(obs.keys())[0]].shape[0]
    return [{k: v[[i]] if keepdims else v[i] for k, v in obs.items()} for i in range(n_agents)]


def render_frame(sim, offscreen_ctx, width=640, height=480):
    offscreen_ctx.render(width, height, camera_id=-1)
    frame = offscreen_ctx.read_pixels(width, height, depth=False)
    return frame[::-1]
    core_dir = os.path.join(PROJECT_DIR, 'multi-agent-emergence-environments')

def main():
    core_dir = CORE_DIR
    jsonnet_path = os.path.join(core_dir, 'examples', 'hide_and_seek_quadrant.jsonnet')
    policy_path = os.path.join(core_dir, 'examples', 'hide_and_seek_quadrant.npz')

    print("Loading environment from jsonnet...")
    env = load_env(jsonnet_path, core_dir=core_dir,
                   envs_dir='mae_envs/envs', xmls_dir='xmls')

    if isinstance(env.action_space, Tuple):
        env = JoinMultiAgentActions(env)

    obs = env.reset()
    print(f"Environment loaded. Obs keys: {sorted(obs.keys())}")

    print("Loading trained policy...")
    policy = load_policy(policy_path, env=env, scope='policy_0')
    policy.reset()
    print("Policy loaded!")

    n_episodes = 3
    all_frames = []
    width, height = 640, 480

    for ep in range(n_episodes):
        print(f"\n--- Episode {ep + 1}/{n_episodes} ---")
        obs = env.reset()
        policy.reset()
        sim = env.unwrapped.sim

        offscreen = MjRenderContextOffscreen(sim, device_id=-1)
        offscreen.cam.distance = 12.0
        offscreen.cam.azimuth = 90
        offscreen.cam.elevation = -65
        offscreen.cam.lookat[0] = 3.0
        offscreen.cam.lookat[1] = 3.0
        offscreen.cam.lookat[2] = 0.0

        frames = []
        done = False
        step = 0
        total_reward = np.zeros(4)

        while not done:
            # Get action from trained policy
            action, _ = policy.act(obs)

            obs, reward, done, info = env.step(action)
            total_reward += reward

            frame = render_frame(sim, offscreen, width, height)
            frames.append(frame)
            step += 1

            if info.get('discard_episode', False):
                break

        print(f"  {step} steps, reward: {total_reward}")
        all_frames.extend(frames)

        # Black frames between episodes
        for _ in range(15):
            all_frames.append(np.zeros((height, width, 3), dtype=np.uint8))

    output_path = os.path.join(PROJECT_DIR, "hide_and_seek_quadrant.mp4")
    print(f"\nSaving video to {output_path} ({len(all_frames)} frames)...")
    writer = imageio.get_writer(output_path, fps=20, quality=8)
    for frame in all_frames:
        writer.append_data(frame)
    writer.close()
    print(f"Done! {len(all_frames)} frames at 20fps = {len(all_frames)/20:.1f}s")
    print(f"\nThe file is in your local project folder: hide_and_seek_quadrant.mp4")


if __name__ == '__main__':
    main()
