import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from datetime import datetime, timedelta

tomorrow = datetime.now() + timedelta(days=2)
date = tomorrow.strftime("%Y-%m-%d")

from flight_search import FlightSearch

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5109a664bda0cebc8a10944188eb7b5e/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.username, self.password)

    def get_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.authorization)
        return response.json()

    # def add_codes(self):
    #     flight_data = FlightSearch()
    #     all_data = self.get_data()["prices"]
    #
    #     responses = []
    #
    #     for nr in all_data:
    #         destination_city = nr["city"]
    #         iata_code = flight_data.get_city(destination_city)["data"][0]["iataCode"]
    #
    #         body = {
    #             "price": {
    #                 "iataCode": iata_code
    #             }
    #         }
    #
    #         row_id = nr["id"]
    #
    #         response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", auth=self.authorization, json=body)
    #
    #         responses.append(response.text)
    #
    #     return responses

    def update_price(self):
        responses = []
        data = DataManager()
        fetch_data = data.get_data()["prices"]

        for i in fetch_data:
            destination = i["iataCode"]
            price = i["lowestPrice"]

            flight_search = FlightSearch()
            result = flight_search.get_offers(destination, price, date)

            total = result["data"][0]["price"]["total"]

            body = {
                "price": {
                    "lowestPrice": total
                }
            }

            row_id = i["id"]

            if int(total) <= int(price):
                response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", auth=self.authorization, json=body)
                responses.append(response.text)

        return responses