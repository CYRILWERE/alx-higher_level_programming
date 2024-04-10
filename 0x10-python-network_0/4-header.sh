#!/bin/bash
<<<<<<< HEAD
# This script takes in a URL as an argument, sends a GET request to the URL with a header variable X-School-User-Id, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
=======
# This script takes in a URL as an argument, sends a GET request to the URL with a specific header, and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
>>>>>>> c3099ea39b023c39207629c04da03c62b072ed42

