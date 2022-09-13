#!/usr/bin/python3

import requests
import json

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2021-03-14" " 10:33:36",
  "toTimeZone": "America/New_York",
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())