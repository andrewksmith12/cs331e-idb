import requests
import json
import os
import subprocess 
from models import db, Song, Artist, Album, Song_Album, Song_Artist, Genre, Genre_Artist

db.drop_all()
db.create_all()


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

playlistID = '6UeSakyzhiEt4NB3UAd6NQ'
spotifyUS50 = '37i9dQZEVXbLRQDuF5jeBp'
UKtop40 = '4OIVU71yO7SzyGrh0ils2i'


artistList = []
#subprocess.run("pbcopy", universal_newlines=True, input=str(data['tracks']['items']))

#Get list of artists to process
def processPlaylist(playlistID):
    r = requests.get(BASE_URL + 'playlists/' + playlistID, headers=auth_header, params={'market': 'US'})
    data = r.json()
    for song in data['tracks']['items']:
        for artist in song['track']['album']['artists']:
            if artist['id'] not in artistList:
                artistList.append(artist['id'])
    print(artistList)
    for artist in artistList:
        print("Add artist from billboard charts: "+artist)
        r = requests.get(BASE_URL + 'artists/' + artist, headers=auth_header, params={'market': 'US'})
        artistData = r.json()
        if artist not in artistsCreated:
            newArtist = Artist(name=artistData['name'], id=artistData['id'], thumbnail=artistData['images'][0]['url'])
            artistsCreated.append(artist)
            db.session.add(newArtist)
            for item in artistData['genres']:
                if item not in genresCreated:
                    newGenre = Genre(name=item)
                    db.session.add(newGenre)
                    genresCreated.append(item)
                dbGenre = db.session.query(Genre).filter(Genre.name==item).first()
                Genre_Artist(artist_id=artist, genre_name=item, artist=newArtist, genre=dbGenre)
        else:
            newArtist = db.session.query(Artist).filter(Artist.id==artist).first()
        r = requests.get(BASE_URL + 'artists/' + artist + '/top-tracks', headers=auth_header, params={'market': 'US'})
        songData = r.json()
        for song in songData['tracks']:
            if song['id'] not in songsCreated:
                print("Add Song: "+song['id'])
                newSong = Song(id=song['id'], title=song['name'], release_date=song['album']['release_date'], thumbnail=song['album']['images'][0]['url'])
                songsCreated.append(song['id'])
                db.session.add(newSong)
                for artist in song['album']['artists']:
                    if artist['id'] not in artistsCreated:
                        artistAdditional = requests.get(BASE_URL + 'artists/' + artist['id'], headers=auth_header, params={'market': 'US'})
                        artistAdditionalData = artistAdditional.json()
                        newAdditionalArtist = Artist(name=artistAdditionalData['name'], id=artistAdditionalData['id'], thumbnail=artistAdditionalData['images'][0]['url'])
                        artistsCreated.append(artist['id'])
                        print("Add Additional Artist: "+artist['id'])
                        db.session.add(newAdditionalArtist)
                    dbArtist = db.session.query(Artist).filter(Artist.id==artist['id']).first()
                    print("Start Song-Artist Rel: artist:"+song['id']+" artist: "+artist['id'])
                    Song_Artist(artist_id=dbArtist.id, song_id=newSong.id, artist=dbArtist, song=newSong)
                if song['album']['id'] not in albumsCreated:
                    dbArtist = db.session.query(Artist).filter(Artist.id==artist['id']).first()
                    newAlbum = Album(id=song['album']['id'], title=song['album']['name'], thumbnail=song['album']['images'][0]['url'], artistID=artist['id'], artist=dbArtist)
                    albumsCreated.append(song['album']['id'])
                    db.session.add(newAlbum)
                album = db.session.query(Album).filter(Album.id==song['album']['id']).first()
                Song_Album(album_id=song['album']['id'], song_id=song['id'], album=album, song=newSong)
genresCreated = []
artistsCreated = []
albumsCreated = []
songsCreated = []
errorSongs = []
processPlaylist(playlistID)
artistList.clear()
processPlaylist(spotifyUS50)
artistList.clear()
processPlaylist(UKtop40)
db.session.commit()
print("Commit Done!")