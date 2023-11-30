#!/bin/bash
# A bash script that takes in a URL as an argument, sends a GET response to the URL and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
