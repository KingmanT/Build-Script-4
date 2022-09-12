#!/bin/bash
#
# This script will be used to gather information from the user about what time zone they want information on
# and then use that input to get the sunrise/sunset information on that time zone.

echo "Welcome to the sunrise/sunset calculator"
read -p "Please press enter to continue or type 'exit' to quit program " ans1
if [[ $ans1 = "exit" ]]; then
echo "Exiting program"
exit 0
fi
echo "so far so good"