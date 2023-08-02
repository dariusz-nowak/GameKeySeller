def loadAddingSale():
    return """
        <div class="adding-sale">
            <h1>Dodawanie sprzedaży</h1>
            <form action="/api/adding-sale" onsubmit="return checkForm()" method="get">
                <div>
                    <label for="title">Title:</label>
                    <input type="text" id="title" name="title">
                </div>
                <div>
                    <label for="buy-price">Buy price:</label>
                    <input type="number" id="buy-price" name="buy-price">
                </div>
                <div>
                    <label for="sell-price">Sell price:</label>
                    <input type="number" id="sell-price" name="sell-price">
                </div>
                <div>
                    <label for="platform">Platform:</label>
                    <input type="text" id="platform" name="platform">
                </div>
                <input class="submit" type="submit" value="Send">
            </form>
        </div>
    """