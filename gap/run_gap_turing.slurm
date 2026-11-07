#!/bin/bash
#SBATCH --partition=COMPUTE
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=170G
#SBATCH --time=04:00:00
#SBATCH --job-name=gap-bench
#SBATCH --output=gap-bench-%j.out

set -euo pipefail
cd "${PHD_DIR:-$HOME/Phd}/gap"

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
export NUMEXPR_NUM_THREADS=1

: "${GAP_LLM_API_KEY:?Export GAP_LLM_API_KEY before sbatch}"
export GAP_LLM_API_KEY_HEADER=x-bf-vk
export GAP_LLM_BASE_URL=https://turing2.ucy.ac.cy/v1
export GAP_LLM_MODEL=qwen3.5:9b
export GAP_LLM_ONLY=1
export GAP_LLM_PROPOSALS="${GAP_LLM_PROPOSALS:-5}"
export GAP_WORKERS="${GAP_WORKERS:-44}"
export GAP_TOTAL_EPISODES="${GAP_TOTAL_EPISODES:-2000000}"
export GAP_REHEARSALS="${GAP_REHEARSALS:-100}"
export GAP_ROUND_WINDOW="${GAP_ROUND_WINDOW:-45}"
export GAP_OUTPUT_DIR="${GAP_OUTPUT_DIR:-$HOME/training_output_gap_turing}"

mkdir -p "$GAP_OUTPUT_DIR"

# mujoco_py leaks one tmp*.xml per episode reset into $TMPDIR
export TMPDIR="/tmp/${USER}_gap_${SLURM_JOB_ID:-$$}"
mkdir -p "$TMPDIR"
trap 'rm -rf "$TMPDIR"' EXIT
( while sleep 600; do find "$TMPDIR" -maxdepth 1 -name 'tmp*.xml' -mmin +5 -delete 2>/dev/null; done ) &

srun --cpu-bind=cores "$HOME/conda_envs/gap38/bin/python" -u train_gap.py