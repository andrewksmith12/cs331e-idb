import requests
CLIENT_ID = "adcb7fe6a96a4e4db325d9c5440b0419"
CLIENT_SECRET = "51eaeca06fae4f0383bf7b298d7c3773"
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = 'https://api.spotify.com/v1/'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
access_token = auth_response.json()['access_token']
auth_header = {
    'Authorization' : 'Bearer {token}'.format(token=access_token)
}

artist_id = '1t8LijuXy59r0O5qlLkENl'

r = requests.get(BASE_URL + 'search/', headers=auth_header, params={'q':'taylor swift', 'type':'artist'})
data = r.json()

for artist in data['artists']['items']:
    print(artist['name']+" ----- "+ artist['id']+" ---- "+str(artist['followers']['total']))