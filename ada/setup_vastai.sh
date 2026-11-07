#!/bin/bash
# =========================================================================
#  vast.ai setup script for Hide-and-Seek + AdA training
#  Target: Ubuntu 20.04 / 22.04, native x86_64, NVIDIA GPU (CUDA 11.x+)
#  Usage:  bash setup_vastai.sh
#  Time:   ~10-20 min depending on CPU
# =========================================================================
set -e
export DEBIAN_FRONTEND=noninteractive
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"
export MUJOCO_PY_MJKEY_PATH="${MUJOCO_PY_MJKEY_PATH:-/root/.mujoco/mjkey.txt}"

if [ ! -f "$MUJOCO_PY_MJKEY_PATH" ]; then
    echo "MuJoCo key not found at: $MUJOCO_PY_MJKEY_PATH"
    echo "Obtain your own valid key and place it there; do not commit it to GitHub."
    exit 1
fi

echo "========================================================="
echo "  vast.ai bootstrap — Hide-and-Seek + AdA"
echo "  Repo dir: $REPO_DIR"
echo "========================================================="

echo ""; echo "[1/10] System packages..."
apt-get update -qq
apt-get install -y --no-install-recommends \
    git curl wget ca-certificates build-essential cmake pkg-config \
    python3.8 python3.8-dev python3.8-venv python3-pip \
    libgl1-mesa-dev libgl1-mesa-glx libosmesa6-dev libglew-dev libglfw3-dev \
    patchelf unzip xvfb ffmpeg 2>&1 | tail -1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 2>/dev/null || true
update-alternatives --install /usr/bin/python  python  /usr/bin/python3.8 1 2>/dev/null || true
echo "  OK"

echo ""; echo "[2/10] MuJoCo 1.50..."
if [ ! -d "/root/.mujoco/mjpro150" ]; then
    mkdir -p /root/.mujoco
    wget -q https://www.roboti.us/download/mjpro150_linux.zip -O /tmp/mjpro150.zip
    unzip -qo /tmp/mjpro150.zip -d /root/.mujoco/
    rm -f /tmp/mjpro150.zip
fi
echo "  OK"

echo ""; echo "[3/10] Env vars (persisted to ~/.bashrc)..."
BASHRC=/root/.bashrc
if ! grep -q "MUJOCO_PY_MJPRO_PATH" "$BASHRC" 2>/dev/null; then
cat >> "$BASHRC" <<EOF

# ===== Hide-and-Seek + AdA env =====
export MUJOCO_PY_MJPRO_PATH=/root/.mujoco/mjpro150
export MUJOCO_PY_MJKEY_PATH=$MUJOCO_PY_MJKEY_PATH
export LD_LIBRARY_PATH=/root/.mujoco/mjpro150/bin:\${LD_LIBRARY_PATH}
export MUJOCO_GL=osmesa
export PYTHONPATH=$REPO_DIR/mujoco-worldgen:$REPO_DIR/multi-agent-emergence-environments:\${PYTHONPATH}
EOF
fi
export MUJOCO_PY_MJPRO_PATH=/root/.mujoco/mjpro150
export MUJOCO_PY_MJKEY_PATH=$MUJOCO_PY_MJKEY_PATH
export LD_LIBRARY_PATH=/root/.mujoco/mjpro150/bin:${LD_LIBRARY_PATH}
export MUJOCO_GL=osmesa
export PYTHONPATH=$REPO_DIR/mujoco-worldgen:$REPO_DIR/multi-agent-emergence-environments:${PYTHONPATH}
echo "  OK"

echo ""; echo "[4/10] pip/setuptools..."
python3 -m pip install --upgrade pip==23.3.2 setuptools==68.0.0 wheel 2>&1 | tail -1
echo "  OK"

echo ""; echo "[5/10] numpy, scipy, Cython..."
pip3 install --no-cache-dir numpy==1.21.6 scipy==1.7.3 Cython==0.29.36 2>&1 | tail -1
echo "  OK"

echo ""; echo "[6/10] mujoco-py (compiles C, a few min)..."
pip3 install --no-cache-dir mujoco-py==1.50.1.68 2>&1 | tail -1
echo "  OK"

echo ""; echo "[7/10] gym, tensorflow, baselines..."
pip3 install --no-cache-dir gym==0.15.7 cloudpickle==1.2.2 2>&1 | tail -1
pip3 install --no-cache-dir tensorflow==2.8.4 2>&1 | tail -1
pip3 install --no-cache-dir git+https://github.com/openai/baselines.git 2>&1 | tail -1
echo "  OK"

echo ""; echo "[8/10] PyTorch with CUDA (GPU build)..."
# CUDA 11.8 wheel — works on most vast.ai GPUs (Ampere/Ada/Hopper)
pip3 install --no-cache-dir torch==2.0.1 --index-url https://download.pytorch.org/whl/cu118 2>&1 | tail -1
echo "  OK"

echo ""; echo "[9/10] Remaining packages..."
pip3 install --no-cache-dir \
    imageio==2.35.1 imageio-ffmpeg==0.5.1 opencv-python==4.13.0.92 \
    glfw==2.10.0 matplotlib==3.7.5 jsonnet==0.11.2 xmltodict==0.12.0 \
    tqdm==4.67.3 numpy-stl==2.10.1 pyglet==1.5.0 lockfile==0.12.2 2>&1 | tail -1
echo "  OK"

echo ""; echo "[10/10] Patches + install local repos..."
DIST_FILE=/usr/local/lib/python3.8/dist-packages/baselines/common/distributions.py
if [ -f "$DIST_FILE" ]; then
    sed -i '1s/^import tensorflow as tf/import tensorflow.compat.v1 as tf/' "$DIST_FILE" 2>/dev/null || true
fi
GYM_SPACES=/usr/local/lib/python3.8/dist-packages/gym/spaces
if [ -d "$GYM_SPACES" ]; then
    cd "$GYM_SPACES"
    for f in dict tuple box discrete multi_binary multi_discrete; do
        ln -sf ${f}.py ${f}_space.py 2>/dev/null || true
    done
    cd "$REPO_DIR"
fi
cd "$REPO_DIR/mujoco-worldgen"                   && pip3 install -e . --no-deps 2>/dev/null || true
cd "$REPO_DIR/multi-agent-emergence-environments" && pip3 install -e . --no-deps 2>/dev/null || true
cd "$REPO_DIR"
echo "  OK"

echo ""
echo "========================================================="
echo "  Verifying install..."
python3 -c "
import sys; print(f'  Python:     {sys.version.split()[0]}')
import numpy; print(f'  numpy:      {numpy.__version__}')
import torch; print(f'  torch:      {torch.__version__}  CUDA={torch.cuda.is_available()}  device={torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"CPU only\"}')
import gym; print(f'  gym:        {gym.__version__}')
import mujoco_py; print(f'  mujoco-py:  OK')
import mujoco_worldgen; print(f'  worldgen:   OK')
import mae_envs; print(f'  mae_envs:   OK')
"
echo "========================================================="
echo "  READY."
echo ""
echo "  Next steps:"
echo "    source ~/.bashrc"
echo "    nohup bash $REPO_DIR/ada/run_train.sh > $REPO_DIR/ada/wrapper.log 2>&1 &"
echo "    bash $REPO_DIR/ada/monitor.sh"
echo "========================================================="
