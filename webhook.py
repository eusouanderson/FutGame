from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os
import signal

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/':
            print("✅ Webhook recebido. Executando git pull...")
            try:
                # Atualiza o repositório
                output = subprocess.check_output(['git', '-C', './app', 'pull'], stderr=subprocess.STDOUT)
                print("📦 Git pull output:\n", output.decode())

                # Reinicia o servidor (procura pelo processo do uvicorn)
                print("♻️ Reiniciando o servidor FastAPI...")
                result = subprocess.check_output(["pgrep", "-f", "uvicorn"])
                for pid in result.decode().split():
                    os.kill(int(pid), signal.SIGTERM)

                # Reinicia o servidor novamente (ajuste se você usa systemd ou supervisord)
                subprocess.Popen(["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"], cwd="./app")

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Success and restarted')
            except subprocess.CalledProcessError as e:
                print("❌ Erro ao atualizar ou reiniciar:\n", e.output.decode())
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'Git pull or restart failed')
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, WebhookHandler)
    print("📡 Webhook escutando na porta 3000...")
    httpd.serve_forever()
