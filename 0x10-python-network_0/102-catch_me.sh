#!/bin/bash
# A bash script that makes a request to a server that causes the server to respond with a message.
curl -sX PUT -L -d "user_id=98" --header "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
