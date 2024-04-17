"""define a function to authenticate the app for requesting the reddit API"""
import requests
import os
def app_auth():
    """authenticate the app to access the reddit API"""
    client_id = os.environ["CLIENT_ID"]
    secret_token = os.environ["SECRET_TOKEN"]
    username = os.environ["USERNAME"]
    password = os.environ["PASSWORD"]
    auth = requests.auth.HTTPBasicAuth(client_id, secret_token)

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': username,
            'password': password}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'AZlegacy/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    print(res)
    print(res.text)
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    # while the token is valid (~2 hours) we just add headers=headers to our requests
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
