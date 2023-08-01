from backend.saleOfKeys.olx.advertsActions import createAdvertData, priceDetermination
from backend.getInformation.database.databaseActions import getAdvertID, editAdvert
from requests import put

def editAuction(game, headers):
    advert = put(f'https://www.olx.pl/api/partner/adverts/{getAdvertID(game["id"])}', headers=headers, json = createAdvertData(game))
    
    editAdvert({
        'id': advert['id'],
        'price': advert['price']['value'],
    })