from backend.saleOfKeys.olx.advertsActions import createAdvertData, priceDetermination
from backend.getInformation.database.databaseActions import addAdvert
from requests import post

def createAuction(game, header):
    advert = post('https://www.olx.pl/api/partner/adverts', headers=header, json = createAdvertData(game))
    
    addAdvert({
        'id': advert['id'],
        'game id': game['id'],
        'title': advert['title'],
        'image': advert['images'][0]['url'],
        'price': advert['price']['value'],
        'url': advert['url'],
    })