from steam import Steam
from ast import literal_eval
from re import compile, sub
from time import sleep

steam = Steam("5017E3CC647B3610F0029724DCFE8774")

def removeHTMLtags(raw_html):
     raw_html = sub(compile('<a.*?/a>') , '', raw_html)
     raw_html = sub(compile('<br>') , '\n', raw_html)
     raw_html = sub(compile('<.*?>') , '', raw_html)
     raw_html = sub(compile('&nbsp;') , ' ', raw_html)
     return raw_html

def getGameInfo(gameName):
     print(f'loading {gameName}')
     sleep(3.2)
     gameSteamID = steam.apps.search_games(gameName)['id']
     game = str(steam.apps.get_app_details(gameSteamID))

     game = game.replace('true', 'True')
     game = game.replace('false', 'False')
     game = game.replace('null', 'None')
     game = literal_eval(game)

     return {
          'description': removeHTMLtags(game[str(gameSteamID)]['data']['detailed_description']), 
          'images': [{'url': image['path_full']} for key, image in enumerate(game[str(gameSteamID)]['data']['screenshots']) if key < 5]
     }