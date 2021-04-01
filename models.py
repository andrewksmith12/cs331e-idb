#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Table, Column, Integer, ForeignKey
from flask_sqlalchemy.orm import relationship
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DB_STRING", 'postgres://postgres:asd123@localhost:5432/bookdb')
# to suppress a warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

artist_album_table = Table('association', Base.metadata,
                           Column("artist_id", Integer,
                                  ForeignKey("artist.id")),
                           Column("album_id", Integer,
                                  ForeignKey("album.id"))
                           )

artist_genre_table = Table('association', Base.metadata,
                           Column('artist_id', Integer,
                                  ForeignKey('artist.id')),
                           Column('genre_id', Integer, ForeignKey('artist.id'))
                           )

album_genre_table = Table('association', Base.metadata,
                          Column('album_id', Integer,
                                 ForeignKey('album.id')),
                          Column('genre_id', Integer, ForeignKey('artist.id'))
                          )


class Artist(db.Model):
    # Artist has two primary attributes, ID and name

    __tablename__ = "artist"

    name = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    albums = relationship("Album",
                          secondary=artist_album_table,
                          backpopulates="artists")

    genres = relationship("Genre",
                          secondary=artist_genre_table,
                          backpopulates="artists")


class Album(db.Model):
    # Album also has two primary attributes, ID and name

    __tablename__ = "album"

    name = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    artists = relationship("Artist",
                           secondary=artist_album_table,
                           backpopulates="albums")

    genres = relationship("Genre",
                          secondary=artist_genre_table,
                          backpopulates="albums")


class Song(db.Model):
    # Song is dependent on album, and can be identified by the position in that album

    __tablename__ = "song"

    name = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    album_id = Column(Integer, ForeignKey("album.id"))
    album = relationship("Album", backref="songs")


class Genre(db.Model):

    __tablename__ = "genre"

    name = Column(db.String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    artists = relationship("Artist",
                           secondary=artist_album_table,
                           backpopulates="genres")

    albums = relationship("Album",
                          secondary=artist_album_table,
                          backpopulates="genres")


db.drop_all()
db.create_all()
