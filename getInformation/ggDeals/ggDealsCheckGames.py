from ast import literal_eval
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint

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
        print(f'loading page {currentPage}')
        if currentPage > 1: 
            sleep(randint(5, 10))
            soup = BeautifulSoup(get(f'{url}&page={currentPage}').content, 'html.parser')

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
                existingGamesList.remove(existingGame)
                
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
    url = 'https://gg.deals/deals/?drm=1&minDiscount=1&minPrice=1&minRating=5&platform=1&store=3,8,14,16,17,18,20,26,30,40,41,43,45,49,52,53,54,56,76,80,82,84,86,91,92,95'
    gamesList = checkExistingGamesInList(
        loadGamesFromURL(url), 
        loadGamesListFromFile()
    )
    saveGamesListToFile(gamesList)
    return sortGamesInList(gamesList)
    