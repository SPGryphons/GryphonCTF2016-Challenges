#!/bin/sh

docker build -t jackandthebeanstalk .
docker run -dt -p 9999:9999 --name jackandthebeanstalk jackandthebeanstalk
