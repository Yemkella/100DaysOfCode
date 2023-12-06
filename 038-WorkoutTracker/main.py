import requests
from datetime import datetime
import os

SYNDIGO_APP_ID = os.environ.get("SYNDIGO_APP_ID")
SYNDIGO_API_KEY = os.environ.get("SYNDIGO_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_URL = os.environ.get("SHEETY_URL")
host_domain = "https://trackapi.nutritionix.com"
endpoint = "/v2/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": SYNDIGO_APP_ID,
    "x-app-key": SYNDIGO_API_KEY,
}

user_params = {
    "query": input("Tell me which exercise you did: "),
}

response = requests.post(url=f"{host_domain}{endpoint}", headers=headers, json=user_params)
data = response.json()

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

sheety_response = requests.post(url=SHEETY_URL, json=sheet_inputs, headers=sheety_header)

print("Exercise documented!")