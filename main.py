import requests
import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
apy_key = os.environ["api_key"]
number = os.environ["number"]

#Uruguay COORD
# LAT = "44.513290"
# LONG = "-88.013260"

LAT = "42.672829"
LONG = "-82.916458"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": apy_key,
    "exclude": "minutely,current,daily"

    }

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
id = data["hourly"][0:12]


cond_code = []
will_rain = False
for i in range(len(id)):
    cond_code.append(id[i]["weather"][0]["id"])
for item in cond_code:
    if item < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its going to rain",
        from_= number,
        to=''
    )
    print(message.status)