#!/bin/sh
DIR="$( cd "$( dirname "$0"  )" && pwd  )"
echo ${DIR}

docker run --name db-urlshorten -e MYSQL_ROOT_PASSWORD=password1 -v ${DIR}/schema.sql:/docker-entrypoint-initdb.d/schema.sql -d mysql
#docker run  --name db-urlshorten -v $pwd/schema.sql:/docker-entrypoint-initdb.d/schema.sql -e MYSQL_ROOT_PASSWORD=password1 -d mysql
