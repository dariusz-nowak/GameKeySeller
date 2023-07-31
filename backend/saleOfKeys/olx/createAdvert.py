from backend.saleOfKeys.olx.advertsActions import addAdvert, createAdvertData
from requests import post

def createAuction(game, header):
    advert = post('https://www.olx.pl/api/partner/adverts', headers=header, json = createAdvertData(game))
    
    addAdvert({
        'id': advert['id'],
        'title': advert['title'],
        'url': advert['url'],
    })