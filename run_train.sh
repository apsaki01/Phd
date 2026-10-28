#!/bin/bash
# run_train.sh — robust training launcher with auto-restart on worker hang.
#
# - Launches train_ada.py
# - If Python exits with code 2 (mujoco hang we detected via watchdog),
#   restart automatically up to MAX_RETRIES times. Training resumes from
#   the latest checkpoint (which save_npz wrote just before exit).
# - Any other exit code (0=success, 1=other error, 130=SIGINT) → stop.
#
# Set OUTPUT_DIR to an existing checkpoint directory to resume that run.

set -u
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"
OUTPUT_DIR="${OUTPUT_DIR:-$REPO_DIR/training_output}"
case "$OUTPUT_DIR" in
    /*) ;;
    *) OUTPUT_DIR="$REPO_DIR/$OUTPUT_DIR" ;;
esac
export OUTPUT_DIR

# MuJoCo 1.50 env vars (required for mujoco_py to find the binary)
export LD_LIBRARY_PATH=/root/.mujoco/mjpro150/bin${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export MUJOCO_PY_MUJOCO_PATH=/root/.mujoco/mjpro150
export MUJOCO_PY_MJKEY_PATH="${MUJOCO_PY_MJKEY_PATH:-/root/.mujoco/mjkey.txt}"
if [ ! -f "$MUJOCO_PY_MJKEY_PATH" ]; then
    echo "MuJoCo key not found at: $MUJOCO_PY_MJKEY_PATH"
    echo "Set MUJOCO_PY_MJKEY_PATH to your own valid key file."
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

MAX_RETRIES=10
TRAIN_LOG="$OUTPUT_DIR/train.log"

attempt=0
while [ "$attempt" -le "$MAX_RETRIES" ]; do
    ts=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$ts] Starting train_ada.py (attempt $((attempt+1))/$((MAX_RETRIES+1)))"

    # On retries, archive the previous log so it's not overwritten
    if [ "$attempt" -gt 0 ] && [ -f "$TRAIN_LOG" ]; then
        mv "$TRAIN_LOG" "${TRAIN_LOG%.log}.attempt${attempt}.log"
    fi

    /venv/py38/bin/python3.8 -u train_ada.py > "$TRAIN_LOG" 2>&1
    rc=$?

    # Clean up temp XML files leaked by mujoco_py/worldgen on every episode reset
    find /tmp -maxdepth 1 -name 'tmp*.xml' -delete 2>/dev/null || true

    ts=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$ts] train_ada.py exited with code $rc"

    if [ "$rc" -eq 0 ]; then
        echo "[$ts] ✓ Training completed normally"
        exit 0
    elif [ "$rc" -eq 2 ]; then
        echo "[$ts] ⚠ Worker hang detected — restarting from latest checkpoint"
        attempt=$((attempt+1))
        sleep 5
        # leftover shmem segments / orphaned mujoco workers?
        pkill -9 -f train_ada.py 2>/dev/null || true
        sleep 2
        continue
    else
        echo "[$ts] ✗ Non-recoverable exit code $rc — stopping"
        exit "$rc"
    fi
done

echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✗ Max retries ($MAX_RETRIES) exceeded"
exit 3
