# EzPwn
All server side files are in 'service'.

## Question Text
I just learned C last semester! Better put that to the test!

Play it here: `nc play.spgame.site 9993`

## Setup Guide
TODO

## Solution
This is a integer overflow exploit as well as a format string attack.

1. To find the secret number, type in `%d %d %d %d %d %d %d %d %d %d %d`. The secret number would probably be the 9th number.
2. The first number to input would be 2147483648.
3. Then calculate the positive amount to offset the value by using 2147483648 - secret number.
4. Key that number into the system.
5. Key in the rest of the numbers as 0.

Format string attack works because in the source code, `printf(line)` is used instead of `printf("%s", line)`. This results in being able to read what is in the memory at the time.

Why 2147483647? The number is the maximum integer in a 32-bit set up. This means that if it exceeds by 1 after 2147483647, it will wrap around to -2147483648. I recommend reading up on 2's compliment to see how this works.

