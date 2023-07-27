from getInformation.ggDeals.ggDealsCheckGames import checkGames
from getInformation.steam.steamGetGameInfo import getGameInfo
from saleOfKeys.olx.createAuction import createAuction
from saleOfKeys.olx.editAuction import editAuction
from saleOfKeys.olx.removeAuction import removeAuction
from saleOfKeys.olx.config import oAuthHeader

# == GG.DEALS ==
def getGamesFromGGdeals():
   return checkGames()

# == STEAM ==
def getDataFromSteam(gamesList):
    for game in gamesList: 
        game.update(getGameInfo(game['title']))

# == OLX ==
def olxActions(gamesList):
    header = oAuthHeader()
    for game in gamesList:
        if game['status'] == 'new': createAuction(game, header)
        elif game['status'] == 'expensive' or game['status'] == 'cheaper': editAuction(game, header)
        elif game['status'] == 'deleted': removeAuction(game, header)

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach

def app():
    gamesList = getGamesFromGGdeals()
    getDataFromSteam(gamesList['new'])
    olxActions(gamesList)

app()