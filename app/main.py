from fastapi import FastAPI, Request, Response
import subprocess
import os
import signal

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is Ok testando!"}


@app.post("/webhook")
async def webhook(request: Request):

    print("✅ Webhook recebido. Executando git pull...")

    try:
        output = subprocess.check_output(['git', '-C', os.getcwd(), 'pull'], stderr=subprocess.STDOUT)

        print("📦 Git pull output:\n", output.decode())

        print("♻️ Reiniciando o servidor FastAPI...")

        result = subprocess.check_output(["pgrep", "-f", "uvicorn"])
        for pid in result.decode().split():
            os.kill(int(pid), signal.SIGTERM)

        subprocess.Popen(
    ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"],
    cwd="."  # ou simplesmente remova o argumento cwd
)


        return Response(content="Success and restarted!", status_code=200)

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao atualizar ou reiniciar:\n", e.output.decode())
        return Response(content="Git pull or restart failed", status_code=500)
    except Exception as e:
        print("❌ Erro desconhecido:\n", str(e))
        return Response(content="Unknown error occurred", status_code=500)
