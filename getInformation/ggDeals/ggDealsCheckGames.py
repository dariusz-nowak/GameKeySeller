from ast import literal_eval
from requests import get
from bs4 import BeautifulSoup

def loadGamesFromURL(url):
    soup = BeautifulSoup(get(url).content, 'html.parser')

    games = []
    currentPage = 1

    if soup.find('li', class_='last-page') != None: 
        pages = int(soup.find('li', class_='last-page').text.replace('.', ''))
    else: pages = 1
    
    def removeSpecialCharactersFromPrice(price):
        for char in price:
            if char == ',': price = price.replace(',', '.')
            elif not char.isnumeric(): price = price.replace(char, '')
        return float(price)

    for _ in range(pages):
        if currentPage > 1: soup = BeautifulSoup(get(f'{url}&page={currentPage}').content, 'html.parser')

        for container in soup.find_all('div', class_='game-box-options'):
            games.append({
                'title': container.find('a', class_='game-info-title').text,
                'old price': removeSpecialCharactersFromPrice(container.find('span', class_='price-old').text),
                'current price': removeSpecialCharactersFromPrice(container.find('span', class_='game-price-new').text),
                'store': f'https://gg.deals{container.find("a", class_="shop-link")["href"]}',
                'status': 'none'
            })
        currentPage += 1
    return games

def loadGamesListFromFile():
    with open("docs/games.txt", "r", encoding='utf8') as file: 
        return literal_eval(file.read())
    
def checkExistingGamesInList(newGamesList, existingGamesList):
    existingGamesTitles = [game['title'] for game in existingGamesList]
    
    for newGame in newGamesList:
        if newGame['title'] not in existingGamesTitles: 
            newGame['status'] = 'new'
            continue

        for existingGame in existingGamesList:
            if newGame['title'] == existingGame['title']:
                if newGame['current price'] > existingGame['current price']: newGame['status'] = 'expensive'
                elif newGame['current price'] < existingGame['current price']: newGame['status'] = 'cheaper'
                existingGamesList.remove(existingGame)\
                
    for remainingGame in existingGamesList:
        remainingGame['status'] = 'deleted'
        newGamesList.append(remainingGame)
    
    return newGamesList

def saveGamesListToFile(games):
    gamesToSave = []
    for game in games:
        if game['status'] == "Usunięta": break
        else: gamesToSave.append(game)
    with open("docs/games.txt", "w", encoding='utf8') as file: file.write(str(gamesToSave))

def sortGamesInList(gamesList):
    sortedGamesList = {
        'new' : [],
        'expensive' : [],
        'cheaper' : [],
        'deleted' : [],
    }

    for game in gamesList:
        if game['status'] == 'new': sortedGamesList['new'].append(game)
        elif game['status'] == 'expensive': sortedGamesList['expensive'].append(game)
        elif game['status'] == 'cheaper': sortedGamesList['cheaper'].append(game)
        elif game['status'] == 'deleted': sortedGamesList['deleted'].append(game)

    return sortedGamesList

def checkGames():
    # url = 'https://gg.deals/deals/?drm=1&minDiscount=1&minPrice=1&minRating=7&store=3,8,14,16,17,18,20,26,30,40,41,43,45,49,52,53,54,56,76,80,82,84,86,91,92,94,95,1169,1175'
    # gamesList = checkExistingGamesInList(
    #     loadGamesFromURL(url), 
    #     loadGamesListFromFile()
    # )
    # saveGamesListToFile(gamesList)

    gamesList = {'new': [{'title': 'LEGO Star Wars: The Skywalker Saga', 'old price': 206.47, 'current price': 59.17, 'store': 'https://gg.deals/pl/redirect/b546b263ccb10776783f5734ce2babc3c2063091/?utm_source=deals%2Findex', 'status': 'new'}, {'title': "Marvel's Midnight Suns", 'old price': 249.0, 'current price': 85.66, 'store': 'https://gg.deals/pl/redirect/238b63541ffffb2cf46fecc62001159f2cc1a57a/?utm_source=deals%2Findex', 'status': 'new'}], 'expensive': [{'title': "Tiny Tina's Wonderlands", 'old price': 249.0, 'current price': 70.67, 'store': 'https://gg.deals/pl/redirect/f0057754e02fcce6913a158e3ff28c3205f2eb17/?utm_source=deals%2Findex', 'status': 'expensive'}], 'cheaper': [{'title': 'FINAL FANTASY XV WINDOWS EDITION', 'old price': 125.99, 'current price': 63.0, 'store': 'https://gg.deals/pl/redirect/1d0dc429f9f18bda92fc78bb3efca4b05da44000/?utm_source=deals%2Findex', 'status': 'cheaper'}, {'title': 'Tales of Arise', 'old price': 265.4, 'current price': 74.06, 'store': 'https://gg.deals/pl/redirect/cebf54d726ae3e9adb882ffb2755187bc020583b/?utm_source=deals%2Findex', 'status': 'cheaper'}], 'deleted': [{'title': 'xddddd', 'old price': 206.47, 'current price': 59.17, 'store': 'https://gg.deals/pl/redirect/b546b263ccb10776783f5734ce2babc3c2063091/?utm_source=deals%2Findex', 'status': 'deleted'}, {'title': 'wwwwwww', 'old price': 19.0, 'current price': 15.66, 'store': 'https://gg.deals/pl/redirect/238b63541ffffb2cf46fecc62001159f2cc1a57a/?utm_source=deals%2Findex', 'status': 'deleted'}, {'title': 'TEST1', 'old price': 206.47, 'current price': 59.17, 'store': 'https://gg.deals/pl/redirect/b546b263ccb10776783f5734ce2babc3c2063091/?utm_source=deals%2Findex', 'status': 'deleted'}, {'title': 'TEST2', 'old price': 110.56, 'current price': 274.06, 'store': 'https://gg.deals/pl/redirect/886b910766c17d718ec5a3e57967654065d49ffb/?utm_source=deals%2Findex', 'status': 'deleted'}]}

    return gamesList
    # return sortGamesInList(gamesList)