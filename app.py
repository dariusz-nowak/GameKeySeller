from getInformation.ggDeals.ggDealsCheckGames import checkGames
from getInformation.steam.steamGetGameInfo import getGameInfo
from getInformation.steam.exceptions import checkException
from getInformation.steam.exclusions import checkExclusions
from saleOfKeys.olx.createAuction import createAuction
from saleOfKeys.olx.editAuction import editAuction
from saleOfKeys.olx.removeAuction import removeAuction
from saleOfKeys.olx.config import oAuthHeader
from ast import literal_eval

# == GG.DEALS ==
def getGamesFromGGdeals():
   return checkGames()

# == STEAM ==
def getDataFromSteam(gamesList):
    for game in gamesList:
        if game['title'] in checkExclusions(): continue
        try: game.update(getGameInfo(checkException(game['title'])))
        except UnboundLocalError:
            game['status'] = 'unknown'
            with open("docs/titlesToRepair.txt", "a", encoding='utf8') as file: file.write(f'{game["title"]}\n')

# == OLX ==
def olxActions(gamesList):
    # header = oAuthHeader()
    header = 'a'
    for gameType in gamesList:
        for game in gamesList[gameType]:
            if game['status'] == 'new': createAuction(game, header)
            elif game['status'] == 'expensive' or game['status'] == 'cheaper': editAuction(game, header)
            elif game['status'] == 'deleted': removeAuction(game, header)

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach

def app():
    # gamesList = getGamesFromGGdeals()
    # getDataFromSteam(gamesList['new'])
    
    # with open("docs/steamGameList.txt", "w", encoding='utf8') as file: file.write(f'{gamesList}\n')
    with open("docs/steamGameList.txt", "r", encoding='utf8') as file: 
        gamesList = literal_eval(file.read())

    olxActions(gamesList)

app()