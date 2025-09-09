from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a552ba6fed4e9da316a5f835a59c27d4/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url="https://api.sheety.co/a552ba6fed4e9da316a5f835a59c27d4/flightDeals/prices")
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
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
