#!/bin/sh
docker build -t godofgamble .
docker run -d -p 9996:80 --name godofgamble godofgamble
docker start godofgamble
