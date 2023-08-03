from http.server import BaseHTTPRequestHandler, HTTPServer

from pages.loadIndex import loadIndex
from pages.loadAddingSale import loadAddingSale
from pages.saveSale import saveSale
from redirect import redirect

import os
import signal

serverDown = False
routes = ['/api/index', '/api/adding-sale', '/api/add-sale']

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in routes:
            if self.path == '/api/index': result = loadIndex()
            elif self.path == '/api/adding-sale': result = loadAddingSale()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))
            
        elif self.path.startswith('/api/adding-sale'): redirect(saveSale(self))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Nie znaleziono strony')

def runServer():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    httpd.serve_forever()

runServer()