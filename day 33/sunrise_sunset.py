import requests

LONG = 3.765860
LAT = 32.831228

parameters = {
    "lat": LAT,
    "lng": LONG
}
response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

print(data)
