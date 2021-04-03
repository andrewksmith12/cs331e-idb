from unittest import TestCase
from models import db, Artist, Song, Album
import requests

db.drop_all()

class TestApplication(TestCase):
    def test1(self):
        #Ensure API authentication is working
        CLIENT_ID = "adcb7fe6a96a4e4db325d9c5440b0419"
        CLIENT_SECRET = "51eaeca06fae4f0383bf7b298d7c3773"
        AUTH_URL = "https://accounts.spotify.com/api/token"
        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })
        self.assertEqual(auth_response.status_code, '200')

    def test2(self):
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
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        test_artist_uri = '1ad0OVCVHS0twEyPoRHNkR'
        r = requests.get(BASE_URL + 'artists/' + test_artist_uri,
                        headers=auth_header, params={'market': 'US'})
        data = r.json()
        self.assertEqual(data['name'],"Arioid")
    def testArtist1(self):
        testArtist = Artist(name="Darius Rucker", id=1)
        db.session.add(testArtist)
        r = db.session.query(Artist).filter(id=1).one()
        self.assertEqual(str(r.id), '1')
        self.assertEqual(str(r.name), 'Darius Rucker')
    def testArtist2(self):
        testArtist = Artist(name="Andrew Rucker", id=2)
        db.session.add(testArtist)
        r = db.session.query(Artist).filter(id=1).one()
        self.assertEqual(str(r.id), '2')
        self.assertEqual(str(r.name), 'Andrew Rucker')
    def testArtist3(self):
        testArtist = Artist(name="John Rucker", id=3)
        db.session.add(testArtist)
        r = db.session.query(Artist).filter(id=1).one()
        self.assertEqual(str(r.id), '3')
        self.assertEqual(str(r.name), 'John Rucker')
    def testSong1(self):
        testSong = Song(title="Bow Chicka Bow Wow", id=5)
        db.session.add(testSong)
        r = db.session.query(Song).filter(id=5).one()
        self.assertEqual(str(r.id), '5')
        self.assertEqual(str(r.name), 'Bow Chicka Bow Wow')
    def testSong2(self):
        testSong = Song(title="Bow Bow Chica Wow", id=8)
        db.session.add(testSong)
        r = db.session.query(Song).filter(id=8).one()
        self.assertEqual(str(r.id), '8')
        self.assertEqual(str(r.name), 'Bow Bow Chica Wow')
    def testSong3(self):
        testSong = Song(title="Chica Chica Bow Wow", id=12)
        db.session.add(testSong)
        r = db.session.query(Song).filter(id=12).one()
        self.assertEqual(str(r.id), '12')
        self.assertEqual(str(r.name), 'Chica Chica Bow Wow')