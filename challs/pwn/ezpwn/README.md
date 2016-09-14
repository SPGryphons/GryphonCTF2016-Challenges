# EzPwn

All server side files are in 'service'.

## Solution

This is the simplest integer overflow exploit.
Take 2147483647 * 2 - (CurrentNumber - 1000) + 2 and put it into the input.

