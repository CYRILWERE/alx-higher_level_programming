#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign the URL to a variable
url=$1

# Send a POST request with curl, passing email and subject parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"

