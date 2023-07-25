from ast import literal_eval
from requests import get
from bs4 import BeautifulSoup
from xlsxwriter import Workbook

def loadGamesFromURL(link):
    allGames = []
    activePage = 1
    soup = BeautifulSoup(get(f'{link}&page={activePage}').content, 'html.parser')
    for _ in range(int((soup.find('li', class_='last-page').find('a', class_='pjax-link').text).replace('.', '')) if soup.find('li', class_='last-page') is not None else 1):
        newSoup = BeautifulSoup(get(f'{link}&page={activePage}').content, 'html.parser')
        games = []
        activePage += 1
        def removeSpecialCharactersFromPrice(price):
            if '~' in price: price = price.replace('~', '')
            if 'zł' in price: price = price.replace('zł', '')
            if ' ' in price: price = price.replace(' ', '')
            if ',' in price: price = price.replace(',', '.')
            return float(price)
            
        for _ in range(len(newSoup.find_all('div', class_='game-box-options'))):  games.append([])
        for key, gameTitle in enumerate(newSoup.find('div', class_='list-items').find_all('a', class_='game-info-title')): games[key].append(gameTitle.text)
        for key, gameOldPrice in enumerate(newSoup.find('div', class_='list-items').find_all('span', class_='price-old')): games[key].append(removeSpecialCharactersFromPrice(gameOldPrice.text))
        for key, gameNewPrice in enumerate(newSoup.find('div', class_='list-items').find_all('span', class_='game-price-new')): games[key].append(removeSpecialCharactersFromPrice(gameNewPrice.text))
        for key, gameShopLink in enumerate(newSoup.find('div', class_='list-items').find_all('a', class_='shop-link')): games[key].append(gameShopLink['href'])
        for key, _ in enumerate(games): games[key].append('Brak zmian')
        allGames.extend(games)
    return allGames
    
def loadGamesListFromFile():
    with open("docs/games.txt", "r", encoding='utf8') as file: 
        return literal_eval(file.read())
    
def checkDeletedGamesInList():
    pass

def checkExistingGamesInList(newGamesList, existingGamesList):
    existingGamesTitles = []
    deletedGamesList = existingGamesList
    for game in existingGamesList: existingGamesTitles.append(game[0])
    for key, newGame in enumerate(newGamesList):
        if newGame[0] not in existingGamesTitles: newGamesList[key][4] = 'Nowa pozycja'
        else:
            for existingGame in existingGamesList:
                if newGame[0] == existingGame[0]:
                    if newGame[2] > existingGame[2]: newGamesList[key][4] = 'Wyższa cena'
                    elif newGame[2] < existingGame[2]: newGamesList[key][4] = 'Niższa cena'
                    deletedGamesList.remove(existingGame)
    for deletedGame in deletedGamesList: 
        deletedGame[4] = 'Usunięta'
        newGamesList.append(deletedGame)
    return newGamesList

def saveGamesListToFile(games):
    gamesToSave = []
    for game in games:
        if game[4] == "Usunięta": break
        else: gamesToSave.append(game)
    with open("docs/games.txt", "w", encoding='utf8') as file: file.write(str(gamesToSave))

def createXLSXfile(games):
    workbook = Workbook('docs/Games to check.xlsx')
    allGamesWorksheet = workbook.add_worksheet('Wszystkie')
    newGamesWorksheet = workbook.add_worksheet('Nowe pozycje')
    higherPriceGamesWorksheet = workbook.add_worksheet('Droższe')
    lowerPriceGamesWorksheet = workbook.add_worksheet('Tańsze')
    deletedGamesWorksheet = workbook.add_worksheet('Usunięte')
    allGamesRow, newGamesRow, higherPriceGamesRow, lowerPriceGamesRow, deletedGamesRow, col = 1, 1, 1, 1, 1, 0

    worksheets = [
        [allGamesWorksheet, allGamesRow],
        [newGamesWorksheet, newGamesRow],
        [higherPriceGamesWorksheet, higherPriceGamesRow],
        [lowerPriceGamesWorksheet, lowerPriceGamesRow],
        [deletedGamesWorksheet, deletedGamesRow],
    ]

    def saveGameDataInWorksheet(worksheet):
        worksheet[0].write(worksheet[1], col,     title)
        worksheet[0].write(worksheet[1], col + 1, oldPrice)
        worksheet[0].write(worksheet[1], col + 2, newPrice)
        worksheet[0].write(worksheet[1], col + 3, shopLink)
        worksheet[0].write(worksheet[1], col + 4, status)
        worksheet[1] += 1

    def fitWorksheetAndCreateTable(worksheet):
        worksheet[0].autofit()
        worksheet[0].add_table(f'A1:D{worksheet[1]}',
            {
                'style': 'Table Style Light 1',
                'columns': [
                    {'header':'Nazwa gry'},
                    {'header':'Stara cena'},
                    {'header':'Nowa cena'},
                    {'header':'Link'},
                ],
            })

    for title, oldPrice, newPrice, shopLink, status in games:
        saveGameDataInWorksheet(worksheets[0])
        if status == 'Nowa pozycja': saveGameDataInWorksheet(worksheets[1])
        elif status == 'Wyższa cena': saveGameDataInWorksheet(worksheets[2])
        elif status == 'Niższa cena': saveGameDataInWorksheet(worksheets[3])
        elif status == 'Usunięta': saveGameDataInWorksheet(worksheets[4])

    for worksheet in worksheets: 
        if worksheet[1] > 1: fitWorksheetAndCreateTable(worksheet)

    workbook.close()

def checkGames():
    gamesFromGGdeals = loadGamesFromURL('https://gg.deals/deals/?drm=1&minDiscount=1&minRating=9&sort=discount&store=3,5,8,10,14,16,17,18,20,22,26,30,38,40,41,43,45,49,52,53,54,56,57,72,76,80,82,84,86,91,92,94,95,1169,1175')
    existingGamesList = loadGamesListFromFile()
    newGamesList = checkExistingGamesInList(gamesFromGGdeals, existingGamesList)
    saveGamesListToFile(newGamesList)
    createXLSXfile(newGamesList)
    return newGamesList