#!/bin/bash


# As usual, CCC doesn't work at the beginning. Made this script to test the website lol

url="https://register.codingcontest.org/"

while true; do
    response_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    if [ "$response_code" -ne 500 ]; then
        echo "Website is no longer returning HTTP 500 (Status Code: $response_code)"
        break
    fi

    echo "HTTP 500 detected. Retrying in 1 second..."
    sleep 1
done
