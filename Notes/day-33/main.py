import requests
from datetime import datetime

MY_LAT = 32.392719
MY_LONG = -96.843880

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# coordinates = (longitude, latitude)

# print(coordinates)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()


print(sunrise)
print(sunset)

