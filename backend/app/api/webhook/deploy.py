import os
import subprocess

DEPLOY_SCRIPT = "/app/deploy.sh"


def run_deploy():
    try:
        output = subprocess.check_output(
            ["git", "-C", os.getcwd(), "pull"], stderr=subprocess.STDOUT
        )
        print("📦 Git pull output:\n", output.decode())

        dc_cmd = [
            "docker-compose",
            "-f",
            os.path.join(os.getcwd(), "docker-compose.yml"),
            "up",
            "-d",
            "--build",
        ]
        output = subprocess.check_output(dc_cmd, stderr=subprocess.STDOUT)
        print("🐳 docker-compose output:\n", output.decode())

    except subprocess.CalledProcessError as e:
        print("❌ Erro no deploy:\n", e.output.decode())
        raise
    except Exception as e:
        print("❌ Erro desconhecido no deploy:\n", str(e))
        raise
