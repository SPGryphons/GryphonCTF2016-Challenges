# Zizi
Your ex-coworker, **Zizi**, discreetly changed your wallpaper on your desktop before leaving the company.

## Question Text
Your ex-coworker, **Zizi**, discreetly changed your wallpaper on your desktop before leaving the company...

## Distribution
Image found in distrib folder.

## Solution
The user will need to know about basic hex dumping and file signatures.

Hex dump the JPEG image, find the JPEG trailer "FF D9". Right after it, there is a "50 4B 03 04" signature, a ZIP signature, and also some plaintext showing that there is a "pass.txt" file in the archive. The user can copy the appended ZIP archive to a new file by copying the hex data starting with "50 4B 03 04" (all the way to the end) to a new file, and by naming it "test.zip". Extract it, and open the "pass.txt". The text file gives a password to the user, "l0v3z1z1".

The password is not the flag, the user will then have to extract the actual JPEG image out of the original JPEG + ZIP image, and use JPHS (a stego tool for hiding files within JPEG images, introduced in Poly Year 1) to extract the file within the original JPEG image using the password. The extracted file will be another ZIP archive, once extracted, produces a love note containing the flag within it.

Two different techniques to get the flag, two different ZIP archive files present, hence the name, Zizi.
