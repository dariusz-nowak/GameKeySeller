from urllib.parse import parse_qs, urlparse

import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadPlatforms, loadFilteredSales

def loadSale(self):
    html = """
            <div class="sales-raport big window">
                <h1>Sprzedaż</h1>
                <h3 onClick="loadFiltersForm()">Filtry v</h3>
                <form action="/api/load-sales-raport" onsubmit="return checkForm()" method="get" class="">
                    <div class="filters">
                        <div>
                            <label for="game">Gra:</label>
                            <input type="text" id="game" name="game">
                        </div>
    """

    purchasePlatforms = loadPlatforms('purchase_platforms')
    html += '<div>'
    html += '<label for="purchase-platform">Platforma zakupu:</label>'
    html += '<select id="purchase-platform" name="purchase-platform">'
    html += '<option value=''></option>'
    for platform in purchasePlatforms: html += f"<option value='{platform['name']}'>{platform['name']}</option>"
    html += '</select></div>'

    salsePlatforms = loadPlatforms('sales_platforms')
    html += '<div>'
    html += '<label for="sale-platform">Platforma sprzedaży:</label>'
    html += '<select id="sale-platform" name="sale-platform">'
    html += '<option value=''></option>'
    for platform in salsePlatforms: html += f"<option value='{platform['name']}'>{platform['name']}</option>"
    html += '</select></div>'

    html += """
                        <div>
                            <label for="purchase-price">Cena zakupu:</label>
                            <div class="prices">
                                <input type="number" id="min-purchase-price" name="min-purchase-price" step="0.01">
                                <span>-</span>
                                <input type="number" id="max-purchase-price" name="max-purchase-price" step="0.01">
                            </div>
                        </div>
                        <div>
                            <label for="fee">Prowizja:</label>
                            <div class="prices">
                                <input type="number" id="min-fee" name="min-fee" step="0.01">
                                <span>-</span>
                                <input type="number" id="max-fee" name="max-fee" step="0.01">
                            </div>
                        </div>
                        <div>
                            <label for="date">Data:</label>
                            <div class="dates">
                                <input type="date" id="from-date" name="from-date">
                                <span>-</span>
                                <input type="date" id="to-date" name="to-date">
                            </div>
                        </div>
                        <div>
                            <label for="sell-price">Cena sprzedaży:</label>
                            <div class="prices">
                                <input type="number" id="min-sell-price" name="min-sell-price" step="0.01">
                                <span>-</span>
                                <input type="number" id="max-sell-price" name="max-sell-price" step="0.01">
                            </div>
                        </div>
                        <div>
                            <label for="profit">Profit:</label>
                            <div class="prices">
                                <input type="number" id="min-profit" name="min-profit" step="0.01">
                                <span>-</span>
                                <input type="number" id="max-profit" name="max-profit" step="0.01">
                            </div>
                        </div>
                        <div>
                            <input class="submit" type="submit" value="Filtruj">
                        </div>
                    </div>
                </form>
                <table class="list">
                    <thead>
                        <tr class="header">
                            <th>Data</th>
                            <th>Gra</th>
                            <th>Platforma zakupu</th>
                            <th>Cena zakupu</th>
                            <th>Platforma sprzedaży</th>
                            <th>Cena sprzedaży</th>
                            <th>Prowizja</th>
                            <th>Profit</th>
                        </tr>
                    </thead>
    """

    html += '<tbody>'

    # Pobrać informacje o GET, jeśli jest, wywołać funkcję z filtrami z GET, inaczej wczytać miesiąc bez filtracji

    if self:
        query_params = parse_qs(urlparse(self.path).query)
        filters = {
            'game': query_params.get('game', [''])[0],
            'purchasePlatform': query_params.get('purchase-platform', [''])[0],
            'salePlatform': query_params.get('sale-platform', [''])[0],
            'minPurchasePrice': query_params.get('game', [''])[0],
            'maxPurchasePrice': query_params.get('max-purchase-price', [''])[0],
            'minFee': query_params.get('min-fee', [''])[0],
            'maxFee': query_params.get('max-fee', [''])[0],
            'fromDate': query_params.get('from-date', [''])[0],
            'toDate': query_params.get('to-date', [''])[0],
            'minSellPrice': query_params.get('min-sell-price', [''])[0],
            'maxSellPrice': query_params.get('max-sell-price', [''])[0],
            'minProfit': query_params.get('min-profit', [''])[0],
            'maxProfit': query_params.get('max-profit', [''])[0]
        }
    else:
        filters = {}

    print(loadFilteredSales(filters))

    html += """
                        <tr class="sale list">
                            <td class="date">Data</td>
                            <td class="game-title">Jakaś gra z całkiem długą nazwą</td>
                            <td class="sell-platform">Platforma zakupu</td>
                            <td class="purchase-price">Cena zakupu</td>
                            <td class="purchase-platform">Platforma sprzedaży</td>
                            <td class="sell-price">Cena sprzedaży</td>
                            <td class="fee">Prowizja</td>
                            <td class="profit">Profit</td>
                        </tr>
                    </tbody>
                </table>
            </div>
    """
    
    return html