import time
from fastapi import FastAPI, Request, Response
import subprocess
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is runing"}

@app.post("/webhook")
async def webhook(request: Request):
    print("✅ Webhook recebido. Executando git pull...")

    try:
        output = subprocess.check_output(['git', '-C', os.getcwd(), 'pull'], stderr=subprocess.STDOUT)
        print("📦 Git pull output:\n", output.decode())

        print("⏳ Aguardando para garantir que as alterações sejam aplicadas...")
        time.sleep(3)

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao executar git pull:\n", e.output.decode())
        return Response(content="Erro ao atualizar o código", status_code=500)
    except Exception as e:
        print("❌ Erro desconhecido:\n", str(e))
        return Response(content="Erro desconhecido", status_code=500)
    print("✅ Atualização concluída com sucesso.")
    return Response(content="Atualização concluída com sucesso", status_code=200)
