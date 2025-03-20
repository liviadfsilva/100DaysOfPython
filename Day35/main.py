import requests

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "9924a81a577c76a5a40d1edd7d015519"


weather_params = {
    "lat": "-15.595100",
    "lon": "-56.092265",
    "appid": api_key,
    "cnt": 4
}

response = requests.get(weather_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_it_rain = False

for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 600:
        will_it_rain = True

if will_it_rain:
    print("Bring an umbrella.")


