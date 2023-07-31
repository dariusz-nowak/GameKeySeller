from requests import post
from ast import literal_eval

clientID = None
client_secret = None

def oAuthHeader():

    tokenInformations = post('https://www.olx.pl/api/open/oauth/token', json = {
        "grant_type": "authorization_code",
        "client_id": clientID,
        "client_secret": client_secret,
        "scope": "v2 read write"
    }).json()
    
    if tokenInformations['expires_in'] == 0: 
        tokenInformations['access_token'] = refreshAccessToken(tokenInformations['refresh_token'])

    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {tokenInformations['access_token']}",
        "Version": "2.0",
    }

def refreshAccessToken(refreshToken):
    return post('https://www.olx.pl/api/open/oauth/token', json = {
        "grant_type": "refresh_token",
        "client_id": clientID,
        "client_secret": client_secret,
        "refresh_token": refreshToken
    }).json()['access_token'] # Sprawdzić, co zwraca zapytanie. Zwrócić access_token

def priceDetermination(currentPrice, oldPrice):
    quotient = (1 - (currentPrice / oldPrice)) * 100

    if quotient >= 80: sellPrice = currentPrice * 2.8
    elif quotient >= 60: sellPrice = currentPrice * 1.75
    elif quotient >= 40: sellPrice = currentPrice * 1.5
    elif quotient >= 20: sellPrice = currentPrice * 1.3
    else: sellPrice = currentPrice * 1.2
    
    if int(str(round(sellPrice, 2))[-4]) < 5: sellPrice += 5
    if sellPrice > oldPrice: sellPrice = oldPrice - 10

    return float(round(sellPrice, -1) - 0.01)

def createAdvertData(game):
    return {
        "title": game['title'],
        "description": game['description'],
        "category_id": 99,
        "advertiser_type": "private",
        "external_url": "",
        "external_id": "",
        "contact": {
        "name": "Dariusz Nowak",
        "phone": ""
    },
    "location": {
        "city_id": 0,
        "district_id": 0,
        "latitude": 0,
        "longitude": 0
    },
    "images": game['images'],
    "price": {
        "value": priceDetermination(game['current price'], game['old price']),
        "currency": "PLN",
        "negotiable": False,
        "trade": False,
        "budget": False
    },
    "salary": {
        "value_from": 0,
        "value_to": 0,
        "currency": "string",
        "negotiable": True,
        "type": "hourly"
    },
    "attributes": [
        {
        "code": "string",
        "value": "string",
        "values": [
            "string"
        ]
        }
    ],
    "courier": False
    }

def getAdvertID(gameTitle):
    with open("docs/adverts.txt", "r", encoding='utf8') as file: 
        adverts = literal_eval(file.read())
        for advert in adverts:
            if gameTitle == advert['title']: return advert['id']

def addAdvert(advert):
    with open("docs/adverts.txt", "r", encoding='utf8') as file: 
        adverts = literal_eval(file.read())
        adverts.append(advert)
    with open("docs/adverts.txt", "w", encoding='utf8') as file: file.write(str(adverts))

def removeAdvert(gameTitle):
    with open("docs/adverts.txt", "r", encoding='utf8') as file: 
        adverts = literal_eval(file.read())
        for advert in adverts:
            if gameTitle == advert['title']: adverts.remove(advert)
            break
    with open("docs/adverts.txt", "w", encoding='utf8') as file: file.write(str(adverts))