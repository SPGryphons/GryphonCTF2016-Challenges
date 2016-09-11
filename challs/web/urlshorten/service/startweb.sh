#!/bin/sh
DIR="$( cd "$( dirname "$0"  )" && pwd  )"
docker run -d --link db-urlshorten --name urlshorten -v ${DIR}:/usr/local/tomcat/webapps tomcat:8-jre8
