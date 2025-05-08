from fastapi import FastAPI, Request, Response
import subprocess
import os
import signal

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is Ok funciona Logo!"}

@app.post("/webhook")
async def webhook(request: Request):
    print("✅ Webhook recebido. Executando git pull...")

    try:
        # Executando o comando git pull
        output = subprocess.check_output(['git', '-C', os.getcwd(), 'pull'], stderr=subprocess.STDOUT)
        print("📦 Git pull output:\n", output.decode())

        print("♻️ Reiniciando o servidor FastAPI...")

        # Encontrando processos uvicorn em execução
        try:
            result = subprocess.check_output(["pgrep", "-f", "uvicorn"])
            # Matar os processos encontrados
            for pid in result.decode().split():
                os.kill(int(pid), signal.SIGTERM)
            print("🛑 Processos 'uvicorn' encerrados.")
        except subprocess.CalledProcessError:
            print("⚠️ Nenhum processo 'uvicorn' encontrado.")

        # Reiniciando o servidor FastAPI
        subprocess.Popen(
            ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"],
            cwd=os.getcwd()  # Certificando-se de que está no diretório correto
        )

        return Response(content="Success and restarted!", status_code=200)

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao atualizar ou reiniciar:\n", e.output.decode())
        return Response(content="Git pull or restart failed", status_code=500)
    except Exception as e:
        print("❌ Erro desconhecido:\n", str(e))
        return Response(content="Unknown error occurred", status_code=500)
