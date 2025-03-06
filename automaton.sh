#!/bin/bash

# Путь к Python-скрипту
PYTHON_SCRIPT="~/rodos_scheduler/rodos_scheduler.py"
LOG_FILE="/var/log/script_monitor.log"

# Проверка активности процесса
if ! pgrep -f "$PYTHON_SCRIPT" > /dev/null; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - The script is not active. Starting..." >> "$LOG_FILE"
    /usr/bin/python3 "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1 &
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - The script is working." >> "$LOG_FILE"
fi