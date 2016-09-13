#!/bin/sh

docker build -t pokemon .
docker run -d -p 8000:8000 --name pokemon pokemon
docker start pokemon
