def loadAddingPurchasePlatform():
    return """
        <div class="add-purchase-platform window">
            <h1>Dodaj platformę zakupu</h1>
            <form action="/api/add-purchase-platform" onsubmit="return checkForm()" method="get" class="list">
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