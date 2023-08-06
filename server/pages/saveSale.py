from urllib.parse import parse_qs, urlparse

import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import addSale, addPurchasePlatform, addSalesPlatform

def saveSale(self):
    query_params = parse_qs(urlparse(self.path).query)
    title = query_params.get('title', [''])[0]
    date = query_params.get('date', [''])[0]
    buyPrice = query_params.get('buy-price', [''])[0]
    sellPrice = query_params.get('sell-price', [''])[0]
    fee = query_params.get('fee', [''])[0]
    purchasePlatform = query_params.get('purchase-platform', [''])[0]
    salesPlatform = query_params.get('sale-platform', [''])[0]
    alert = f"<h1>Dodano sprzedaz. \nTytul: {title}\nCena zakupu: {buyPrice}\nCena sprzedazy: {sellPrice}\nZarobek: {float(buyPrice) - float(sellPrice)}\nZakupione w: {purchasePlatform}\n Sprzedane w: {salesPlatform}</h1>"

    addSale({'title': title, 'buy price': buyPrice, 'sell price': sellPrice, 'fee': fee, 'purchase platform': purchasePlatform, 'sale platform': salesPlatform, 'date': date})
    
    return {
        'self': self, 
        'page': "/alert", 
        'alert': alert
    }

def savePlatform(platform, self): 
    query_params = parse_qs(urlparse(self.path).query)
    platformTitle = query_params.get('platform', [''])[0]
    alert = f"<h1>Dodano platforme {'zakupu' if platform == 'purchase' else 'sprzedazy'}: {platformTitle}</h1>"

    addPurchasePlatform({'platform': platformTitle}) if platform == 'purchase' else addSalesPlatform({'platform': platformTitle})
    
    return {
        'self': self, 
        'page': "/alert",
        'alert': alert
    }