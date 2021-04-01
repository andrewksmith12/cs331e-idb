#!/usr/bin/env python3


import json
import os
from models import app, db, Artist, Song, Album, Location

# ------------
# load_json
# ------------

datafile = os.path.join(app.static_folder, 'data', 'data.json')
data = json.load(open(datafile))
artists = data["artists"]
locationsData = data["locations"]
albums = data["albums"]
songs = data["songs"]


def load_json(filename):
    """
    return a python dict jsn
    filename a json file
    """
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# ------------
# create_artists
# ------------


def create_artists():
    """
    populate artist table
    """

    for artist in artists:
        name = artist['name']
        id = artist['id']

        newArtist = Artist(name=name, id=id)
        db.session.add(newArtist)
        db.session.commit()


def create_songs():
    """
    populate songs table
    """
    for song in songs:
        title = song['title']
        id = song['id']
        artists = song['artists']
        albums = song['albums']

        newSong = Song(title=title, id=id, artists=artists, albums=albums)
        db.session.add(newSong)
        db.session.commit()


def create_albums():
    """
    populate albums table
    """
    for album in albums:
        title = album['title']
        id = album['id']
        newAlbum = Album(title=title, id=id)
        db.session.add(newAlbum)
        db.session.commit()


create_artists()
