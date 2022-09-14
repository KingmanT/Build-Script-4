# Build-Script-4
Repository for Build Script 4- Using API's to gather and organize data

Created by Kingman Tam for Kura Assignment Build Script 4.

This program is designed to provide the user with the times that the sun will rise and set in the area that they specify.
It utilizes 3 sources of API's: Google Maps, sunrise-sunset.org, and timeapi.io

The user will be prompted to provide and API key in order to use the Google Maps API.  Once they have provided a key, they will be prompted to enter a location for which they want sunrise/sunset data on.

The main API that will provide this information is from sunrise-sunset.org.  Unfortunately, they require that the location be input as a Longitude/Latitude pair.  This is where Google Maps is utilized.  Based on the location that the user inputs, a GET request is made to the Google Maps API will search for information about the location- including the best approximate long/lat coordinates.  The more specific the location is (address) the more accurate the geocoordinates will be.

The data is parsed and the coordinates are saved as variables which are then used in a GET request for the sunrise/sunset information.  Also unfortunately, the times that are provided are only in UTC time zone.  This is where timeapi.io is utilized.

Based on the Google Maps provided information, a GET request is made for the time zone information and a POST request is made to a time zone calculator API. This calculator takes the sunrise and sunset time (which needed to be formatted in the script) and the time zone (UTC) and returns information of the time zone of the location that the user specified.  Two separate POST requests are made for each time- sunrise and sunset.