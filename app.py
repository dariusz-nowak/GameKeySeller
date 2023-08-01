from backend.server.server_script import run_server
from backend.getInformation.database.databaseActions import removeGame
from backend.getInformation.ggDeals.ggDealsCheckGames import checkGames
from backend.getInformation.steam.steamGetGameInfo import getGameInfo
from backend.getInformation.steam.exceptions import checkException
from backend.getInformation.steam.exclusions import checkExclusions
from backend.saleOfKeys.olx.advertsActions import oAuthHeader
from backend.saleOfKeys.olx.createAdvert import createAuction
from backend.saleOfKeys.olx.editAdvert import editAuction
from backend.saleOfKeys.olx.removeAdvert import removeAuction
from ast import literal_eval

# == GG.DEALS ==
def getGamesFromGGdeals():
   return checkGames()

# == STEAM ==
def getDataFromSteam(gamesList, exclusionsList):
    for game in gamesList:
        if game['title'] in exclusionsList: continue
        try: game.update(getGameInfo(checkException(game['title']))) == 1
        except UnboundLocalError: 
            game['status'] = 'deleted'
            removeGame(game['id'])
    return gamesList

# == OLX ==
def olxActions(gamesList):
    # header = oAuthHeader()
    header = None
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

    # with open("gamesList.txt", "w", encoding="utf-8") as file:
    #     file.write(str(gamesList))

    with open("gamesList.txt", "r", encoding="utf-8") as file:
        gamesList = literal_eval(file.read())

    olxActions(gamesList)
    
run_server()

# while True:
#     app()
#     break

# Zrobić nieskończoną pętlę:
# 1. Wywołanie app()
# 2. Kilkukrotne sprawdzenie zakupów (co 5-10 minut)
#   a) Wywołanie auto-zakupu
# get city, categories
# For list of available categories, attributes, cities please check out appropriate endpoint references like /api/partner/categories, /api/partner/cities and so on.
# You can get list of required attributes by /api/partner/categories/ID/attributes endpoint where ID is the category ID you choosed. Endpoint return list of required and optional attributes to create advert - attributes vary in different countries and categories.