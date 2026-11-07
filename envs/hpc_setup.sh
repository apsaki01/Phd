#!/bin/bash
# One-time setup of the gap38 environment on the UCY HPC (turing2, login node).
# Safe to re-run: existing pieces are detected and skipped.
#   bash ~/Phd/envs/hpc_setup.sh
set -eo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/hpc_env.sh"
ENV_DIR="$HOME/conda_envs/gap38"

if [[ ! -x "$ENV_DIR/bin/python" ]]; then
    echo "[1/4] creating conda env $ENV_DIR (conda-forge only; the default channel needs a ToS accept)"
    conda create -y -p "$ENV_DIR" --override-channels -c conda-forge python=3.8.20 pip
else
    echo "[1/4] conda env exists: $ENV_DIR"
fi

if [[ ! -d "$MUJOCO_PY_MJPRO_PATH" ]]; then
    echo "[2/4] downloading MuJoCo 1.50"
    mkdir -p "$HOME/.mujoco"
    wget -q https://www.roboti.us/download/mjpro150_linux.zip -O /tmp/mjpro150_$USER.zip
    unzip -qo /tmp/mjpro150_$USER.zip -d "$HOME/.mujoco/"
    rm -f /tmp/mjpro150_$USER.zip
else
    echo "[2/4] MuJoCo exists: $MUJOCO_PY_MJPRO_PATH"
fi
if [[ ! -s "$MUJOCO_PY_MJKEY_PATH" ]]; then
    echo "      !! $MUJOCO_PY_MJKEY_PATH is missing. Upload it from your Mac (never commit it):"
    echo "         scp ~/Downloads/mjkey.txt ucy-hpc:~/.mujoco/mjkey.txt && ssh ucy-hpc chmod 600 ~/.mujoco/mjkey.txt"
fi

echo "[3/4] python packages"
"$PY" -m pip install -q pip==23.3.2 setuptools==68.0.0 wheel
"$PY" -m pip install -q -r "$HERE/requirements-gap38.txt"
"$PY" -m pip install -q torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu
"$PY" -m pip install -q --no-build-isolation mujoco-py==1.50.1.68

echo "[4/4] verify (first mujoco_py import compiles its extension; takes a few minutes once)"
cd "$PHD_DIR"
"$PY" - <<'EOF'
import sys, os
sys.path[:0] = ['mujoco-worldgen', 'multi-agent-emergence-environments']
import numpy, torch, gym, mujoco_py
from mae_envs.envs.hide_and_seek import make_env
print('python', sys.version.split()[0], '| numpy', numpy.__version__, '| torch', torch.__version__, '| gym', gym.__version__)
print('mujoco_py + mae_envs OK')
EOF
