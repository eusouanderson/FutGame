from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Atualizando projeto FutGame...')

        print("🚀 Recebido push do GitHub! Executando git pull...")

        try:
            result = subprocess.run(
                ["git", "-C", "./app", "pull", "origin", "main"],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ Atualização concluída:\n", result.stdout)
        except subprocess.CalledProcessError as e:
            print("❌ Erro ao atualizar o repositório:\n", e.stderr)

    def log_message(self, format, *args):
        return  # Oculta logs padrão do HTTPServer

if __name__ == "__main__":
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, WebhookHandler)
    print("📡 Webhook escutando na porta 3000...")
    httpd.serve_forever()
