import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = datetime.time(now).strftime("%H:%M:%S")

#Nutritionix info
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

#Sheety info
sheety_url = os.getenv("SHEETY_URL")
sheety_username = os.getenv("SHEETY_USERNAME")
sheety_project = os.getenv("SHEETY_PROJECT")

#Nutritionix request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": input("Tell me which exercises you did: ")
}

nutri_response = requests.post(url=nutri_endpoint, headers=headers, json=body)
nutri_data = nutri_response.json()

exercise = nutri_data["exercises"][0]["name"].title()
duration = nutri_data["exercises"][0]["duration_min"]
calories = nutri_data["exercises"][0]["nf_calories"]

# #Sheety request
sheety_headers = {
    "Authorization": os.getenv("SHEETY_AUTHORIZATION")
}

sheety_data = {
    "workout": {
    "date": date,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
    }
}

sheety_response =  requests.post(url=sheety_url, headers=sheety_headers, json=sheety_data)
print(sheety_response.json())