#!/usr/bin/python3

import json
import sys
import requests

latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + (sys.argv[1]) + '&key=' + (sys.argv[3]))
# latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=new york&key=')
# print(latlong.json())
latitude = latlong.json()['results'][0]['geometry']['location']['lat']
longitude = latlong.json()['results'][0]['geometry']['location']['lng']
print("line 12-", latitude)
print("line 13-", longitude)

# print(sys.argv)
# print(sys.arg[1])
# suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=40.7127753,&lng=-74.0059728&date=9/12/22')
# suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=9/13/22')
suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=' + str(sys.argv[2]))
# print(suninfo.json())
sunriseutc = suninfo.json()['results']['sunrise']
sunsetutc = suninfo.json()['results']['sunset']
print("line 23-", sunriseutc)
print("line 24-", sunsetutc)

# timezone = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=38.9&longitude=-77.03')
timeinfo = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=' + str(latitude) + '&longitude=' + str(longitude))
timezone = timeinfo.json()['timeZone']
print("line 29-", timezone)

if sunriseutc.split()[1] == "PM":
    hour = sunriseutc.split()[0]
    # print(hour)
    hh = int(hour.split(':')[0])
    hhh = str(hh + 12) 
    # print(hhh)
    sunrise = hhh + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    print("line 38-", sunrise)

elif sunriseutc.split()[1] == "AM":
    sunrise = sunriseutc.split()[0]
    print("line 42-", sunrise)

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2021-03-14 " f'{sunrise}',
  "toTimeZone": f'{timezone}',
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json()['conversionResult']['time'])

if sunsetutc.split()[1] == "PM":
    hour = sunsetutc.split()[0]
    # print(hour)
    hh = int(hour.split(':')[0])
    hhh = str(hh + 12) 
    # print(hhh)
    sunset = hhh + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    print("line 66-", sunset)

elif sunseteutc.split()[1] == "AM":
    sunset = sunsetutc.split()[0]
    print("line 70-", sunset)

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2021-03-14 " f'{sunset}',
  "toTimeZone": f'{timezone}',
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json()['conversionResult']['time'])