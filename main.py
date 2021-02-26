from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import random
import os
app = Flask(__name__)

datafile = os.path.join(app.static_folder, 'data', 'data.json')
data = json.load(open(datafile))
artistsData = data["artists"]
genresData = data["genres"]
albumsData = data["albums"]

# genreIndex is used for dynamically updating navbar dropdown as genres are added
genreIndex = [None]*len(genresData)
for thisGenre in genresData:
    genreIndex[int(thisGenre["id"])] = thisGenre


def getArtistAlbums(albumList):
    artistAlbums = [None]*len(albumList)
    for i, albumID in enumerate(albumList):
        artistAlbums[i] = albumsData[albumID]
    return artistAlbums


@app.route('/')
def index():
    return render_template('index.html', genreIndex=genreIndex)


@app.route('/search-by-artist', methods=['GET'])
def artists():
    return render_template('artistsTable.html', genreIndex=genreIndex)


@app.route('/search-by-song', methods=['GET'])
def songs():
    return render_template('songsTable.html', genreIndex=genreIndex)


@app.route('/search-by-genre', methods=['GET'])
def genres():
    return render_template('genresTable.html', genreIndex=genreIndex)


@app.route('/artist/<int:id>', methods=['GET'])
def artist(id):
    artistData = artistsData[int(id)]
    artistAlbums = getArtistAlbums(artistData["albums"])
    return render_template('artistPage.html', artistData=artistData, artistAlbums=artistAlbums, genreIndex=genreIndex)


@app.route('/genre/<int:id>', methods=['GET'])
def genre(id):
    return render_template('genrePage.html', genreData=genresData[id], genreIndex=genreIndex)


@app.route('/album/<int:id>', methods=['GET'])
def album(id):
    return render_template('songPage.html', albumData=albumsData[id], genreIndex=genreIndex)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
