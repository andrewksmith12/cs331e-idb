from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from models import app, db, Artist, Song, Album
import random
import requests
import os
import subprocess

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
    'Authorization' : 'Bearer {token}'.format(token=access_token)
}


r = requests.get(BASE_URL + 'artists/' + '4kYSro6naA4h99UJvo89HB', headers=auth_header, params={'market': 'US'})
artistTracks = r.json()
subprocess.run("pbcopy", universal_newlines=True, input=str(artistTracks))

print(artistTracks)