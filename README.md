# Build-Script-4
Repository for Build Script 4- Using API's to gather and organize data

Created by Kingman Tam for Kura Assignment Build Script 4.

INSTRUCTIONS: 

1- Please make sure that the "Panda" module is installed onto your system in order to get a DataTable and CSV file at the end.
    -Panda can be installed onto your Ubuntu system with the command: pip install pandas
2- Make sure that both files: "SunTime-start.sh" and "SunTime_continued.py" are in the same directory and executable.
3- Google Maps API Key is required to run program.  Please have that key available as it is the first field that the user must input
    -Kura staff: Please contact Kingman for API key if one is not available
4- Run "SunTime_start.sh" to start script.


SCRIPT LOGIC:

1- Recieve input from user about 'API Key', 'Location', and 'Date'
2- Use 'API Key' and 'Location' to 'GET' 'longitude' and 'latitude'
3- Use 'longitude' and 'latitude' to 'GET' 'sunrise' and 'sunset' time in UTC (HH:MM:SS AM/PM)
4- Use 'Location' to 'GET' 'timezone'
5- Format 'time' to HH:MM:SS (24HR)
6- POST formatted 'time' and 'timezone' to conversion API to get local 'sunrise time' and 'sunset time' 
7- Create DataTable with Panda module and export to CSV


DESCRIPTION:

This program is designed to provide the user with the times that the sun will rise and set in the area that they specify.
It utilizes 3 sources of API's: Google Maps, sunrise-sunset.org, and timeapi.io

The user will be prompted to provide and API key in order to use the Google Maps API.  Once they have provided a key, they will be prompted to enter a location for which they want sunrise/sunset data on.

The main API that will provide this information is from sunrise-sunset.org.  Unfortunately, they require that the location be input as a Longitude/Latitude pair.  This is where Google Maps is utilized.  Based on the location that the user inputs, a GET request is made to the Google Maps API which will search for information about the location- including the best approximate long/lat coordinates.  The more specific the location is (address) the more accurate the geocoordinates will be.

The data is parsed and the coordinates are saved as variables which are then used in a GET request for the sunrise/sunset information.  Also unfortunately, the times that are provided are only in the UTC time zone.  This is where timeapi.io is utilized.

Based on the Google Maps provided information, a GET request is made for the IANA time zone information and a POST request is made to a time zone calculator API. This calculator takes the sunrise and sunset time (which needed to be formatted in the script) and the time zone (UTC) and returns information of the time zone of the location that the user specified.  Two separate POST requests are made for each time- sunrise and sunset.

The information is given to the user and the variables that were set are put into a dictionary which the Panda module uses to form a DataTable and a CSV file that is created in the current directory.  


ISSUES/BUG FIXES: 

FIXED 9/14/22 - This script will break if user enters a location where the sun will rise/set at 12:00PM to 12:59PM UTC. 
                Conversion to 24 format was done manually and 2400 hours to 2459 hours does not exist.  
FIXED 9/14/22 - This script will break if 1 digit hour is POST into conversion API.