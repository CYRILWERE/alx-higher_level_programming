#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response

# Sending the request and storing the response in a temporary file
curl -s -o response.txt -w "%{http_code}" "$1"

# Extracting the status code from the file and displaying it
cat response.txt
rm -f response.txt  # Remove the temporary file

