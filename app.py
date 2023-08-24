from backend.database.databaseActions import removeGame
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
            removeGame(game['id'], game['title'])
    return gamesList

# == OLX ==
def olxActions(gamesList):
    for gameType in gamesList:
        for game in gamesList[gameType]:
            # Zrobić pętle po wszystkich krajach OLX
            #
            # platforms = [
            #     { 'platform': 'OLX PL', 'client ID': 'cID', 'client secret': 'cST' },
            #     { 'platform': 'OLX BG', 'client ID': 'cID', 'client secret': 'cST' },
            #     { 'platform': 'OLX RO', 'client ID': 'cID', 'client secret': 'cST' },
            #     { 'platform': 'OLX PT', 'client ID': 'cID', 'client secret': 'cST' },
            #     { 'platform': 'OLX UA', 'client ID': 'cID', 'client secret': 'cST' },
            #     { 'platform': 'OLX KZ', 'client ID': 'cID', 'client secret': 'cST' }
            # ]
            #
            # for platform in platforms:
            #     header = oAuthHeader(platform['client ID'], platform['client secret'])
            #     Część kodu odpowiedzialna za tworzenie, edycje i usuwanie ofert

            header = None
            if game['status'] == 'new': createAuction(game, header)
            elif game['status'] == 'different price': editAuction(game, header)
            elif game['status'] == 'deleted': removeAuction(game, header)

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach

def app():
    gamesList = getGamesFromGGdeals()
    gamesList['new'] = getDataFromSteam(gamesList['new'], checkExclusions())

    with open("gamesList.txt", "w", encoding="utf-8") as file:
        file.write(str(gamesList))

    # with open("gamesList.txt", "r", encoding="utf-8") as file:
    #     gamesList = literal_eval(file.read())

    # olxActions(gamesList)
    
app()