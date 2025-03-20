import requests
import smtplib
import os

my_email = "parakeet.test013@gmail.com"
password = os.environ.get("email_test_password")

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("weather_map_api_key")


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
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="macaw.test011@yahoo.com",
                            msg=f"Subject: Rain alert!\n\n It's going to rain today. Remember to bring an umbrella.")