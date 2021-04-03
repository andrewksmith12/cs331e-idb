from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from models import app, db, Artist, Song, Album, Song_Artist, Song_Album  # , Location
import random
import os
query = db.session.query

datafile = os.path.join(app.static_folder, 'data', 'data.json')
data = json.load(open(datafile))
locationsData = data["locations"]

# locationIndex is used for dynamically updating navbar dropdown as locations are added
locationIndex = [None]*len(locationsData)
for thislocation in locationsData:
    locationIndex[int(thislocation["id"])] = thislocation


"""def getArtistAlbums(albumList):
    artistAlbums = [None]*len(albumList)
    for i, albumID in enumerate(albumList):
        artistAlbums[i] = albumsData[albumID]
    return artistAlbums"""


@app.route('/')
def index():
    return render_template('index.html', locationIndex=locationIndex)


@app.route('/search-by-artist', methods=['GET'])
def artists():
    song_list = query(Song).all()
    album_list = query(Album).all()
    artist_list = query(Artist).all()
    return render_template('artistsTable.html', locationIndex=locationIndex, song_list=song_list, album_list = album_list, artist_list = artist_list)


@app.route('/search-by-song', methods=['GET'])
def songs():
    song_list = query(Song).all()
    album_list = query(Album).all()
    artist_list = query(Artist).all()
    return render_template('songsTable.html', locationIndex=locationIndex, song_list=song_list, album_list = album_list, artist_list = artist_list)
    
@app.route('/search-by-album', methods=['GET'])
def albums():
    song_list = query(Song).all()
    album_list = query(Album).all()
    artist_list = query(Artist).all()
    return render_template('albumTable.html', locationIndex=locationIndex, song_list=song_list, album_list = album_list, artist_list = artist_list)


"""@app.route('/search-by-location', methods=['GET'])
def locations():
    return render_template('locationsTable.html', locationIndex=locationIndex)"""


@app.route('/artist/<string:id>', methods=['GET'])
def artist(id):
    artistData = query(Artist).filter(Artist.id == id).first()
    artistAlbums = query(Album).filter(Album.artistID== id).all()
    print(artistAlbums)
    return render_template('artistPage.html', artistData=artistData, artistAlbums=artistAlbums)


"""@app.route('/location/<int:id>', methods=['GET'])
def location(id):
    return render_template('locationsPage.html', locationData=locationsData[id], locationIndex=locationIndex)"""


@app.route('/album/<string:id>', methods=['GET'])
def album(id):
    albumID = query(Album).filter(Album.id == id).first()
    songsQuery = query(Song_Album).filter(Song_Album.album_id == id)
    for song in songsQuery:
        print(song.song_id)
    #artistID = query(Album).filter(Artist.id == albumID.artist).first()

    return render_template('albumPage.html', albumID=albumID, artistsList = artistsList, songID = songID)
    
@app.route('/song/<string:id>', methods=['GET'])
def song(id):
    songID = query(Song).filter(Song.id == id).first()
    artistsList = query(Song_Artist).filter(Song_Artist.song_id==id)
    for songArtist in artistsList:
        print(songArtist.artist.name)
    albumID = query(Album).filter(Album.id == songID.albums[0].album_id).first()
    return render_template('songPage.html', songID= songID, artistsList = artistsList, albumID = albumID)
    

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
