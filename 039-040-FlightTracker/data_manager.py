from pprint import pprint
import requests
import os

SHEETY_ENDPOINT = "redacted"
BEARER_TOKEN = "redacted"
SHEETY_USERS = "redacted"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        # pprint(data)
        # print(response.text)
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
                url=f"{SHEETY_ENDPOINT}/{city["id"]}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS
        response = requests.get(url=customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data