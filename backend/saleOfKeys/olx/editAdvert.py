from backend.saleOfKeys.olx.advertsActions import createAdvertData, getAdvertID
from requests import put

def editAuction(game, headers):
    put(f'https://www.olx.pl/api/partner/adverts/{getAdvertID(game["title"])}', headers=headers, json = createAdvertData(game))