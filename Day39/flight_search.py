import requests
import os
from dotenv import load_dotenv

ACCESS_TOKEN = "qksIWnCGbJJ36ak8pOgcZXNESi3K"
FLIGHT_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("FLIGHT_SEARCH_API_KEY")
        self.api_secret = os.getenv("FLIGHT_SEARCH_API_SECRET")

        self.get_token_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self.header = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }

        self.body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

    def get_token(self):
        response = requests.post(url=FLIGHT_TOKEN_ENDPOINT, headers=self.get_token_header, data=self.body)
        return response.text

    def get_city(self, city_name):
        city = {
            "keyword": city_name
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=self.header, params=city)
        return response.json()

    def get_offers(self, destination, price, date):
        my_header = self.header
        query = {
            "originLocationCode": "LGW",
            "destinationLocationCode": destination,
            "departureDate": date,
            "adults": "1",
            "currencyCode": "GBP",
            "maxPrice": price
        }
        response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, params=query, headers=my_header)

        return response.json()

# new_token = FlightSearch().get_token()
# print(new_token)