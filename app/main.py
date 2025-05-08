from fastapi import FastAPI, Request, Response
import subprocess
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is Ok funciona PORRA!"}

@app.post("/webhook")
async def webhook(request: Request):
    print("✅ Webhook recebido. Executando git pull...")

    try:
        # Executando o comando git pull
        output = subprocess.check_output(['git', '-C', os.getcwd(), 'pull'], stderr=subprocess.STDOUT)
        print("📦 Git pull output:\n", output.decode())

        print("♻️ Reiniciando o servidor FastAPI com o script de reinício...")

        # Chama o script restart.sh para reiniciar o servidor
        subprocess.Popen(['bash', 'restart.sh'], cwd=os.getcwd())

        return Response(content="Success and restarted!", status_code=200)

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao atualizar ou reiniciar:\n", e.output.decode())
        return Response(content="Git pull or restart failed", status_code=500)
    except Exception as e:
        print("❌ Erro desconhecido:\n", str(e))
        return Response(content="Unknown error occurred", status_code=500)
