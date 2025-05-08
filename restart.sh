#!/bin/bash

# Encontrar e matar processo na porta 8000
PID=$(sudo lsof -t -i :8000)

if [ -n "$PID" ]; then
    echo "Encerrando processo com PID: $PID"
    sudo kill -9 $PID
    sleep 2  # Dar um tempo para o processo encerrar completamente
fi

echo "Iniciando servidor FastAPI..."
# Executar em background e redirecionar logs para um arquivo
nohup poetry run uvicorn main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &

echo "Servidor iniciado. Verifique server.log para detalhes."
