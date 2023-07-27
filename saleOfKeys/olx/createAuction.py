def createAuction(game, header):

    # todo 
    # wybrać kategorie
    # wybrać ID miasta
    # dodać zdjęcia
    # określić cenę

    data = {
        "title": game['title'],
        "description": game['description'],
        "category_id": 0,
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
    "images": [
        {
            "url": "string"
        }
    ],
    "price": {
        "value": 0,
        "currency": "string",
        "negotiable": True,
        "trade": True,
        "budget": True
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
    