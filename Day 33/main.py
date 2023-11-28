import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LNG = -0.127758

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# lon = data["iss_position"]["longitude"]
# lat = data["iss_position"]["latitude"]
# pos = (lon, lat)
# print(data, "\n", pos)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
print(time_now.minute)
