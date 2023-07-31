from sqlite3 import connect

connection = connect("backend/database/sql.db")
cursor = connection.cursor()

def addGame(game):
    title = game['title'].replace('\'', '`')
    cursor.execute(f"INSERT INTO games VALUES(null, '{title}', {game['old price']}, {game['current price']}, '{game['store']}', '{game['status']}', strftime('%Y-%m-%d %H-%M-%S','now'), strftime('%Y-%m-%d %H-%M-%S','now'))")
    connection.commit()

def editGame(game):
    cursor.execute(f"UPDATE games SET old_price = {game['old price']}, current_price = {game['current price']}, status = '{game['status']}', time_modyfied = strftime('%Y-%m-%d %H-%M-%S','now') WHERE id = {game['id']}")
    connection.commit()

def removeGame(gameID):
    cursor.execute(f"DELETE FROM games WHERE id = {gameID}")
    connection.commit()

def loadGamesListFromDB():
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

def editGamesListInDB(gamesList):
    for game in gamesList:
        if game['status'] == 'new': addGame(game)
        elif game['status'] in ['different price', 'no changes']: editGame(game)
        elif game['status'] == 'deleted': removeGame(game['id'])

    return gamesList