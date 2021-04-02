import requests
import json
import os
from flask import Flask
app = Flask(__name__)

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
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


playlist_id = '6UeSakyzhiEt4NB3UAd6NQ'  # billboard 100 url
r = requests.get(BASE_URL + 'playlists/' + playlist_id,
                 headers=auth_header, params={'market': 'US'})
# gives us info from billboard 100

data = r.json()

artists = {}
for i in range(100):
    for j in data["tracks"]["items"][i]["track"]["artists"]:
        artists[j["id"]] = j["name"]
# extracts dictionary of artists in billboard 100 where key is artistID and value is artist name
# more than 100 artists because of features

uziKey = '4O15NlyKLIASxsJ0PrXPfz'
r = requests.get(BASE_URL + 'artists/' + uziKey + "/top-tracks/",
                 headers=auth_header, params={'market': 'US'})
data = r.json()
uziSongs = []
for i in data["tracks"]:
    uziSongs.append(i["name"])
# print(uziSongs)
# print(data["tracks"][0]["name"])
# print(data["tracks"][0]["album"]["name"])


tracks = []
for artistKey in artists.keys():

    r = requests.get(BASE_URL + 'artists/' + artistKey +
                     "/top-tracks/", headers=auth_header, params={'market': 'US'})
    data = r.json()
    for j in data["tracks"]:
        track = (j["name"])
        album = j["album"]["name"]
        dict = {"track": track, "album": album, "artist": artists[artistKey]}
        tracks.append(dict)


# print(tracks)
# print(len(tracks))
datafile = os.path.join(app.static_folder, 'data', 'dbdata.json')
with open(datafile, 'w') as fout:
    json.dump(tracks, fout)
