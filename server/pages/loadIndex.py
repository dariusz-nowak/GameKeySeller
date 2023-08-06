def loadIndex():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Panel zarządzania</title>

            <link rel="stylesheet" href="frontend/css/style.css">
        </head>
        <body>
            <div class="content">
                <div class="panel">
                    <div class="list">
                        <h2>Raporty</h2>
                        <ul>
                            <li onclick="loadPage('index')">Strona główna</li>
                            <!-- Sprzedaż per kraj lub świat oraz per gra/gry oraz per czas-->
                            <li class="todo" onclick="loadPage('load-sale')">Sprzedaż</li>
                            <!-- Zakup per gra/gry oraz per czas -->
                            <li class="todo">Zakup</li>
                        </ul>
                    </div>
                    <div class="list">
                        <h2>Statystyki</h2>
                        <ul>
                            <!-- Popularność stron zakupowych per kraj lub świat oraz per czas -->
                            <li class="todo">Popularne strony</li>
                            <!-- Popularność gier per kraj lub świat oraz per czas -->
                            <li class="todo">Popularne gry</li>
                        </ul>
                    </div>
                    <div class="list">
                        <h2>Oferty</h2>
                        <ul>
                            <!-- Dodać wszystkie dostępne kraje sprzedaży OLX w widoku OLX/ALLEGRO -->
                            <li class="todo">OLX</li>
                            <li class="todo">ALLEGRO</li>
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
                </div>
            </div>
            <div class="scripts">
                <script src="frontend/javascript/main.js"></script>
            </div>
        </body>
        </html>
    """