#iwantix2
This is a challenge that requires the participants to analyse the http header and understand basic ssh tunneling and sql injection knowledge.

```
docker build -t iwantix2 .


docker run --name db-iwantix2 -e MYSQL_ROOT_PASSWORD=wow_w0w -e MYSQL_USER=iwantix2 -e MYSQL_PASSWORD=iwantix22 -e MYSQL_DATABASE=iwantix2 -v pathtosql/sql.sql:/docker-entrypoint-initdb.d/sql.sql -d mysql


docker run --name iwantix2 --link db-iwantix2 -d -p 8002:80 -p 8001:22 iwantix2



docker exec -ti iwantix2 bash



service ssh start
```

##Question Text
Get into the organiser's network and generate tickets so you can sell it at a very low price to our dear admin QR!

##Solution
Tunnel into the port 8001 which is provided in the index.php

Access it at the localhost:Yourport/

Do a SQL Injection 'OR '1'='1 to get the flag,

