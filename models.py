#!/usr/bin/env python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DB_STRING', 'postgresql://postgres:asd123@localhost:5432/musicforyou')
# to suppress a warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.metadata.clear()

"""artist_song_table = Table('song_to_artist', Base.metadata,
                          Column('artist_id', Integer,
                                 ForeignKey('artist.c.id')),
                          Column('song_id', Integer,
                                 ForeignKey('song.c.id'))
                          )

song_album_table = Table('song_to_album', Base.metadata,
                         Column('album_id', Integer,
                                ForeignKey('album.id')),
                         Column('song_id', Integer,
                                ForeignKey('song.id'))
                         )"""


class Song_Artist(db.Model):
    __tablename__ = 'song_to_artist'
    artist_id = Column(db.String(30), ForeignKey('artist.id'), primary_key=True)
    song_id = Column(db.String(30), ForeignKey('song.id'), primary_key=True)
    artist = relationship("Artist", back_populates="songs")
    song = relationship("Song", back_populates="artists")



class Song_Album(db.Model):
    __tablename__ = 'song_to_album'
    album_id = Column(db.String(30), ForeignKey('album.id'), primary_key=True)
    song_id = Column(db.String(30), ForeignKey('song.id'), primary_key=True)
    album = relationship("Album", back_populates="songs")
    song = relationship("Song", back_populates="albums")



class Artist(db.Model):
    # Artist has two primary attributes, ID and name

    __tablename__ = 'artist'
    name = Column(db.String(140), nullable=False)
    id = Column(db.String(30), primary_key=True)
    songs = relationship("Song_Artist", back_populates="artist")
    thumbnail = Column(db.String(200))


class Song(db.Model):
    # Song is dependent on album, and can be identified by the position in that album

    __tablename__ = 'song'

    title = Column(db.String(140), nullable=False)
    id = Column(db.String(30), primary_key=True)
    artists = relationship("Song_Artist", back_populates="song")
    albums = relationship("Song_Album", back_populates="song")
    release_date = Column(db.String(60))
    thumbnail = Column(db.String(200))


class Album(db.Model):
    # Album also has two primary attributes, ID and name

    __tablename__ = 'album'
    title = Column(db.String(140), nullable=False)
    id = Column(db.String(30), primary_key=True)
    songs = relationship("Song_Album", back_populates="album")
    thumbnail = Column(db.String(200))
    artist = relationship("Artist")
    artistID = Column(db.String(30), ForeignKey(Artist.id))
