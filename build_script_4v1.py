#!/usr/bin/python3

# This script was created by Kingman Tam for Build Script 4.  Script started on 9/12/22.  
# This script is to be used in conjunction with BASH script to use API's 
#
#
# ISSUES: This script will break if user enters a location where the sun will rise/set at 12:00PM to 12:59PM.  Conversion to 24 format was done 
# manually and 2400 hours to 2459 hours does not exist. Will add rule for this bug at later time.  

import json
import sys
import requests

latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + (sys.argv[1]) + '&key=' + (sys.argv[3]))
# latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=new york&key=')
# print(latlong.json())
latitude = latlong.json()['results'][0]['geometry']['location']['lat']
longitude = latlong.json()['results'][0]['geometry']['location']['lng']
print("line 19-", latitude)
print("line 20-", longitude)

# print(sys.argv)
# print(sys.arg[1])
# suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=40.7127753,&lng=-74.0059728&date=9/12/22')
# suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=9/13/22')
suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=' + str(sys.argv[2]))
# print(suninfo.json())
sunriseutc = suninfo.json()['results']['sunrise']
sunsetutc = suninfo.json()['results']['sunset']
print("line 30-", sunriseutc)
print("line 31-", sunsetutc)

# timezone = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=38.9&longitude=-77.03')
timeinfo = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=' + str(latitude) + '&longitude=' + str(longitude))
timezone = timeinfo.json()['timeZone']
print("line 36-", timezone)

if sunriseutc.split()[1] == "PM":
    hour = sunriseutc.split()[0]
    # print(hour)
    hh = int(hour.split(':')[0])
    if hh == 12:
        hh24 = str(12)
    else:
        hh24 = str(hh + 12) 
        # print(hh24)
    sunrise24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    print(sunrise24)

elif sunriseutc.split()[1] == "AM":
    hour = sunriseutc.split()[0]
    hh = int(hour.split(":")[0])
    if hh == 12:
        hh24 = "00"
        sunrise24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    else:
        sunrise24 = sunriseutc.split()[0]
    print(sunrise24)

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2021-03-14 " f'{sunrise24}',
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
    if hh == 12:
        hh24 = str(12)
    else:
        hh24 = str(hh + 12) 
        # print(hh24)
    sunset24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    print(sunset24)

elif sunsetutc.split()[1] == "AM":
    hour = sunsetutc.split()[0]
    hh = int(hour.split(":")[0])
    if hh == 12:
        hh24 = "00"
        sunset24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    else:
        sunset24 = sunsetutc.split()[0]
    print(sunset24)

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2021-03-14 " f'{sunset24}',
  "toTimeZone": f'{timezone}',
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json()['conversionResult']['time'])