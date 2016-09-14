#!/bin/sh
docker build -t iwantix .
docker run -d -p --rm 9994:80 --name iwantix iwantix
docker start iwantix
