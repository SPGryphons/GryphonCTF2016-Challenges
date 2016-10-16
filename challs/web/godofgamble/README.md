# God Of Gamble
This challenge is a no brainer. --> God Of Gamble

## Description
This challenge objective is for the participants to learn how to script with forms


## Setup Guide
1. Set up a php-apache server

## Distribution
Distribute all the contents inside `distrib` folder to the users.

## Solution
```bash
while [ 1 ]; do curl -s 'http://172.17.0.4/flag.php' --data 'bet=1' | grep -v Sorry; done
```


