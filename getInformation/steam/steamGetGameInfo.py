from ast import literal_eval
from steam import Steam
from re import compile, sub
from time import sleep

steam = Steam("STEAM_API_KEY")

def removeHTMLtags(raw_html):
     raw_html = sub(compile('<a.*?/a>') , '', raw_html)
     raw_html = sub(compile('<br>') , '\n', raw_html)
     raw_html = sub(compile('<.*?>') , '', raw_html)
     raw_html = sub(compile('&nbsp;') , ' ', raw_html)
     return raw_html

def getGameInfo(gameName):
     sleep(1.5)
     gameID = steam.apps.search_games(gameName)['id']
     game = str(steam.apps.get_app_details(gameID))

     game = game.replace('true', 'True')
     game = game.replace('false', 'False')
     game = game.replace('null', 'None')
     game = literal_eval(game)

     gameDescription = removeHTMLtags(game[str(gameID)]['data']['detailed_description'])
     gameImages = [image['path_full'] for key, image in enumerate(game[str(gameID)]['data']['screenshots']) if key < 5]

     return {
          'description': gameDescription, 
          'images': gameImages
          }