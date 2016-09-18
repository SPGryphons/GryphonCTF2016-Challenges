# Hide and Seek
Distribution file located in distrib folder, solution script located in solution folder, script to recreate the challenge located in generate folder. The script to recreate the challenge requires the files in the lib folder.

## Question Text
Welcome to Hide and Seek.
Hiders code to hide, seekers seek to capture the flag.
Are you a hider or a seeker?

## Solution
The challenge requires the user to have knowledge on basic QR code formats and moderate-level programming (loops, IO programming, image processing, QR code parsing, string formatting).

The rough steps to solve this challenge:

1. Load challenge image
2. Split challenge image into 33x33 blocks
3. Parse each block as a QR code
4. Filter out the single QR code that contains the flag "GCTF{...}"

The full solution `solution.py` is located in the solution folder.
