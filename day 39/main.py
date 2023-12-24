#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

response = requests.get(url='https://api.sheety.co/b35a68f81a770a7ae5c6269e80e18086/flightDeals/prices')
data = response.json()
print(data)