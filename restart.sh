#!/bin/bash

# Parar servidor existente (se desejar)
pkill -f "uvicorn" 2>/dev/null

echo "Iniciando servidor FastAPI..."

# Entrar na pasta app e iniciar o servidor com poetry
cd app || exit
echo "Entrando na pasta $APP_DIR"

echor "Iniciando o servidor FastAPI..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 > ../server.log 2>&1 &

echo "Servidor iniciado. Verifique server.log para detalhes."
