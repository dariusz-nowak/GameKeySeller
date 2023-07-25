from requests import post

def oAuthConfig():

    url = 'https://www.olx.pl/api/open/oauth/token'
    data = {
        "grant_type": "authorization_code",
        "client_id": "",
        "client_secret": "",
        "code": "",
        "scope": "v2 read write"
    }

    response  = post(url, json = data)
