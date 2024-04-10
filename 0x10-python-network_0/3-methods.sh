#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
<<<<<<< HEAD
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print substr($0, index($0, $2))}'
=======
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-
>>>>>>> c3099ea39b023c39207629c04da03c62b072ed42

