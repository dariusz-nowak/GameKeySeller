from requests import post

def oAuthHeader():
    data = {
        "grant_type": "authorization_code",
        "client_id": "",
        "client_secret": "",
        "scope": "v2 read write"
    }
    accessToken = post('https://www.olx.pl/api/open/oauth/token', json=data).json()['access_token']

    headers = {
        "Authorization": f"Bearer {accessToken}",
        "Content-Type": "application/json"
    }
    
    return headers
