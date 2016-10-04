# 3D Printing
This challenge requires users to use data carving methods to find the solution

## Question Text
My friend went for this "iExperience" field trip and sent me this photo about them 3D printing something. Pretty cool eh?

## Distribution
Distribute all the contents inside `distrib` folder to the users.

## Solution
To get the flag out, all you have to do is to run it through a data carving program like binwalk.

Binwalk command: `binwalk -e <filename>`

To do it manually,
1. Search for the hex `0xFFD8` to find the start of JPEG files.
2. Select the bytes all up until `0xFFD9` as that is the end of file indicator for JPEG.
3. Repeat Step 1 to 2 until end of data is reached.
4. Open all the files found to see the flag.

## Recommended Reads
[File Signatures](http://www.garykessler.net/library/file_sigs.html)
