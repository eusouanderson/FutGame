#!/bin/bash


PID=$(sudo lsof -t -i :8000)

if [ -n "$PID" ]; then
    echo "Matar processo com PID: $PID"
    sudo kill -9 $PID
fi

echo "Reiniciando o servidor FastAPI..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
