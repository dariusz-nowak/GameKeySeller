from requests import post

def oAuthHeader(url):
    data = {
        "grant_type": "authorization_code",
        "client_id": "",
        "client_secret": "",
        "scope": "v2 read write"
    }
    accessToken = post(url, json=data).json()['access_token']

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {accessToken}",
        "Version": 2.0,
    }
    
    return headers
