from urllib.parse import parse_qs, urlparse

import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import addSale, addPurchasePlatform, addSalesPlatform

def savePlatform(platform, self): 
    query_params = parse_qs(urlparse(self.path).query)
    platformTitle = query_params.get('platform', [''])[0]
    alert = f"<h1>Dodano platformę {'zakupu' if platform == 'purchase' else 'sprzedaży'}: {platformTitle}</h1>"

    addPurchasePlatform({'platform': platformTitle}) if platform == 'purchase' else addSalesPlatform({'platform': platformTitle})
    
    return {
        'self': self, 
        'page': "/", 
        'alert': alert
    }

def redirect(data):
    url = f"{data['page']}?alert={str(data['alert']).encode('latin-1')}"
    data['self'].send_response(302)
    data['self'].send_header('Content-type', 'text/html')
    data['self'].send_header('Location', url)
    data['self'].end_headers()



redirect(savePlatform('sale', self))