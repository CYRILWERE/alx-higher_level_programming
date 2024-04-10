#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X GET "$1" -D - | awk '/HTTP\/1.1 200 OK/ {flag=1; next} flag {print}'

