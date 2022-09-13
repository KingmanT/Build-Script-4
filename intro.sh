#!/bin/bash
#
# This script will be used to gather information from the user about what time zone they want information on
# and then use that input to get the sunrise/sunset information on that time zone.

echo "Welcome to the sunrise/sunset calculator"
echo "------------------------------------------"
read -p "Please press enter to continue or type 'exit' to quit program " ans1
echo "------------------------------------------"
if [[ $ans1 = "exit" ]]; then
    echo "Exiting program"
    echo "------------------------------------------"
    exit 0
fi
echo " "
echo "This program will allow you to check the time that"
echo "the sun will set and rise based on the location you enter"
echo " "
echo "------------------------------------------"
echo "Please enter the time zone or city of that you would like to get information about"
echo "------------------------------------------"
read inputlocation
echo "------------------------------------------"
echo "Please enter the date that you would like to get information on"
echo "------------------------------------------"
read inputdate

python3 build_script_4v1.py "$inputlocation" "$inputdate"

