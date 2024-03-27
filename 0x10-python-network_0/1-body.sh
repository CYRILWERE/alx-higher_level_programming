#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X GET "$1" -w "%{http_code}" -o temp_body.txt
status_code=$(tail -n1 temp_body.txt)
if [ $status_code -eq 200 ]; then
    cat temp_body.txt | sed '$d'
fi
rm temp_body.txt

