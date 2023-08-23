from urllib.parse import parse_qs, urlparse
import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadPlatforms, loadFilteredSales

def loadSale(self, loadTableExporter):
    filters = {
            'game title': '', 'purchase platform': '', 'sale platform': '', 'min purchase price': '',
            'max purchase price': '', 'min fee': '', 'max fee': '', 'from date': '', 'to date': '',
            'min sell price': '', 'max sell price': '', 'min profit': '', 'max profit': ''
            }
    if self:
        query_params = parse_qs(urlparse(self.path).query)
        filters = {
            'game title': query_params.get('game', [''])[0],
            'purchase platform': query_params.get('purchase-platform', [''])[0],
            'sale platform': query_params.get('sale-platform', [''])[0],
            'min purchase price': query_params.get('min-purchase-price', [''])[0],
            'max purchase price': query_params.get('max-purchase-price', [''])[0],
            'min fee': query_params.get('min-fee', [''])[0],
            'max fee': query_params.get('max-fee', [''])[0],
            'from date': query_params.get('from-date', [''])[0],
            'to date': query_params.get('to-date', [''])[0],
            'min sell price': query_params.get('min-sell-price', [''])[0],
            'max sell price': query_params.get('max-sell-price', [''])[0],
            'min profit': query_params.get('min-profit', [''])[0],
            'max profit': query_params.get('max-profit', [''])[0]
        }

    html = """
            <div class="sales-raport big window">
                <h1>Sprzedaż</h1>
                <h3 onClick="loadFiltersForm()">Filtry v</h3>
                <form action="/filtration-load-sales-raport" onsubmit="return checkForm()" method="get" class="hide">
                    <div class="filters">
                        <div>
                            <label for="game">Gra:</label>
                            <input type="text" id="game" name="game" value="{gameTitle}">
                        </div>
    """.format(gameTitle = filters['game title'])

    purchasePlatforms = loadPlatforms('purchase_platforms')
    html += '<div>'
    html += '<label for="purchase-platform">Platforma zakupu:</label>'
    html += '<select id="purchase-platform" name="purchase-platform">'
    html += '<option value=''></option>'
    for platform in purchasePlatforms: html += f"<option value='{platform['name']}' {'selected' if platform['name'] == filters['purchase platform'] else ''}>{platform['name']}</option>"
    html += '</select></div>'

    salsePlatforms = loadPlatforms('sales_platforms')
    html += '<div>'
    html += '<label for="sale-platform">Platforma sprzedaży:</label>'
    html += '<select id="sale-platform" name="sale-platform">'
    html += '<option value=''></option>'
    for platform in salsePlatforms: html += f"<option value='{platform['name']}' {'selected' if platform['name'] == filters['sale platform'] else ''}>{platform['name']}</option>"
    html += '</select></div>'

    html += """
            <div>
                <label for="purchase-price">Cena zakupu:</label>
                <div class="prices">
                    <input type="number" id="min-purchase-price" name="min-purchase-price" step="0.01" value="{minPurchasePrice}">
                    <span>-</span>
                    <input type="number" id="max-purchase-price" name="max-purchase-price" step="0.01" value="{maxPurchasePrice}">
                </div>
            </div>
            <div>
                <label for="fee">Prowizja:</label>
                <div class="prices">
                    <input type="number" id="min-fee" name="min-fee" step="0.01" value="{minFee}">
                    <span>-</span>
                    <input type="number" id="max-fee" name="max-fee" step="0.01" value="{maxFee}">
                </div>
            </div>
            <div>
                <label for="date">Data:</label>
                <div class="dates">
                    <input type="date" id="from-date" name="from-date" value="{fromDate}">
                    <span>-</span>
                    <input type="date" id="to-date" name="to-date" value="{toDate}">
                </div>
            </div>
            <div>
                <label for="sell-price">Cena sprzedaży:</label>
                <div class="prices">
                    <input type="number" id="min-sell-price" name="min-sell-price" step="0.01" value="{minSellPrice}">
                    <span>-</span>
                    <input type="number" id="max-sell-price" name="max-sell-price" step="0.01" value="{maxSellPrice}">
                </div>
            </div>
            <div>
                <label for="profit">Profit:</label>
                <div class="prices">
                    <input type="number" id="min-profit" name="min-profit" step="0.01" value="{minProfit}">
                    <span>-</span>
                    <input type="number" id="max-profit" name="max-profit" step="0.01" value="{maxProfit}">
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
                <th>Platforma sprzedaży</th>
                <th>Cena zakupu</th>
                <th>Cena sprzedaży</th>
                <th>Prowizja</th>
                <th>Profit</th>
            </tr>
        </thead>
        <tbody>
    """.format(
        minPurchasePrice = filters['min purchase price'],
        maxPurchasePrice = filters['max purchase price'],
        minFee = filters['min fee'],
        maxFee = filters['max fee'],
        fromDate = filters['from date'],
        toDate = filters['to date'],
        minSellPrice = filters['min sell price'],
        maxSellPrice = filters['max sell price'],
        minProfit = filters['min profit'],
        maxProfit = filters['max profit'],
        )
    
    salesSum = {
        'purchase price': 0,
        'sell price': 0,
        'fee': 0,
        'profit': 0
    }

    for sale in loadFilteredSales(filters):
        salesSum['purchase price'] += sale['purchase price']
        salesSum['sell price'] += sale['sell price']
        salesSum['fee'] += sale['fee']
        salesSum['profit'] += sale['profit']
        html += """
                <tr class="sale list">
                    <td class="date">{data}</td>
                    <td class="game-title">{gameTitle}</td>
                    <td class="purchase-platform">{purchasePlatform}</td>
                    <td class="sell-platform">{sellPlatform}</td>
                    <td class="purchase-price">{purchasePrice:.2f}zł</td>
                    <td class="sell-price">{sellPrice:.2f}zł</td>
                    <td class="fee">{fee:.2f}zł</td>
                    <td class="profit">{profit:.2f}zł</td>
                </tr>
        """.format(
            data = sale['date'],
            gameTitle = sale['game title'],
            purchasePlatform = sale['purchase platform'],
            purchasePrice = sale['purchase price'],
            sellPlatform = sale['sell platform'],
            sellPrice = sale['sell price'],
            fee = sale['fee'],
            profit = sale['profit'],
            )
    
    html += """
        </tbody>
            <tfoot>
                <tr class="sale list">
                    <td class="date"></td>
                    <td class="game-title"></td>
                    <td class="purchase-platform"></td>
                    <td class="sell-platform"></td>
                    <td class="purchase-price">{purchasePrice:.2f}zł</td>
                    <td class="sell-price">{sellPrice:.2f}zł</td>
                    <td class="fee">{fee:.2f}zł</td>
                    <td class="profit">{profit:.2f}zł</td>
                </tr>
            </tfoot>
        </table>
    </div>
    """.format(
        purchasePrice = salesSum['purchase price'],
        sellPrice = salesSum['sell price'],
        fee = salesSum['fee'],
        profit = salesSum['profit'],
    )
    
    html += f"</tfoot></table>{loadTableExporter()}</div>"
    return html