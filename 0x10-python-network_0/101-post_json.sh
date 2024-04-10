#!/bin/bash
<<<<<<< HEAD
# This script sends a JSON POST request to a URL passed as the first argument, with the contents of a file passed as the second argument, and displays the body of the response

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File $2 does not exist."
    exit 1
fi

# Send the POST request and display the body of the response
=======
# This script sends a JSON POST request to a URL passed as the first argument, using the contents of a file passed as the second argument, and displays the body of the response

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File not found: $2"
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON content and display response body
>>>>>>> c3099ea39b023c39207629c04da03c62b072ed42
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

