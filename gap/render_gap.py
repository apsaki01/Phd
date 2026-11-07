#!/usr/bin/env python3
"""
Render episodes played by the GaP team graphs to an MP4 (CPU only).
Usage:
    python3 render_gap.py                                   # best graphs from GAP_OUTPUT_DIR
    python3 render_gap.py hider_graph.json seeker_graph.json
Env:
    RENDER_EPISODES=5  RENDER_P_DOOR=0.5  RENDER_OUTPUT=~/gap_hide_and_seek.mp4
"""
import os, sys, json
import numpy as np
import train_gap as G
import imageio
from mujoco_py import MjRenderContextOffscreen


def main():
    out_dir = G.cfg.output_dir
    hpath = sys.argv[1] if len(sys.argv) > 1 else os.path.join(out_dir, 'best_hider_graph.json')
    spath = sys.argv[2] if len(sys.argv) > 2 else os.path.join(out_dir, 'best_seeker_graph.json')
    with open(hpath) as f:
        hider = json.load(f)
    with open(spath) as f:
        seeker = json.load(f)
    assert G.validate_graph(hider, 'hider') and G.validate_graph(seeker, 'seeker')
    print('hider graph:\n' + G.describe_graph(hider))
    print('seeker graph:\n' + G.describe_graph(seeker))

    env = G.make_env(**G.ENV_KWARGS)
    n_eps = int(os.environ.get('RENDER_EPISODES', '5'))
    p_door = float(os.environ.get('RENDER_P_DOOR', '0.5'))
    out = os.path.expanduser(os.environ.get('RENDER_OUTPUT', '~/gap_hide_and_seek.mp4'))
    W, H, FPS = 640, 480, 20
    frames = []
    ctx = {'r': None}

    def frame_cb(env_, t):
        if t == 0 or ctx['r'] is None:
            ctx['r'] = MjRenderContextOffscreen(env_.unwrapped.sim, device_id=-1)
            ctx['r'].cam.distance, ctx['r'].cam.elevation, ctx['r'].cam.azimuth = 12, -65, 90
            ctx['r'].cam.lookat[:] = [3, 3, 0]
        ctx['r'].render(W, H, camera_id=-1)
        frame = np.asarray(ctx['r'].read_pixels(W, H, depth=False), dtype=np.uint8)
        frames.append(frame[::-1])

    for ep in range(n_eps):
        ctx['r'] = None
        res = G.run_episode(env, hider, seeker, p_door, 1000 + ep, frame_cb=frame_cb)
        if res is None:
            print('  episode %d discarded (MuJoCo instability)' % (ep + 1))
            continue
        print('  episode %d: J_hider=%.2f hider_win=%s behaviours=%s' % (
            ep + 1, res['J_hider'], res['hider_win'], {k: v for k, v in res['behaviours'].items() if v}))
        frames.extend([np.zeros((H, W, 3), dtype=np.uint8)] * 15)

    print('saving %d frames -> %s' % (len(frames), out))
    w = imageio.get_writer(out, fps=FPS, codec='libx264', quality=8, pixelformat='yuv420p')
    for f in frames:
        w.append_data(f)
    w.close()
    print('done (%.0f KB)' % (os.path.getsize(out) / 1024))


if __name__ == '__main__':
    main()
