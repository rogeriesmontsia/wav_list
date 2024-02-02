import requests
import os
API_URL = os.getenv("API_URL")
url = "{}trending/all/day?language=en-US".format(API_URL)

headers = {
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

print(response.text)