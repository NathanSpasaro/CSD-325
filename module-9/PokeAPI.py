# Nathan Spasaro
# CSD-325 Module 9.2
# Date: 11/6/2026
# Purpose: Retrieve and format Pokemon generation data using an API.

import requests
import json
# Request Pokemon generation data from the API.
response = requests.get('https://pokeapi.co/api/v2/generation/?limit=2', timeout=10)

# Create a formatted string of the Python JSON object.
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Display the HTTP status code.
print("HTTP Status Code:", response.status_code)

# Display the unformatted API response.
print("\nUnformatted API Response:")
print(response.text)

# Display the formatted API response.
print("\nFormatted API Response:")
jprint(response.json())