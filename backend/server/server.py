from http.server import BaseHTTPRequestHandler, HTTPServer
from pages.loadIndex import loadIndex
from pages.loadAddingSale import loadAddingSale
from pages.saveSale import saveSale
from urllib.parse import parse_qs, urlparse

routes = ['/api/index', '/api/adding-sale', '/api/add-sale']

def run_python_script():
    # Tutaj można umieścić dowolny kod Pythona, który chcesz wykonać po stronie serwera
    result = str(float(1 + 32))
    return result

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path.startswith('/api/adding-sale'))
        print(self.path)
        print(parse_qs(urlparse(self.path).query))
        if self.path in routes:
            if self.path == '/api/index': result = loadIndex()
            elif self.path == '/api/adding-sale': result = loadAddingSale()
            elif self.path.startswith('/api/adding-sale'): result = saveSale(self)
            
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
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    httpd.serve_forever()

run_server()