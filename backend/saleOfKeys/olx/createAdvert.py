from backend.saleOfKeys.olx.advertsActions import createAdvertData
from backend.database.databaseActions import addAdvert
from requests import post

def createAuction(game, header):
    advert = post('https://www.olx.pl/api/partner/adverts', headers=header, json = createAdvertData(game))
    
    addAdvert({
        'advert id': advert['id'],
        'platform': 'OLX PL', # Do zmiany
        'title': advert['title'],
        'price': advert['price']['value'],
        'currency': advert['price']['currency'],
        'url': advert['url'],
    })