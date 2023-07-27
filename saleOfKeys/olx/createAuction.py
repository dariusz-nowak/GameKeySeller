def createAuction(game, header):
    data = {
        "title": "string",
        "description": "string",
        "category_id": 0,
        "advertiser_type": "private",
        "external_url": "string",
        "external_id": "string",
        "contact": {
        "name": "string",
        "phone": "string"
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
    "courier": True
    }
    pass