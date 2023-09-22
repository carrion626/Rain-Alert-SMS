import requests
import info
from twilio.rest import Client

api_key = info.api_k
account_sid = info.account_s
auth_token = info.auth_t

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Whatever you want",
                     from_=info.number_from,
                     to=info.number_to
                 )

print(message.status)

# Coordinates in a format which is below (example coordinates: Ukraine)
parameters = {
        'lat': 48.6166642,
        'lon': 22.2999988,
        'appid': api_key,
    }


respond = requests.get(url=info.url, params=parameters)
respond.raise_for_status()

weather_data = respond.json()
print(weather_data)

weather_id = weather_data['weather'][0]['id']
print(weather_id)

# Condition if the weather will be rainy to send the message (in this example just print to console)
if 500 < weather_id < 532:
    print('Take an umbrella')
