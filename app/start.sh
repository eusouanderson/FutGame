#!/bin/bash

# Inicia o servidor FastAPI
echo "Iniciando o servidor FastAPI..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 &

# Aguarda o servidor iniciar
sleep 2

# Inicia o ngrok para a porta 8000
echo "Iniciando o ngrok..."
ngrok http 8000 &

# Aguarda o ngrok gerar a URL pública
sleep 5


