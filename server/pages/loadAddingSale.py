import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadPlatforms

def loadAddingSale():
    html = """
    <div class="adding-sale window">
        <h1>Dodaj sprzedaż</h1>
        <form action="/api/adding-sale" onsubmit="return checkForm()" method="get" class="list">
            <div>
                <label for="title">Tytuł:</label>
                <input type="text" id="title" name="title">
            </div>
            <div>
                <label for="date">Data:</label>
                <input type="date" id="date" name="date">
            </div>
            <div>
                <label for="buy-price">Cena zakupu:</label>
                <input type="number" id="buy-price" name="buy-price" step="0.01">
            </div>
            <div>
                <label for="sell-price">Cena sprzedaży:</label>
                <input type="number" id="sell-price" name="sell-price" step="0.01">
            </div>
            <div>
                <label for="fee">Prowizja:</label>
                <input type="number" id="fee" name="fee" step="0.01">
            </div>
    """
    purchasePlatforms = loadPlatforms('purchase_platforms')
    html += '<div>'
    html += '<label for="purchase-platform">Platforma zakupu:</label>'
    html += '<select id="purchase-platform" name="purchase-platform">'
    for platform in purchasePlatforms: html += f"<option value='{platform['name']}'>{platform['name']}</option>"
    html += '</select></div>'

    salsePlatforms = loadPlatforms('sales_platforms')
    html += '<div>'
    html += '<label for="sale-platform">Platforma sprzedaży:</label>'
    html += '<select id="sale-platform" name="sale-platform">'
    for platform in salsePlatforms: html += f"<option value='{platform['name']}'>{platform['name']}</option>"
    html += '</select></div>'
    
    html += """
            <div>
                <input class="submit" type="submit" value="Dodaj">
            </div>
        </form>
    </div>
    """

    return html