from requests import post
from math import ceil

def priceDetermination(currentPrice, oldPrice):
    quotient = (1 - (currentPrice / oldPrice)) * 100

    if quotient >= 80: sellPrice = currentPrice * 2.8
    elif quotient >= 60: sellPrice = currentPrice * 1.75
    elif quotient >= 40: sellPrice = currentPrice * 1.5
    elif quotient >= 20: sellPrice = currentPrice * 1.3
    else: sellPrice = currentPrice * 1.2
    
    if int(str(round(sellPrice, 2))[-4]) < 5: sellPrice += 5
    if sellPrice > oldPrice: sellPrice = oldPrice - 10

    return round(sellPrice, -1) - 0.01

def createAuction(game, header, url):

    # TODO 
    # wybrać ID miasta

    data = {
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

    # post(url, headers=header, json = data)
    