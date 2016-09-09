#!/bin/sh

docker build -t pokemon .
docker run -p -d 8000:8000 --name pokemon pokemon
docker docker start pokemon
