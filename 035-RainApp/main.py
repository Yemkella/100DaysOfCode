import requests
import os
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LONG = redacted
LAT = redacted
KEY = "redacted"
SECRET = "redacted"

account_sid = "redacted"
auth_token = "redacted"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": KEY,
    "cnt": 4
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()

will_rain = False
condition_code_list = [data["list"][x]["weather"][0]["id"] for x in range(0, 4)]
for code in condition_code_list:
    if int(code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella!",
                     from_="+redacted",
                     to="+redacted"
                 )

    print(message.sid)