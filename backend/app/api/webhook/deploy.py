import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)

DEPLOY_SCRIPT = "/app/deploy.sh"


def run_deploy():
    if os.path.exists(DEPLOY_SCRIPT):
        logging.info(f"🎯 Executando o script de deploy: {DEPLOY_SCRIPT}")
        try:
            subprocess.check_call([DEPLOY_SCRIPT])
            logging.info("🚀 Script de deploy executado com sucesso.")
        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Erro ao executar o script de deploy: {e}")
            raise
    else:
        logging.warning(f"⚠️ O script de deploy {DEPLOY_SCRIPT} não foi encontrado.")

    try:
        logging.info("🔄 Atualizando o repositório com git pull...")
        output = subprocess.check_output(
            ["git", "-C", os.getcwd(), "pull"], stderr=subprocess.STDOUT
        )
        logging.info("📦 Git pull output:\n" + output.decode())

        dc_cmd = [
            "docker-compose",
            "-f",
            os.path.join(os.getcwd(), "docker-compose.yml"),
            "up",
            "-d",
            "--build",
        ]
        logging.info("🐳 Iniciando containers Docker com docker-compose...")
        output = subprocess.check_output(dc_cmd, stderr=subprocess.STDOUT)
        logging.info("🐳 docker-compose output:\n" + output.decode())

    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Erro no deploy:\n{e.output.decode()}")
        raise
    except Exception as e:
        logging.error(f"❌ Erro desconhecido no deploy:\n{str(e)}")
        raise
