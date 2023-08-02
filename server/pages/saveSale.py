from urllib.parse import parse_qs, urlparse

import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import addSale

def saveSale(self):
    query_params = parse_qs(urlparse(self.path).query)
    title = query_params.get('title', [''])[0]
    buyPrice = query_params.get('buy-price', [''])[0]
    sellPrice = query_params.get('sell-price', [''])[0]
    platform = query_params.get('platform', [''])[0]
    alert = f"<h1>Dodano sprzedaz. \nTytul: {title}\nCena zakupu: {buyPrice}\nCena sprzedazy: {sellPrice}\nZarobek: {int(buyPrice) - int(sellPrice)}\nZakupione w: {platform}</h1>"
    
    addSale({'title': title, 'buy price': buyPrice, 'sell price': sellPrice, 'platform': platform})
    
    return {
        'self': self, 
        'page': "/", 
        'alert': alert
    }