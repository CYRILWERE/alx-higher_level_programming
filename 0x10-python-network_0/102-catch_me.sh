#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me causing the server to respond with a message containing "You got me!" in the body of the response
<<<<<<< HEAD
curl -sLX PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin:HolbertonSchool"
=======
curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -L -H "Origin: HolbertonSchool"
>>>>>>> c3099ea39b023c39207629c04da03c62b072ed42

