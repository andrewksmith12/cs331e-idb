# #!/usr/bin/env python3


# import json
# import os
# from models import app, db, Artist, Song, Album, Song_Artist, Song_Album  # , Location
# query = db.session.query
# add = db.session.add
# commit = db.session.commit

# # ------------
# # load_json
# # ------------


# def load_json(filename):
#     """
#     return a python dict jsn
#     filename a json file
#     """
#     with open(filename) as file:
#         jsn = json.load(file)
#         file.close()

#     return jsn


# datafile = os.path.join(app.static_folder, 'data', 'dbdata.json')
# data = load_json(datafile)
# length = len(data)

# track_id = 0
# album_id = 0
# artist_id = 0

# next_album_id = 0
# next_artist_id = 0

# tracks = [""]*length
# albums = [""]*length
# artists = [""]*length

# previous_track = ""
# previous_album = ""
# previous_artist = ""

# for item in data:
#     track = item['track']
#     album = item['album']
#     artist = item['artist']

#     # Optimization to avoid indexing a thousand entry dictionary
#     if artist != previous_artist:
#         if artist in artists:
#             artist_id = artists.index(artist)
#         else:
#             artist_id = next_artist_id
#             artists[artist_id] = artist
#             next_artist_id += 1
#             newArtist = Artist(name=artist, id=artist_id)
#             add(newArtist)

#     if album != previous_album:
#         if album in albums:
#             album_id = albums.index(album)
#         else:
#             album_id = next_album_id
#             albums[album_id] = album
#             next_album_id += 1
#             newAlbum = Album(title=album, id=album_id)
#             add(newAlbum)

#     tracks[track_id] = track
#     track_id += 1
#     newTrack = Song(title=track, id=track_id)
#     add(newTrack)

#     newSongArtist = Song_Artist(artist_id=artist_id, song_id=track_id)
#     add(newSongArtist)
#     newSongAlbum = Song_Album(album_id=album_id, song_id=track_id)
#     add(newSongAlbum)
#     commit()
