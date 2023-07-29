from getInformation.ggDeals.ggDealsCheckGames import checkGames, saveGamesListToFile
from getInformation.steam.steamGetGameInfo import getGameInfo
from getInformation.steam.exceptions import checkException
from getInformation.steam.exclusions import checkExclusions
from saleOfKeys.olx.advertsActions import oAuthHeader
from saleOfKeys.olx.createAdvert import createAuction
from saleOfKeys.olx.editAdvert import editAuction
from saleOfKeys.olx.removeAdvert import removeAuction
from ast import literal_eval

olxURL = ""

# == GG.DEALS ==
def getGamesFromGGdeals():
   return checkGames()

def removeGameFromGGdealsFile(games):
    with open("docs/games.txt", "r", encoding='utf8') as file: 
        ggDealsGamesList = literal_eval(file.read())
    for ggDealsgame in ggDealsGamesList:
        for game in games:
            if ggDealsgame['title'] == game['title']: ggDealsGamesList.remove(ggDealsgame)
    saveGamesListToFile(ggDealsGamesList)

# == STEAM ==
def getDataFromSteam(gamesList, exclusionsList):
    gamesToRemoveFromGGdealsFile = []
    for game in gamesList:
        if game['title'] in exclusionsList: continue
        try: game.update(getGameInfo(checkException(game['title']))) == 1
        except UnboundLocalError: 
            game['status'] = 'unknown'
            gamesToRemoveFromGGdealsFile.append(game)
            with open("docs/titlesToRepair.txt", "a", encoding='utf8') as file: 
                file.write(f'{game["title"]}\n')
    removeGameFromGGdealsFile(gamesToRemoveFromGGdealsFile)
    return gamesList

# == OLX ==
def olxActions(gamesList):
    header = oAuthHeader()
    for gameType in gamesList:
        for game in gamesList[gameType]:
            if game['status'] == 'new': createAuction(game, header)
            elif game['status'] == 'different price': editAuction(game, header)
            elif game['status'] == 'deleted': removeAuction(game, header)

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach

def app():
    # gamesList = getGamesFromGGdeals()
    # gamesList['new'] = getDataFromSteam(gamesList['new'], checkExclusions())
    
    # with open("docs/steamGameList.txt", "w", encoding='utf8') as file: file.write(f'{gamesList}\n')
    with open("docs/steamGameList.txt", "r", encoding='utf8') as file: 
        gamesList = literal_eval(file.read())

    olxActions(gamesList)

app()

# get city, categories
# For list of available categories, attributes, cities please check out appropriate endpoint references like /api/partner/categories, /api/partner/cities and so on.
# You can get list of required attributes by /api/partner/categories/ID/attributes endpoint where ID is the category ID you choosed. Endpoint return list of required and optional attributes to create advert - attributes vary in different countries and categories.