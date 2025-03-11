import requests

parameters = {
    "lat": -21.176630,
    "lng": -47.820839,
    "formatted": 0,
    "tzid": "America/Sao_Paulo"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1]
sunset = data["results"]["sunset"].split("T")[1]

print(sunrise + "\n" + sunset)