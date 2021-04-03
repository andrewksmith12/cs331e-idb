from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from create_db import app, db, Artist, Song, Album
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


@app.route('/artist/<int:id>', methods=['GET'])
def artist(id):
    artistData = query(Artist).filter(Artist.id == id)
    artistAlbums = getArtistAlbums(artistData["albums"])
    return render_template('artistPage.html', artistData=artistData, artistAlbums=artistAlbums, locationIndex=locationIndex)


"""@app.route('/location/<int:id>', methods=['GET'])
def location(id):
    return render_template('locationsPage.html', locationData=locationsData[id], locationIndex=locationIndex)"""


@app.route('/album/<int:id>', methods=['GET'])
def album(id):
    return render_template('songPage.html', albumData=albumsData[id], locationIndex=locationIndex)
    
@app.route('/song/<int:id>', methods=['GET'])
def song(id):
    songID = query(Song).filter(Song.id == id).first()
    artistID = query(Artist).filter(Artist.id == songID.artists[0].artist_id).first()
    albumID = query(Album).filter(Album.id == songID.albums[0].album_id).first()
    return render_template('songPage.html', songID= songID, artistID = artistID, albumID = albumID)
    

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
