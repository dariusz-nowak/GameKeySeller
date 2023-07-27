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
    for game in gamesList: game.update(getGameInfo(game['title']))

# == OLX ==
def olxActions(gamesList):
    header = oAuthHeader()
    for gameType in gamesList:
        for game in gamesList[gameType]:
            if game[4] == 'Nowa pozycja': createAuction(game, header)
            elif game[4] == 'Wyższa cena' or game[4] == 'Niższa cena': editAuction(game, header)
            elif game[4] == 'Usunięta': removeAuction(game, header)

# stworzyć ofertę dla nowego klucza
# edytować cenę względem istniejących oferty
# usunąć ofertę dla usuniętego klucza

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach

def app():
    gamesList = getGamesFromGGdeals()
    # print(gamesList)
    getDataFromSteam(gamesList['new'])
    # print(gamesList)
    # olxActions(gamesList)

app()