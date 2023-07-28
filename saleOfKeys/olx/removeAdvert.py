from saleOfKeys.olx.advertsActions import removeAdvert, getAdvertID
from requests import delete

def removeAuction(game, headers):
    advertID = int(getAdvertID(game["title"]))
    advert = delete(f'https://www.olx.pl/api/partner/adverts/{advertID}', headers=headers, json = {"advertId": advertID})
    removeAdvert(game['title'])
