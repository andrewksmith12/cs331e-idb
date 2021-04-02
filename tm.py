import requests
import subprocess 
KEY = 'hSTvLnkFPALEILu8u0TUOIPyuFDDSxmj'
SECRET = 'Erw8A7xJyKBcLRhO'
BASE_URL = 'https://app.ticketmaster.com/discovery/v2/'

#header={'key':'{key}'.format(key=KEY)}

r = requests.get(BASE_URL + 'events/', params={'keyword':'taylor swift', 'apikey':KEY})
stringme = str(r.json())
subprocess.run("pbcopy", universal_newlines=True, input=stringme)
