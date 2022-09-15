#!/usr/bin/python3

##################################################################################################################################
# Created by Kingman Tam for Build Script 4.  Script started on 9/12/22.  
#
# This script is to be used in conjunction and STARTED with BASH script titled "SunTime_start.sh" to use API's to gather information.
# This script will take information from the user input from BASH script and then 
# use that input to get the sunrise/sunset information on that time zone.
#
# Please read README.md for full notes on script.
#
# ISSUES: FIXED 9/14/22 -This script will break if user enters a location where the sun will rise/set at 12:00PM to 12:59PM UTC. 
#                       Conversion to 24 format was done manually and 2400 hours to 2459 hours does not exist.  
#         FIXED 9/14/22 -This script will break if 1 digit hour is POST into conversion API.
###################################################################################################################################

# import modules required for script to run

import json
import sys
import requests
import pandas as pd
import time

# GET request made to Google for latitude and logitude using user input location and key

latlong = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + (sys.argv[1]) + '&key=' + (sys.argv[3]))
latitude = latlong.json()['results'][0]['geometry']['location']['lat']
longitude = latlong.json()['results'][0]['geometry']['location']['lng']

print("------------------------------------------")
print(" ")
time.sleep(1)
print("Based on the Location you entered, it's approximate latitude and longitude are:", latitude, ",", longitude)
print(" ")

# GET request made to sunrise-sunset.org for sunrinse/sunset times in UTC using latitude and longitude

suninfo = requests.get('https://api.sunrise-sunset.org/json?lat=' + str(latitude) + ',&lng=' + str(longitude) + '&date=' + str(sys.argv[2]))
sunriseutc = suninfo.json()['results']['sunrise']
sunsetutc = suninfo.json()['results']['sunset']

time.sleep(1)
print("Using those coordinates, the sun will rise on that location at:", sunriseutc, "UTC, and the sun will set on that location at:", sunsetutc, "UTC.")
print(" ")

# GET request made to timeapi.io for timezone using latitude and longitude

timeinfo = requests.get('https://timeapi.io/api/TimeZone/coordinate?latitude=' + str(latitude) + '&longitude=' + str(longitude))
timezone = timeinfo.json()['timeZone']

time.sleep(1)
print("Let's convert that time into the local time for that area.")
print(" ")
time.sleep(1)
print("Based on those geocoordinates, the IANA timezone name for that area is:", timezone)
print(" ")

# Format sunrise UTC time to 24hr format

if sunriseutc.split()[1] == "PM":
    hour = sunriseutc.split()[0]
    hh = int(hour.split(':')[0])
    if hh == 12:
        hh24 = str(12)
    else:
        hh24 = str(hh + 12) 
    sunriseutc24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]

elif sunriseutc.split()[1] == "AM":
    hour = sunriseutc.split()[0]
    hh = int(hour.split(":")[0])
    if hh == 12:
        hh24 = "00"
        sunriseutc24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    elif hh >= 10:
        sunriseutc24 = sunriseutc.split()[0]
    else:
        hh24 = "0" + str(hh)
        sunriseutc24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]

# POST request for local time conversion using 24hour sunrise time and user timezone

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2022-09-14 " f'{sunriseutc24}',
  "toTimeZone": f'{timezone}',
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

sunrisepost = requests.request("POST", url, headers=headers, data=payload)

# Local time for sunrise

sunriselocal = sunrisepost.json()['conversionResult']['time']

# Format sunset UTC time to 24hr format

if sunsetutc.split()[1] == "PM":
    hour = sunsetutc.split()[0]
    hh = int(hour.split(':')[0])
    if hh == 12:
        hh24 = str(12)
    else:
        hh24 = str(hh + 12) 
    sunsetutc24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]

elif sunsetutc.split()[1] == "AM":
    hour = sunsetutc.split()[0]
    hh = int(hour.split(":")[0])
    if hh == 12:
        hh24 = "00"
        sunsetutc24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    elif hh >= 10:
        sunsetutc24 = sunsetutc.split()[0]
    else:
        hh24 = "0" + str(hh)
        sunsetutc24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]

# POST request for local time conversion using 24hour sunset time and user timezone

url = "https://timeapi.io/api/Conversion/ConvertTimeZone"
payload = json.dumps({
  "fromTimeZone": "UTC",
  "dateTime": "2022-09-14 " f'{sunsetutc24}',
  "toTimeZone": f'{timezone}',
  "dstAmbiguity": ""
})
headers = {
  'Content-Type': 'application/json'
}

sunsetpost = requests.request("POST", url, headers=headers, data=payload)

# local time for sunset

sunsetlocal = sunsetpost.json()['conversionResult']['time']

print("Converting UTC time to", timezone, "time..")
time.sleep(2)
print(" ")

# Print statements for sunrise and sunset in local time

print("------------------------------------------")
print("On", sys.argv[2], "the sun will rise in", sys.argv[1], "at", sunriselocal)
print("On", sys.argv[2], "the sun will set in", sys.argv[1], "at", sunsetlocal)
print("------------------------------------------")
print(" ")
time.sleep(1)

# Create a dictionary and use Panda to create DataTable and CSV

dictionary = {"Date": sys.argv[2], "Location": sys.argv[1],  "Latitude": latitude, "Longitude": longitude, "Sunrise": sunriselocal, "Sunset": sunsetlocal}
df = pd.DataFrame([dictionary])
df.set_index("Date",inplace=True)
df.to_csv("./suninfo.csv")

print("For your reference, a CVS file has been created of the information provided here")
print(" ")
print("Thank you for using this program.  Enjoy the rest of your day!")
print(" ")

