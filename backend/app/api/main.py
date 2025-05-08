import time
import subprocess
import os
from fastapi import FastAPI, Request, Response, BackgroundTasks

app = FastAPI()

DEPLOY_SCRIPT = "/app/deploy.sh"  # ou o caminho para o seu script

def run_deploy():
    try:
        # 1) git pull
        output = subprocess.check_output(
            ["git", "-C", os.getcwd(), "pull"],
            stderr=subprocess.STDOUT
        )
        print("📦 Git pull output:\n", output.decode())

        # 2) docker-compose pull + up
        # -- Assumindo que docker-compose.yml está em /app
        dc_cmd = ["docker-compose", "-f", os.path.join(os.getcwd(), "docker-compose.yml"),
                  "up", "-d", "--build"]
        output = subprocess.check_output(dc_cmd, stderr=subprocess.STDOUT)
        print("🐳 docker-compose output:\n", output.decode())

    except subprocess.CalledProcessError as e:
        print("❌ Erro no deploy:\n", e.output.decode())
        raise
    except Exception as e:
        print("❌ Erro desconhecido no deploy:\n", str(e))
        raise

@app.get("/")
async def root():
    return {"message": "Server is running successfully!"}

@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    print("✅ Webhook recebido. Iniciando atualização...")

    background_tasks.add_task(run_deploy)

    return Response(content="Deploy agendado", status_code=202)
