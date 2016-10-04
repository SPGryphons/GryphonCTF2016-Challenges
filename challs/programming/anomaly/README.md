# Anomaly
This challenge requires players to use SHA-512 way too many times.

## Question Text
I have made this file by using SHA-512 512 times on every number in string format from 1 to 1000000. However there are some anomalies in the file when I re-ran the same program. Can you find out the anomaly for me?

**WARNING**: 123MB file

## Setup Guide
Go to `generate\setup.py` to generate the file. It will not be the same file as the one given in the actual competition due to RNG.

## Solution
The solution is in `solution\solution.py`

This challenge is pretty evil, as it requires the user to SHA-512 the ASCII version of numbers from 1 to 1 million 512 times to generate a hash that is to be compared with the hashes given in the file.

If the hashes are different, the difference in integer is the ASCII code for the flag character. This script should take less than 10 minutes to finish comparing and reading the file.
