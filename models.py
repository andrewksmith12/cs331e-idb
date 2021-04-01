#!/usr/bin/env python3

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Table, Column, Integer, ForeignKey
from flask_sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DB_STRING', 'postgres://postgres:asd123@localhost:5432/bookdb')
# to suppress a warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

artist_song_table = Table('association', Base.metadata,
                          Column('artist_id', Integer,
                                 ForeignKey('artist.id')),
                          Column('song_id', Integer,
                                 ForeignKey('album.id'))
                          )

song_album_table = Table('association', Base.metadata,
                         Column('album_id', Integer,
                                ForeignKey('artist.id')),
                         Column('song_id', Integer,
                                ForeignKey('album.id'))
                         )


class Artist(db.Model):
    # Artist has two primary attributes, ID and name

    __tablename__ = 'artist'

    name = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    songs = relationship(
        'Song', secondary=artist_song_table, backpopulates="artists")

    albums = relationship("Album", lazy="joined", innerjoin=True)

    """genres = relationship('Genre',
                          secondary=artist_genre_table,
                          backpopulates='artists')"""


class Song(db.Model):
    # Song is dependent on album, and can be identified by the position in that album

    __tablename__ = 'song'

    title = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    artists = relationship(
        'Artist', secondary=artist_song_table, backpopulates="songs")
    albums = relationship(
        'Album', secondary=song_album_table, backpopulates="songs")


class Album(db.Model):
    # Album also has two primary attributes, ID and name

    __tablename__ = 'album'

    title = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    songs = relationship('Song',
                         secondary=song_album_table,
                         backpopulates='albums')

    artists = relationship('Artist', lazy="joined", innerjoin=True)

    """genres = relationship('Genre',
                          secondary=artist_genre_table,
                          backpopulates='albums')"""


"""class Genre(db.Model):

    __tablename__ = 'genre'

    name = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    artists = relationship('Artist',
                           secondary=artist_album_table,
                           backpopulates='genres')

    albums = relationship('Album',
                          secondary=artist_album_table,
                          backpopulates='genres')"""


db.drop_all()
db.create_all()
