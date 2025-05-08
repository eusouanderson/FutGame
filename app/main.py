import time
from fastapi import FastAPI, Request, Response
import subprocess
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is Ok funciona Sera HOJE MESMO? Acho que não!"}

@app.post("/webhook")
async def webhook(request: Request):
    print("✅ Webhook recebido. Executando git pull...")

    try:
        output = subprocess.check_output(['git', '-C', os.getcwd(), 'pull'], stderr=subprocess.STDOUT)
        print("📦 Git pull output:\n", output.decode())

        print("⏳ Aguardando para garantir que as alterações sejam aplicadas...")
        time.sleep(3)

        print("♻️ Reiniciando o servidor FastAPI com o script de reinício...")

        restart_script_path = "/root/projetos/FutGame/restart.sh"
        result = subprocess.run(['bash', restart_script_path], text=True, capture_output=True)


        if result.returncode != 0:
            print(f"❌ Erro ao reiniciar servidor. Código de erro: {result.returncode}")
            print(f"Detalhes do erro: {result.stderr}")
            return Response(content="Falha ao reiniciar o servidor", status_code=500)

        print("✅ Servidor reiniciado com sucesso.")

        return Response(content="Success and restarted!", status_code=200)

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao executar git pull:\n", e.output.decode())
        return Response(content="Erro ao atualizar o código", status_code=500)
    except Exception as e:
        print("❌ Erro desconhecido:\n", str(e))
        return Response(content="Erro desconhecido", status_code=500)
