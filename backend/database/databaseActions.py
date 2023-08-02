from sqlite3 import connect

connection = connect("backend/database/sql.db")
cursor = connection.cursor()

now = "strftime('%Y-%m-%d %H:%M:%S','now', '+2 hours')"

def addGame(game):
    title = game['title'].replace('\'', '`')
    cursor.execute(f"INSERT INTO games VALUES(null, '{title}', {game['old price']}, {game['current price']}, '{game['store']}', '{game['status']}', {now}, {now})")
    connection.commit()

def editGame(game):
    cursor.execute(f"UPDATE games SET old_price = {game['old price']}, current_price = {game['current price']}, status = '{game['status']}', time_modyfied = {now} WHERE id = {game['id']}")
    connection.commit()

def removeGame(gameID, title):
    cursor.execute(f"DELETE FROM games WHERE id = {gameID}")
    cursor.execute(f"INSERT INTO games_to_repair VALUES(null, '{title}')")
    connection.commit()

def loadGamesList():
    gamesFromDB = cursor.execute("SELECT * FROM games").fetchall()
    gamesList = []
    for game in gamesFromDB:
        gamesList.append({
            'id': game[0],
            'title': game[1],
            'old price': game[2],
            'current price': game[3],
            'store': game[4],
            'status': game[5],
        })
    return gamesList

def editGamesList(gamesList):
    for game in gamesList:
        if game['status'] == 'new': addGame(game)
        elif game['status'] in ['different price', 'no changes']: editGame(game)
        elif game['status'] == 'deleted': removeGame(game['id'], game['title'])

    return gamesList

def getAdvertID(gameID):
    return cursor.execute(f"SELECT id FROM adverts WHERE game_id = {gameID}")

def addAdvert(advert):
    title = advert['title'].replace('\'', '`')
    cursor.execute(f"INSERT INTO adverts VALUES(null, {advert['game id']}, '{title}', '{advert['image']}', {advert['price']}, '{advert['url']}')")
    connection.commit()

def editAdvert(advert):
    cursor.execute(f"UPDATE adverts SET price = {advert['price']} WHERE id = {advert['id']}")
    connection.commit()

def removeAdvert(advertID):
    cursor.execute(f"DELETE FROM adverts WHERE id = {advertID}")
    connection.commit()

def addSale(sale):
    cursor.execute(f"INSERT INTO sales VALUES(null, '{sale['title']}', {sale['buy price']}, {sale['sell price']}, '{sale['platform']}', {now})")
    connection.commit()

def loadMonthSales():
    sales = cursor.execute("SELECT title, sell_price, time_created, platform FROM sales WHERE time_created >= strftime('%Y-%m','now') ORDER BY time_created DESC").fetchall()
    salesList = []
    for sale in sales:
        salesList.append({
            'title': sale[0],
            'sell price': sale[1],
            'month': int(sale[2][5:7]),
            'day': int(sale[2][8:10]),
            'platform': sale[3]
        })
    return salesList

def loadPopularSales(type):
    sales = cursor.execute(f"SELECT {type}, COUNT({type}) FROM sales GROUP BY {type} ORDER BY COUNT({type}) DESC LIMIT 10").fetchall()
    salesList = []
    for sale in sales:
        salesList.append({
            'title': sale[0],
            'count': sale[1]
        })
    return salesList