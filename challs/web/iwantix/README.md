# IWanTix
This chall is basically client side validation. It validates the cookie unix time stamp value. On the next level,it's basically modifying elements in the html

## Question Text
One of our admin really wants to watch Eason Chan's concert, but the organiser will only release their sales after 7th of November 2016. Can you help him to get the concert ticket in advance? Please..? ;_;

Play at http://play.spgame.site:9994

## Setup Guide
apache-php

## Solution
Modify the cookie value of the unix time stamp after 7th of Nov. This is get you half of the flag. Next, delete the element of the button disabled='true' to get the other half!

This tool might help!

http://www.unixtimestamp.com/

