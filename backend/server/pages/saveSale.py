from urllib.parse import parse_qs, urlparse

def saveSale(self):
    query_params = parse_qs(urlparse(self.path).query)
    title = query_params.get('title', [''])[0]
    buyPrice = query_params.get('buy-price', [''])[0]
    sellPrice = query_params.get('sell-price', [''])[0]
    platform = query_params.get('platform', [''])[0]
    
    return f'Dodano sprzedaż: {title} kupione za {buyPrice} z platformy {platform} za cenę: {sellPrice}'