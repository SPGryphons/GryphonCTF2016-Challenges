#!/bin/sh
docker build -t sharkweb .
docker run -d -p 9995:80 --name sharkweb sharkweb
docker start sharkweb
