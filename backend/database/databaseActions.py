from sqlite3 import connect
from datetime import datetime
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
    title = title.replace('\'', '`')
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
    cursor.execute(f"INSERT INTO sales VALUES(null, '{sale['title']}', {sale['buy price']}, {sale['sell price']}, {sale['fee']}, '{sale['purchase platform']}', '{sale['sale platform']}', '{sale['date']}')")
    connection.commit()

def loadMonthSales():
    sales = cursor.execute("SELECT title, sell_price, buy_price, fee, sell_platform, time_created FROM sales WHERE time_created >= strftime('%Y-%m-%d', 'now', '-31 days') AND time_created <= strftime('%Y-%m-%d', 'now') ORDER BY time_created DESC").fetchall()
    salesList = []
    for sale in sales:
        salesList.append({
            'title': sale[0],
            'profit': sale[1] - sale[2] - sale[3],
            'platform': sale[4],
            'day': sale[5][8:10],
            'month': sale[5][5:7]
        })
    return salesList

def loadPopularSales(type):
    sales = cursor.execute(f"SELECT {type}, COUNT({type}) FROM sales GROUP BY {type} ORDER BY COUNT({type}) DESC LIMIT 5").fetchall()
    salesList = []
    for sale in sales:
        salesList.append({
            'title': sale[0],
            'count': sale[1]
        })
    return salesList

def loadFilteredSales(filters):
    filtration = False
    for filter in filters.values():
        if filter: filtration = True

    query = "SELECT * FROM sales WHERE"
    
    if filtration:
        if filters['from date'] or filters['to date']: 
            if filters['from date']: 
                daysBefore = (datetime.strptime(filters['from date'], "%Y-%m-%d").date() - datetime.now().date()).days
                query += f" time_created >= strftime('%Y-%m-%d', 'now', '{daysBefore} days')"
            if filters['to date']:
                daysAfter = (datetime.strptime(filters['to date'], "%Y-%m-%d").date() - datetime.now().date()).days
                query += f" AND time_created <= strftime('%Y-%m-%d', 'now', '{daysAfter} days')"
        else: 
            query += " time_created >= strftime('%Y-%m-%d', 'now', '-31 days')"
        if filters['game title']: query += f" AND title = '{filters['game title']}'"
        if filters['purchase platform']: query += f" AND buy_platform = '{filters['purchase platform']}'"
        if filters['sale platform']: query += f" AND sell_platform = '{filters['sale platform']}'"
        if filters['min purchase price']: query += f" AND buy_price >= '{filters['min purchase price']}'"
        if filters['max purchase price']: query += f" AND buy_price <= '{filters['max purchase price']}'"
        if filters['min fee']: query += f" AND fee >= '{filters['min fee']}'"
        if filters['max fee']: query += f" AND fee <= '{filters['max fee']}'"
        if filters['min sell price']: query += f" AND sell_price >= '{filters['min sell price']}'"
        if filters['max sell price']: query += f" AND sell_price <= '{filters['max sell price']}'"
        if filters['min profit']: query += f" AND sell_price - buy_price - fee >= '{filters['min profit']}'"
        if filters['min profit']: query += f" AND sell_price - buy_price - fee <= '{filters['min profit']}'"
    else:
        query += " time_created >= strftime('%Y-%m-%d', 'now', '-31 days') AND time_created <= strftime('%Y-%m-%d', 'now')"
    
    sales = cursor.execute(f"{query} ORDER BY time_created DESC").fetchall()
    salesList = []
    for sale in sales:
        salesList.append({
            'date': sale[7],
            'game title': sale[1],
            'purchase platform': sale[5],
            'purchase price': sale[2],
            'sell platform': sale[6],
            'sell price': sale[3],
            'fee': sale[4],
            'profit': sale[3] - sale[2] - sale[4]
        })
        
    return salesList

def addPurchasePlatform(purchase):
    cursor.execute(f"INSERT INTO purchase_platforms VALUES(null, '{purchase['platform']}')")
    connection.commit()

def addSalesPlatform(sale):
    cursor.execute(f"INSERT INTO sales_platforms VALUES(null, '{sale['platform']}')")
    connection.commit()

def loadPlatforms(platform): 
    platforms = cursor.execute(f"SELECT name FROM {platform}").fetchall()
    platformsList = []
    for platform in platforms:
        platformsList.append({
            'name': platform[0]
        })
    return platformsList