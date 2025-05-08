#!/bin/bash


APP_DIR="./app"

echo "Entrando na pasta $APP_DIR"
cd "$APP_DIR" || exit

echo "Encerrando processos antigos..."

fuser -k 8000/tcp
fuser -k 3000/tcp

pkill -f webhook.py
pkill ngrok

echo "Iniciando o servidor FastAPI..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 &

sleep 2

cd ..

sleep 2

echo "Iniciando o ngrok..."
ngrok http 8000 &

echo "Todos os serviços foram iniciados."
