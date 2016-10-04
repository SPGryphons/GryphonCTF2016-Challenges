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

Why 2147483647? The number is the maximum integer in a 32-bit set up. This means that if it exceeds by 1 after 2147483647, it will wrap around to -2147483648. I recommend reading up on 2's compliment to see how this works.

