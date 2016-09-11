#!/bin/sh
DIR="$( cd "$( dirname "$0"  )" && pwd  )"
docker run -d -p 9997:8080 --link db-urlshorten --name urlshorten -v ${DIR}:/usr/local/tomcat/webapps tomcat:8-jre8
