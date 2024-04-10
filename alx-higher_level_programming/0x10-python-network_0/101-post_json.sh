#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, with the contents of a file passed as the second argument, and displays the body of the response

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File $2 does not exist."
    exit 1
fi

# Send the POST request and display the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

