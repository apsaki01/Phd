#!/bin/bash
# Live monitor for training progress
# Shows the latest progress bar from the log file
# Press Ctrl+C to stop monitoring (training continues in background)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="${OUTPUT_DIR:-$SCRIPT_DIR/training_output}"
case "$OUTPUT_DIR" in
    /*) ;;
    *) OUTPUT_DIR="$SCRIPT_DIR/$OUTPUT_DIR" ;;
esac

echo "Monitoring training progress (Ctrl+C to stop, training keeps running)..."
echo ""

# Disable terminal echo so accidental keypresses don't bleed into the display.
# Restore it on exit so your shell works normally afterwards.
stty -echo 2>/dev/null
trap 'stty echo 2>/dev/null; echo; exit 0' INT TERM EXIT

while true; do
    line=$(tail -c 300 "$OUTPUT_DIR/train.log" 2>/dev/null | strings | tail -1)
    printf "\r\033[K  %s" "$line"
    sleep 5
done
