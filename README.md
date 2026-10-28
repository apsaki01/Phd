# Hide-and-Seek with Adaptive Auto-Curriculum

This repository reproduces the final Hide-and-Seek experiment: OpenAI's quadrant environment and policy architecture, extended with a self-play opponent pool and an adaptive task curriculum.

## What is included

- `train_ada.py`: final training program used for the 43.4M-episode run.
- `render_ada.py`: render our policy checkpoint to MP4.
- `render_quadrant.py`: render the original OpenAI policy supplied in the environment repository.
- `run_train.sh`: training launcher with restart handling.
- `setup_vastai.sh`: installs the required Ubuntu, MuJoCo, Python, PyTorch, Gym, TensorFlow, and rendering dependencies.
- `monitor.sh`: follows training progress.
- `validate_ramp_fix.py`: environment validation script.
- `mujoco-worldgen/`: vendored OpenAI worldgen dependency.
- `multi-agent-emergence-environments/`: vendored OpenAI environment and policy code.
- `training_output_run4/`: the final policy and all saved training checkpoints.

The checkpoints are stored with Git LFS. The paper is not included in this repository.

## Reproduce the project

Use Ubuntu 20.04 or 22.04 on a native x86_64 Vast.ai machine. The tested target is an NVIDIA RTX 4090, at least 32 CPU cores, and at least 64 GB RAM. CUDA 11.8 or newer is suitable.

```bash
git lfs install
git clone https://github.com/apsaki01/Phd.git
cd Phd
git lfs pull
```

The legacy MuJoCo 1.50 environment requires a valid MuJoCo key. Obtain your own
key and place it at `/root/.mujoco/mjkey.txt` (or set
`MUJOCO_PY_MJKEY_PATH` to its location). The key is intentionally not included
in this repository and must not be committed.

Then install the dependencies:

```bash
bash setup_vastai.sh
source ~/.bashrc
```

For a new training run:

```bash
bash run_train.sh
```

This starts a fresh run in `training_output/`. In another terminal, monitor it
with `bash monitor.sh`. Set `OUTPUT_DIR` to use a different output location.

To resume from the included run's latest checkpoint, use:

```bash
OUTPUT_DIR=training_output_run4 bash run_train.sh
```

The final experiment used 128 worker environments, an 80-step horizon, 4 PPO epochs, 1 minibatch, a 256-unit LSTM, 128-dimensional entity embeddings, 4 attention heads, an opponent pool of 10 snapshots, and a target of 43,400,000 episodes. A native x86_64 Ubuntu machine with a CUDA-capable GPU, 32 or more CPU cores, and at least 64 GB RAM is recommended.

## Render a checkpoint

The renderer uses CPU so it does not require the training GPU:

```bash
RENDER_EPISODES=5 \
RENDER_OUTPUT=ada_hide_and_seek.mp4 \
python3 render_ada.py training_output_run4/final_policy.npz
```

Set `RENDER_P_DOOR=1.0` for one-door scenes or `RENDER_P_DOOR=0.0` for two-door scenes. The default is a mixture.

## License and acknowledgements

The environment and worldgen code originate from OpenAI's open-source Multi-Agent Emergence Environments and MuJoCo worldgen projects. The experiment code in this repository builds on those projects and should retain their original license files.
