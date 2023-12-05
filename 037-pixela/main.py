import requests
from datetime import datetime

USERNAME = "redacted"
TOKEN = "redacted"
MINUTES_CODING = "120"
GRAPH_ID = "redacted"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Used the below text to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "float",
    "color": "shibafu",
    "timezone": "US/Central"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Used this code below to create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

add_pixels_config = {
    "date": today_formatted,
    "quantity": MINUTES_CODING,
}

add_pixels_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Used this code below to add pixels to graph
# response = requests.post(url=add_pixels_endpoint, json=add_pixels_config, headers=headers)
# print(response.text)

# Update the {today_formatted} portion if needed
update_pixels_endpoint = f"{add_pixels_endpoint}/{today_formatted}"

update_pixels_config = {
    "quantity": "145"
}

# Used this code below to update a pixel on a graph
# response = requests.put(url=update_pixels_endpoint, headers=headers, json=update_pixels_config)
# print(response.text)

date_to_delete = "20231204"
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"

# Used this code below to delete a pixel on a graph
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)