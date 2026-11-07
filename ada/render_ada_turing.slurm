#!/bin/bash
#SBATCH --partition=COMPUTE
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:45:00
#SBATCH --job-name=ada-render
#SBATCH --output=ada-render-%j.out

set -euo pipefail
PROJECT_DIR="${PHD_DIR:-$HOME/Phd}/ada"
cd "$PROJECT_DIR"

module load Anaconda3/2025.06-1
module load GCCcore/12.3.0
module load Mesa/23.1.4-GCCcore-12.3.0
module load glew/2.2.0-GCCcore-12.3.0-osmesa

export MUJOCO_PY_MJPRO_PATH="$HOME/.mujoco/mjpro150"
export MUJOCO_PY_MJKEY_PATH="$HOME/.mujoco/mjkey.txt"
export MUJOCO_GL=osmesa
export LD_LIBRARY_PATH="$MUJOCO_PY_MJPRO_PATH/bin:$EBROOTMESA/lib:$EBROOTGLEW/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export CPATH="$EBROOTMESA/include:$EBROOTGLEW/include${CPATH:+:$CPATH}"
export LIBRARY_PATH="$EBROOTMESA/lib:$EBROOTGLEW/lib${LIBRARY_PATH:+:$LIBRARY_PATH}"
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1

CHECKPOINT="${ADA_CHECKPOINT:-$PROJECT_DIR/checkpoints/final_policy.npz}"
export RENDER_EPISODES="${RENDER_EPISODES:-10}"
export RENDER_OUTPUT="${RENDER_OUTPUT:-$HOME/ada_hide_and_seek_10episodes.mp4}"

if [[ ! -s "$CHECKPOINT" ]]; then
    echo "Checkpoint not found: $CHECKPOINT" >&2
    exit 2
fi

# mujoco_py leaks one tmp*.xml per episode reset into $TMPDIR
export TMPDIR="/tmp/${USER}_render_${SLURM_JOB_ID:-$$}"
mkdir -p "$TMPDIR"
trap 'rm -rf "$TMPDIR"' EXIT

srun --cpu-bind=cores "$HOME/conda_envs/gap38/bin/python" -u render_ada.py "$CHECKPOINT"