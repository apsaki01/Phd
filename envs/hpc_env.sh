# Source this on the UCY HPC (turing2) before running anything:  source ~/Phd/envs/hpc_env.sh
module use /opt/ohpc/pub/software/modules/all
module load Anaconda3/2025.06-1
module load GCCcore/12.3.0
module load Mesa/23.1.4-GCCcore-12.3.0
module load glew/2.2.0-GCCcore-12.3.0-osmesa

export PHD_DIR="${PHD_DIR:-$HOME/Phd}"
export PY="$HOME/conda_envs/gap38/bin/python"
export MUJOCO_PY_MJPRO_PATH="$HOME/.mujoco/mjpro150"
export MUJOCO_PY_MJKEY_PATH="$HOME/.mujoco/mjkey.txt"
export MUJOCO_GL=osmesa
export LD_LIBRARY_PATH="$MUJOCO_PY_MJPRO_PATH/bin:$EBROOTMESA/lib:$EBROOTGLEW/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export CPATH="$EBROOTMESA/include:$EBROOTGLEW/include${CPATH:+:$CPATH}"
export LIBRARY_PATH="$EBROOTMESA/lib:$EBROOTGLEW/lib${LIBRARY_PATH:+:$LIBRARY_PATH}"
