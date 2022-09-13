#!/usr/bin/python3

import json
import sys
import requests

latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + (sys.argv[1]) + '&key=')
# latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=new york&key=')
# print(latlong.json())
latitude = latlong.json()['results'][0]['geometry']['location']['lat']
longitude = latlong.json()['results'][0]['geometry']['location']['lng']
print(latitude)
print(longitude)

# print(sys.argv)
# print(sys.arg[1])
# suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=40.7127753,&lng=-74.0059728&date=9/12/22')
# suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=9/13/22')
suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=' + str(sys.argv[2]))
# print(suninfo.json())
sunrise = suninfo.json()['results']['sunrise']
sunset = suninfo.json()['results']['sunset']
print(sunrise)
print(sunset)

# timezone = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=38.9&longitude=-77.03')
timeinfo = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=' + str(latitude) + '&longitude=' + str(longitude))
timezone = timeinfo.json()['timeZone']
print(timezone)

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2021-03-14 17:45:00",
  "toTimeZone": f'{timezone}',
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)