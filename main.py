from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import random
import os
app = Flask(__name__)

datafile = os.path.join(app.static_folder, 'data', 'data.json')
data = json.load(open(datafile))
artists = data["artists"]
genres = data["genres"]
albums = data["albums"]

genreIndex = [None]*len(genres)
for thisGenre in genres:
    genreIndex[int(thisGenre["id"])] = thisGenre


def getArtistAlbums(albumList):
    artistAlbums = [None]*len(albumList)
    for i, albumID in enumerate(albumList):
        artistAlbums[i] = albums[albumID]
    return artistAlbums


@app.route('/')
def index():
    return render_template('splash.html')


# Example page for adding to a 'Bands' list, that lets you search bands
@app.route('/addBand/', methods=['GET', 'POST'])
def addBand():
    # If this page receives a post request...
    if request.method == 'POST':
        # Process whatever data has been received, then redirect to main page, or elsewhere as needed
        # "bands.insert(request.form['name'])
        return redirect(url_for('index'))
    else:
        # Otherwise, render the page
        return render_template('addBand.html')


@app.route('/artist/<int:id>', methods=['GET'])
def artist(id):
    artistData = artists[int(id)]
    artistAlbums = getArtistAlbums(artistData["albums"])
    return render_template('artistPage.html', artistData=artistData, artistAlbums=artistAlbums, genreIndex=genreIndex)


@app.route('/genre/<int:id>', methods=['GET'])
def genre(id):
    return render_template('genrePage.html', genreIndex=genreIndex)


@app.route('/album/<int:id>', methods=['GET'])
def song(id):
    return render_template('songPage.html', genreIndex=genreIndex)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
