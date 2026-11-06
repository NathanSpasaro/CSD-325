# Nathan Spasaro
# CSD-325 Module 9.2
# Date: 11/6/2026
# Purpose: Retrieve and format astronaut data using an API.

import requests
import json

response = requests.get('http://api.open-notify.org/astros.json', timeout=10)
print(response.status_code)

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())