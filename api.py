import requests
import json



def api1():
	response = requests.get('http://api.open-notify.org/astros.json')
	print(response.status_code)
	print(response.json())


def SpotifysimilarArtist():
	response = requests.get('	https://api.spotify.com/v1/artists/{id}/related-artists')

print(response.text)
print(response.json())

def Googlelocationapi():
url =https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyC6jkIC1gx-Ovi_iXztsuDNRaQkxzY2npw
myobj = {'lat': 'long': 'accuracy'}
data= json.dumps(myobj)
	response = requests.post(url,data)

print(response.text)
print(response.json())


def SpotifynewRelease():
	reponse= requests.get('https://api.spotify.com/v1/browse/new-releases')

print(response.text)
print(response.json())

def SpotifyRecommendation():
		reponse= requests.get('https://api.spotify.com/v1/recommendations')
print(response.text)
print(response.json())

def getAlbum():
			reponse= requests.get('https://api.spotify.com/v1/albums/{id}')
print(response.text)
print(response.json())


if __name__ == "__main__":
	# api1()
	# api2()
	# api3()
	# api4()
	# api5()
	api6()