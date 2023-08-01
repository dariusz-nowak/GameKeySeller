from http.server import BaseHTTPRequestHandler, HTTPServer

def run_python_script():
    # Tutaj można umieścić dowolny kod Pythona, który chcesz wykonać po stronie serwera
    result = str(float(1 + 32))
    return result

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/backend/server/server_script':
            result = run_python_script()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Nie znaleziono strony')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print('Serwer działa na porcie 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()