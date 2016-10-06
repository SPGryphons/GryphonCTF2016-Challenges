# URL Shorten
Source code is in the 'generate' folder.

## Question Text
My friend hates using external web services to do his work, especially URL shorteners. So he made his own!

http://play.spgame.site:9997/

*Creator - Kelvin Neo (@deathline75)*

## Setup Guide
MySQL and Tomcat (or any webapp that runs J2EE) is needed to run this.
Be sure to run the SQL file first inside the 'service' folder.
Deploy the war file inside the 'service' folder.

## Solution
This is a forceful browsing challenge, along with execution after redirect exploit.

To get the flag, type in terminal
```
curl http://play.spgame.site:9997/l/8
```
