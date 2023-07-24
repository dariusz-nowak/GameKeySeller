from ast import literal_eval
from steam import Steam
steam = Steam("STEAM_API_KEY")

def getGameInfo(gameName):
    gameID = steam.apps.search_games(gameName)['apps'][0]['id']
    game = steam.apps.get_app_details(gameID)
    
    game = game.replace('true', 'True')
    game = game.replace('false', 'False')
    game = literal_eval(game)
    
    gameDescription = game[str(gameID)]['data']['detailed_description']
    gameImages = [image['path_full'] for key, image in enumerate(game[str(gameID)]['data']['screenshots']) if key < 5]

    return [gameDescription, gameImages]