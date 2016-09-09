#!/bin/sh
docker build -t harambe .
docker run -d -p 9998:80 --name harambe harambe
docker start harambe
