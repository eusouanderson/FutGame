from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/':  # aceita POST em "/"
            print("🚀 Recebido push do GitHub! Atualizando código...")
            try:
                output = subprocess.check_output(['git', '-C', './app', 'pull', 'origin', 'main'], stderr=subprocess.STDOUT)
                print("✅ Atualização feita com sucesso:\n", output.decode())
            except subprocess.CalledProcessError as e:
                print("❌ Erro ao executar git pull:\n", e.output.decode())
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Atualizado com sucesso')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

if __name__ == "__main__":
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, WebhookHandler)
    print("📡 Webhook escutando na porta 3000...")
    httpd.serve_forever()
