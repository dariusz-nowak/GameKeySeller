from sqlite3 import connect
from ast import literal_eval

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
    gamesList = []
    gamesFromDB = cursor.execute("SELECT * FROM games").fetchall()

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
        elif game['status'] == 'deleted': removeGame(game['id'])

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