from backend.saleOfKeys.olx.advertsActions import createAdvertData, priceDetermination
from backend.getInformation.database.databaseActions import addAdvert
from requests import post

def createAuction(game, header):
    advert = post('https://www.olx.pl/api/partner/adverts', headers=header, json = createAdvertData(game))
    
    addAdvert({
        'id': advert['id'],
        'title': advert['title'],
        'image': game['image'][0],
        'price': priceDetermination(game['current price'], game['old price']),
        'url': advert['url'],
    })