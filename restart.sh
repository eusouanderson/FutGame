#!/bin/bash

# Matar processo existente do uvicorn (se houver)
PID=$(ps aux | grep 'uvicorn' | grep -v 'grep' | awk '{print $2}')
if [ ! -z "$PID" ]; then
  echo "Parando servidor FastAPI com PID $PID..."
  kill -9 $PID
fi

# Iniciar o servidor novamente usando poetry
echo "Iniciando servidor FastAPI..."
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &
echo "Servidor iniciado. Verifique server.log para detalhes."
