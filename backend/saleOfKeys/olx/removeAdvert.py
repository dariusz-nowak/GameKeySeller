from backend.getInformation.database.databaseActions import removeAdvert, getAdvertID
from requests import delete

def removeAuction(game, headers):
    delete(f'https://www.olx.pl/api/partner/adverts/{int(getAdvertID(game["id"]))}', headers=headers, json = {"command": 'finish'})
    removeAdvert(game['id'])