def loadAddingSalesPlatform():
    return """
        <div class="add-sales-platform window">
            <h1>Dodaj platformę sprzedaży</h1>
            <form action="/api/add-sales-platform" onsubmit="return checkForm()" method="get" class="list">
                <div>
                    <label for="platform">Platforma:</label>
                    <input type="text" id="platform" name="platform">
                </div>
                <div>
                    <input class="submit" type="submit" value="Dodaj">
                </div>
            </form>
        </div>
    """