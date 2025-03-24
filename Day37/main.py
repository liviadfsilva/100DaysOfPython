import requests
from datetime import datetime
import os

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "liviadfsilva"
ID = "medgraph13"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": ID,
    "name": "Meditation Graph",
    "unit": "sessions",
    "type": "int",
    "color": "ajisai"
}

# response = requests.post(url= graph_endpoint, json=graph_config, headers=header)
# print(response.text)

a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime(year=2025, month=3, day=23)
formatted_data = today.strftime("%Y%m%d")

a_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many times did you meditate today?")
}

quantity = {
    "quantity": "5"
}

put_or_delete_api_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formatted_data}"

# response = requests.post(url= a_pixel_endpoint, json=a_pixel_config, headers=header)

# response = requests.put(url= put_or_delete_api_endpoint, json=quantity, headers=header)

response = requests.delete(url= put_or_delete_api_endpoint, headers=header)
print(response.text)