def loadIndex(content):
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Panel zarządzania</title>

            <link rel="stylesheet" href="frontend/css/style.css">
            
            <script src="frontend/javascript/jspdf.js"></script>
            <script src="frontend/javascript/jspdf.autotable.js"></script>
            <script src="frontend/javascript/RobotoMono-VariableFont_wght-normal.js"></script>
        </head>
        <body>
            <div class="content">
                <div class="panel">
                    <div class="list">
                        <h2>Raporty</h2>
                        <ul>
                            <li onclick="loadPage('index')">Strona główna</li>
                            <li class="todo">Oferty</li>
                            <li onclick="loadPage('load-sale')">Sprzedaż</li>
                        </ul>
                    </div>
                    <div class="list">
                        <h2>Statystyki</h2>
                        <ul>
                            <li onclick="loadPage('load-popular-pages')">Popularne strony</li>
                            <li onclick="loadPage('load-popular-games')">Popularne gry</li>
                        </ul>
                    </div>
                    <div class="separate"></div>
                    <div class="list">
                        <h2>Działania</h2>
                        <ul>
                            <li onclick="loadPage('adding-sale')">Dodaj sprzedaż</li>
                            <li onclick="loadPage('adding-purchase-platform')">Dodaj platformę zakupu</li>
                            <li onclick="loadPage('adding-sales-purchase')">Dodaj platformę sprzedaży</li>
                        </ul>
                    </div>
                </div>
                <div class="container">
                {containerContent}
                </div>
            </div>
            <div class="scripts">
                <script src="frontend/javascript/alerts.js"></script>
                <script src="frontend/javascript/main.js"></script>
            </div>
        </body>
        </html>
    """.format(containerContent = content)