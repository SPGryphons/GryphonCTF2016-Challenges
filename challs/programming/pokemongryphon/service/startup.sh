#!/bin/sh

docker build -t pokemon .
docker run -p 8000:8000 --name pokemon pokemon
docker docker start pokemon
