#!/bin/bash
# run_gap.sh — launcher for the Graph-as-Policy (two-graph) self-learning run.
#
#   cd ~/Phd/gap
#   mkdir -p ~/training_output_gap
#   nohup bash run_gap.sh > ~/training_output_gap/wrapper.log 2>&1 & disown
#
# Output (live): ~/training_output_gap/learning_curve.png, history.csv,
#                train.log, best_hider_graph.json, best_seeker_graph.json, feedback/
# Resumes automatically from gap_state.json if the process is restarted.
set -u
cd "$(dirname "$0")"
MUJOCO_PATH="${MUJOCO_PY_MJPRO_PATH:-$HOME/.mujoco/mjpro150}"
export LD_LIBRARY_PATH="$MUJOCO_PATH/bin${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export MUJOCO_PY_MJPRO_PATH="$MUJOCO_PATH"
export MUJOCO_PY_MJKEY_PATH="${MUJOCO_PY_MJKEY_PATH:-$HOME/.mujoco/mjkey.txt}"
export GAP_OUTPUT_DIR="${GAP_OUTPUT_DIR:-$HOME/training_output_gap}"
export GAP_TOTAL_EPISODES="${GAP_TOTAL_EPISODES:-43400000}"
PYTHON_BIN="${PYTHON:-$HOME/conda_envs/gap38/bin/python}"
mkdir -p "$GAP_OUTPUT_DIR"
TRAIN_LOG="$GAP_OUTPUT_DIR/train.log"

attempt=0
while [ "$attempt" -le 10 ]; do
    echo "[$(date '+%F %T')] starting train_gap.py (attempt $((attempt+1)))"
    if [ -f "$TRAIN_LOG" ]; then mv "$TRAIN_LOG" "${TRAIN_LOG%.log}.attempt${attempt}.log"; fi
    "$PYTHON_BIN" -u train_gap.py > "$TRAIN_LOG" 2>&1
    rc=$?
    find /tmp -maxdepth 1 -name 'tmp*.xml' -delete 2>/dev/null || true
    echo "[$(date '+%F %T')] train_gap.py exited with code $rc"
    if [ "$rc" -eq 0 ] || [ "$rc" -eq 130 ]; then exit "$rc"; fi
    attempt=$((attempt+1))
    sleep 5
done
exit 3
