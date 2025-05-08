from fastapi import FastAPI, Request, Response
import subprocess
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is Ok funciona Bora !"}

@app.post("/webhook")
async def webhook(request: Request):
    print("✅ Webhook recebido. Executando git pull...")

    try:
        # Executando o comando git pull
        output = subprocess.check_output(['git', '-C', os.getcwd(), 'pull'], stderr=subprocess.STDOUT)
        print("📦 Git pull output:\n", output.decode())

        print("♻️ Reiniciando o servidor FastAPI com o script de reinício...")

        # Definindo o caminho absoluto do script restart.sh
        restart_script_path = os.path.join(os.getcwd(), 'restart.sh')

        # Verificando se o script existe
        if not os.path.exists(restart_script_path):
            return Response(content="Erro: O script 'restart.sh' não foi encontrado.", status_code=500)

        # Garantindo que o script tenha permissões de execução
        os.chmod(restart_script_path, 0o755)

        # Chama o script restart.sh para reiniciar o servidor
        subprocess.Popen(['bash', restart_script_path], cwd=os.getcwd())

        return Response(content="Success and restarted!", status_code=200)

    except subprocess.CalledProcessError as e:
        print("❌ Erro ao atualizar ou reiniciar:\n", e.output.decode())
        return Response(content="Git pull or restart failed", status_code=500)
    except Exception as e:
        print("❌ Erro desconhecido:\n", str(e))
        return Response(content="Unknown error occurred", status_code=500)
