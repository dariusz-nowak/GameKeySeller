from urllib.parse import parse_qs, urlparse

import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadPlatforms, loadFilteredPopularGames

def loadPopularGames(self):
    filters = {
        'game title': '',
        'purchase platform': '', 'sale platform': '',
        'min keys sold': '', 'max keys sold': '', 
        'from date': '', 'to date': '',
    }

    if self:
        query_params = parse_qs(urlparse(self.path).query)
        filters = {
            'game title': query_params.get('game', [''])[0],
            'purchase platform': query_params.get('purchase-platform', [''])[0],
            'sale platform': query_params.get('sale-platform', [''])[0],
            'min keys sold': query_params.get('min-keys-sold', [''])[0],
            'max keys sold': query_params.get('max-keys-sold', [''])[0],
            'from date': query_params.get('from-date', [''])[0],
            'to date': query_params.get('to-date', [''])[0],
        }

    html = """
            <div class="popular-pages-raport big window">
                <h1>Popularne gry</h1>
                <h3 onclick="loadPopularPagesFilterForm()">Filtry v</h3>
                <form action="/filtration/load-popular-games" onsubmit="" class="hide">
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
                            <label for="keys-sold">Ilość kluczy:</label>
                            <div class="prices">
                                <input type="number" id="min-keys-sold" name="min-keys-sold" value="{minKeysSold}">
                                <span>-</span>
                                <input type="number" id="max-keys-sold" name="max-keys-sold" value="{maxKeysSold}">
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
                            <input class="submit" type="submit" value="Filtruj">
                        </div>
                    </div>
                </form>
                <table class="list">
                    <thead>
                        <tr class="header">
                            <th>Gra</th>
                            <th>Platforma zakupu</th>
                            <th>Platforma sprzedaży</th>
                            <th>Data ostatniego zakupu</th>
                            <th>Ilość sprzedanych kluczy</th>
                        </tr>
                    </thead>
                    <tbody>
    """.format(
        minKeysSold = filters['min keys sold'],
        maxKeysSold = filters['max keys sold'],
        fromDate = filters['from date'],
        toDate = filters['to date'],
    )
    
    for game in loadFilteredPopularGames(filters):
        html += """
                <tr class="popular-pages list">
                    <td class="game">{gameTitle}</td>
                    <td class="purchase-platform">{purchasePlatform}</td>
                    <td class="sell-platform">{sellPlatform}</td>
                    <td class="date">{latestDate}</td>
                    <td class="keys-sold">{keysSold}</td>
                </tr>
        """.format(
            gameTitle = game['game title'],
            purchasePlatform = game['purchase platform'],
            sellPlatform = game['sell platform'],
            latestDate = game['latest date'],
            keysSold = game['keys sold'],
            )
                    
    html += '</tbody></table></div>'
    return html