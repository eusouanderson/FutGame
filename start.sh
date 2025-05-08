#!/bin/bash

# Caminho do app
APP_DIR="./app"

echo "Entrando na pasta $APP_DIR"
cd "$APP_DIR" || exit

echo "Encerrando processos antigos..."
# Mata processos que estão usando as portas 8000 e 3000
fuser -k 8000/tcp
fuser -k 3000/tcp
# Mata o processo do webhook e ngrok, se estiverem em execução
pkill -f webhook.py
pkill ngrok

# Inicia o servidor FastAPI
echo "Iniciando o servidor FastAPI..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 &

# Aguarda o servidor iniciar
sleep 2

# Volta para a raiz do projeto
cd ..

# Inicia o webhook listener na porta 3000
echo "Iniciando webhook listener na porta 3000..."
poetry run python3 webhook.py &

# Aguarda o webhook iniciar
sleep 2

# Inicia o ngrok com apenas um túnel para a porta 8000 em segundo plano
echo "Iniciando o ngrok..."
ngrok http 8000 &

echo "Todos os serviços foram iniciados."
