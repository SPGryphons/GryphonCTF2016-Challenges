# EzPwn
All server side files are in 'service'.

## Question Text
I just learned C last semester! Better put that to the test!

Play it here: `nc play.spgame.site 9993`

## Setup Guide
TODO

## Solution
This is the simplest integer overflow exploit.
Take 2147483647 * 2 - (CurrentNumber - 1000) + 2 and put it into the input.

