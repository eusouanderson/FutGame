#!/bin/bash
echo "🔴 Parando servidor existente..."
pkill -f "uvicorn" 2>/dev/null

echo "🔄 Iniciando servidor FastAPI..."

cd app || { echo "❌ Não foi possível entrar na pasta 'app'."; exit 1; }

echo "📂 Entrando na pasta $PWD"

echo "🚀 Iniciando o servidor FastAPI..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 > ../server.log 2>&1 &

echo "✅ Servidor iniciado. Verifique 'server.log' para detalhes."
