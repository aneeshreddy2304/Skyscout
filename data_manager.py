import os
from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT", "")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        if not SHEETY_PRICES_ENDPOINT:
            raise RuntimeError("Set SHEETY_PRICES_ENDPOINT in the process environment")
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        if not SHEETY_PRICES_ENDPOINT:
            raise RuntimeError("Set SHEETY_PRICES_ENDPOINT in the process environment")
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
