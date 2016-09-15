#!/bin/sh

docker build -t ezpwn .
docker run --name ezpwn -dt -p 9993:9993 ezpwn
