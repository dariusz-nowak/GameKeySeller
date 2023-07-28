from getInformation.ggDeals.ggDealsCheckGames import checkGames, saveGamesListToFile
from getInformation.steam.steamGetGameInfo import getGameInfo
from getInformation.steam.exceptions import checkException
from getInformation.steam.exclusions import checkExclusions
from saleOfKeys.olx.createAuction import createAuction
from saleOfKeys.olx.editAuction import editAuction
from saleOfKeys.olx.removeAuction import removeAuction
from saleOfKeys.olx.config import oAuthHeader
from ast import literal_eval

olxURL = "https://www.olx.pl"

# == GG.DEALS ==
def getGamesFromGGdeals():
   return checkGames()

def removeGameFromGGdealsFile(game):
    with open("docs/games.txt", "r", encoding='utf8') as file: ggDealsGamesList = literal_eval(file.read())
    for ggDealsgame in ggDealsGamesList:
        if ggDealsgame['title'] == game['title']: ggDealsGamesList.remove(ggDealsgame)
    saveGamesListToFile(ggDealsGamesList)

# == STEAM ==
def getDataFromSteam(gamesList):
    for game in gamesList:
        if game['title'] in checkExclusions(): continue
        try: game.update(getGameInfo(checkException(game['title']))) == 1
        except UnboundLocalError: 
            game['status'] = 'unknown'
            removeGameFromGGdealsFile(game)
            with open("docs/titlesToRepair.txt", "a", encoding='utf8') as file: file.write(f'{game["title"]}\n')
    return gamesList

# == OLX ==
def olxActions(gamesList):
    # header = oAuthHeader(f'{olxURL}/api/open/oauth/token')
    header = 'a'
    for gameType in gamesList:
        for game in gamesList[gameType]:
            if game['status'] == 'new': createAuction(game, header, f'{olxURL}/api/partner/adverts')
            elif game['status'] == 'expensive' or game['status'] == 'cheaper': editAuction(game, header)
            elif game['status'] == 'deleted': removeAuction(game, header)

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach

def app():
    gamesList = getGamesFromGGdeals()
    gamesList['new'] = getDataFromSteam(gamesList['new'])
    
    # with open("docs/steamGameList.txt", "w", encoding='utf8') as file: file.write(f'{gamesList}\n')
    # with open("docs/steamGameList.txt", "r", encoding='utf8') as file: 
    #     gamesList = literal_eval(file.read())

    # olxActions(gamesList)

app()

# get city, categories
# For list of available categories, attributes, cities please check out appropriate endpoint references like /api/partner/categories, /api/partner/cities and so on.
# You can get list of required attributes by /api/partner/categories/ID/attributes endpoint where ID is the category ID you choosed. Endpoint return list of required and optional attributes to create advert - attributes vary in different countries and categories.