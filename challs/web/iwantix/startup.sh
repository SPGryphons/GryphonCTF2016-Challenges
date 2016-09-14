#!/bin/sh
docker build -t iwantix .
docker run -d -p 9994:80 --name iwantix iwantix
docker start iwantix
