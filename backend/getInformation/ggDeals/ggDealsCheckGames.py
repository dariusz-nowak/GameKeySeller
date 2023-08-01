from backend.getInformation.database.databaseActions import loadGamesList, editGamesList
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint

def loadGamesFromURL(url):
    games = []
    currentPage = 1
    soup = BeautifulSoup(get(url).content, 'html.parser')
    
    def removeSpecialCharactersFromPrice(price):
        for char in price:
            if char == ',': price = price.replace(',', '.')
            elif not char.isnumeric(): price = price.replace(char, '')
        return float(price)

    if soup.find('li', class_='last-page') != None: 
        pages = int(soup.find('li', class_='last-page').text.replace('.', ''))
    else: pages = 1

    for _ in range(pages):
        print(f'loading games from gg.deals, page {currentPage}')
        # sleep(randint(20, 40))
        sleep(randint(2, 4))
        
        if currentPage > 1: soup = BeautifulSoup(get(f'{url}&page={currentPage}').content, 'html.parser')

        for gameDiv in soup.find_all('div', class_='game-box-options'):
            games.append({
                'id': 0,
                'title': gameDiv.find('a', class_='game-info-title').text,
                'old price': removeSpecialCharactersFromPrice(gameDiv.find('span', class_='price-old').text),
                'current price': removeSpecialCharactersFromPrice(gameDiv.find('span', class_='game-price-new').text),
                'store': f'https://gg.deals{gameDiv.find("a", class_="shop-link")["href"]}',
                'status': ''
            })
        currentPage += 1
    return games
    
def checkExistingGamesInList(newGamesList, existingGamesList):
    existingGamesTitles = [game['title'].replace('`', '\'') for game in existingGamesList]

    for newGame in newGamesList:
        if newGame['title'] not in existingGamesTitles: 
            newGame['status'] = 'new'
            continue

        for existingGame in existingGamesList:
            if newGame['title'] == existingGame['title']:
                newGame['id'] = existingGame['id']

                if newGame['current price'] != existingGame['current price']: newGame['status'] = 'different price'
                else: newGame['status'] = 'no changes'
                
                existingGamesList.remove(existingGame)
                break
                
    for remainingGame in existingGamesList:
        remainingGame['status'] = 'deleted'
        newGamesList.append(remainingGame)

    return newGamesList

def sortGamesInList(gamesList):
    sortedGamesList = {
        'new' : [],
        'different price' : [],
        'deleted' : [],
    }

    for game in gamesList:
        if game['status'] == 'new': sortedGamesList['new'].append(game)
        elif game['status'] == 'different price': sortedGamesList['different price'].append(game)
        elif game['status'] == 'deleted': sortedGamesList['deleted'].append(game)

    return sortedGamesList

def checkGames():
    url = 'https://gg.deals/deals/?drm=1&minDiscount=1&minPrice=1&minRating=6&platform=1&store=3,8,14,16,17,18,20,26,30,40,41,43,45,49,52,53,54,56,76,80,82,84,86,91,92,95'
    return sortGamesInList(editGamesList(checkExistingGamesInList(loadGamesFromURL(url), loadGamesList())))
