def loadSale():
    return """
            <div class="sales-raport big window">
                <h1>Sprzedaż</h1>
                <h3 onClick="loadFiltersForm()">Filtry v</h3>
                <form action="" method="get" class="hide">
                    <div class="filters">
                        <div>
                            <label for="game">Gra:</label>
                            <input type="text" id="game" name="game">
                        </div>
                        <div>
                            <label for="purchase-platform">Platforma zakupu:</label>
                            <select id="purchase-platform" name="purchase-platform">
                                <option value=''></option>
                                <option value='xxx'>xxx</option>
                                <option value='xxx'>xxx</option>
                                <option value='xxx'>xxx</option>
                            </select>
                        </div>
                        <div>
                            <label for="sale-platform">Platforma sprzedaży:</label>
                            <select id="sale-platform" name="sale-platform">
                                <option value=''></option>
                                <option value='xxx'>xxx</option>
                                <option value='xxx'>xxx</option>
                                <option value='xxx'>xxx</option>
                            </select>
                        </div>
                        <div>
                            <label for="date">Data:</label>
                            <div class="dates">
                                <span>Od:</span><input type="date" id="date" name="date">
                                <span>Do:</span><input type="date" id="date" name="date">
                            </div>
                        </div>
                        <div>
                            <label for="purchase-price">Cena zakupu:</label>
                            <input type="number" id="purchase-price" name="purchase-price" step="0.01">
                        </div>
                        <div>
                            <label for="sell-price">Cena sprzedaży:</label>
                            <input type="number" id="sell-price" name="sell-price" step="0.01">
                        </div>
                        <div>
                            <label for="fee">Prowizja:</label>
                            <input type="number" id="fee" name="fee" step="0.01">
                        </div>
                        <div>
                            <label for="profit">Profit:</label>
                            <input type="number" id="profit" name="profit" step="0.01">
                        </div>
                        <div>
                            <input class="submit" type="submit" value="Szukaj">
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
                    <tbody>
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