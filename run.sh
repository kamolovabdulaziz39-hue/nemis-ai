#!/usr/bin/env bash
python keep_alive.py &
while true; do python bot.py > bot.log 2>&1; sleep 5; done &
cd website && gunicorn app:app --bind 0.0.0.0:$PORT
