#!/bin/bash
#
# This script was created by Kingman Tam for Build Script 4.  Script started on 9/12/22. 
# This script will be used to gather information from the user about what time zone they want information on
# and then use that input to get the sunrise/sunset information on that time zone.

echo " "
echo "Welcome to the sunrise/sunset calculator"
echo "------------------------------------------"
echo "Please note that this program requires a Google Maps API key in order to work." 
echo "Enter your Google Maps API key to continue or type 'exit' to quit program "
echo "------------------------------------------"
read key
if [[ $key = "exit" ]]; then
    echo "Exiting program"
    echo "------------------------------------------"
    exit 0
fi
echo " "
echo "This program will allow you to check the time that"
echo "the sun will set and rise based on the location you enter"
echo " "
echo "------------------------------------------"
echo "Please enter the location that you would like to get information about"
echo "------------------------------------------"
read inputlocation
echo "------------------------------------------"
echo "Please enter the date that you would like to get information on"
echo "------------------------------------------"
read inputdate

python3 build_script_4v1.py "$inputlocation" "$inputdate" "$key"

