from saleOfKeys.olx.advertsActions import createDataJSON, getAdvertID
from requests import put

def editAuction(game, headers):
    advert = put(f'https://www.olx.pl/api/partner/adverts/{getAdvertID(game["title"])}', headers=headers, json = createDataJSON(game))