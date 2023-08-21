from http.server import BaseHTTPRequestHandler, HTTPServer

from pages.loadHomepage import loadHomepage
from pages.loadIndex import loadIndex
from pages.loadSale import loadSale
from pages.loadAddingSale import loadAddingSale

from pages.loadAddingPurchasePlatform import loadAddingPurchasePlatform
from pages.loadAddingSalesPlatform import loadAddingSalesPlatform
from pages.loadPopularPages import loadPopularPages
from pages.loadPopularGames import loadPopularGames

from pages.saveSale import saveSale, savePlatform
from redirect import redirect

import os

routes = [
    '/api/index', 
    '/api/load-sale', 
    '/api/adding-sale', '/api/add-sale', 
    '/api/adding-purchase-platform', '/api/add-purchase-platform', 
    '/api/adding-sales-purchase', 'add-sales-purchase',
    '/api/load-popular-pages', '/api/load-popular-games', 
    ]

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/' or self.path.startswith('/alert'): 
            result = loadIndex('')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))

        elif self.path.startswith('/frontend'):
            file_path = os.path.join(os.path.dirname(__file__), self.path[1:])
            file_path = file_path.replace('\\server', '').replace('/', '\\')
            if os.path.isfile(file_path):
                self.send_response(200)
                if self.path.endswith('.css'): self.send_header('Content-type', 'text/css')
                elif self.path.endswith('.js'): self.send_header('Content-type', 'application/javascript')
                self.end_headers()
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())

        elif self.path in routes:
            if self.path == '/api/index': result = loadHomepage()
            elif self.path == '/api/adding-sale': result = loadAddingSale()
            elif self.path == '/api/load-sale': result = loadSale(False)
            elif self.path == '/api/adding-purchase-platform': result = loadAddingPurchasePlatform()
            elif self.path == '/api/adding-sales-purchase': result = loadAddingSalesPlatform()
            elif self.path == '/api/load-popular-pages': result = loadPopularPages(False)
            elif self.path == '/api/load-popular-games': result = loadPopularGames(False)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))
            
        elif self.path.startswith('/api/adding-sale'): redirect(saveSale(self))
        elif self.path.startswith('/api/add-purchase-platform'): redirect(savePlatform('purchase', self), 'save')
        elif self.path.startswith('/api/add-sales-platform'): redirect(savePlatform('sale', self), 'save')

        elif self.path.startswith('/filtration'):
            if self.path.startswith('/filtration/load-sales-raport'): result = loadIndex(loadSale(self))
            elif self.path.startswith('/filtration/load-popular-pages'): result = loadIndex(loadPopularPages(self))
            elif self.path.startswith('/filtration/load-popular-games'): result = loadIndex(loadPopularPages(self))
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Nie znaleziono strony'.encode('utf-8'))
        
def runServer():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    httpd.serve_forever()

runServer()