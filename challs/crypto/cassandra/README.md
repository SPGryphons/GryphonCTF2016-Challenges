Cassandra
---------

Predictable IVs and chosen plaintext prepended to secret data allow an attacker
to abuse the Oracle to decrypt the flag one bit at a time.

# Question Text

He gave to her, yet tenfold claim'd in return -
She hath no life but the one he for her wrought;
Proffer'd to her his wauking heart - she turn'd it down,
Riposted with a tell-tale lore of lies and scorn.

(https://youtu.be/\_J4Onll7VNs)

*Creator -  amon (@nn_amon)*

# Setup Guide

0. Install docker on the hosting system
2. Build the docker image with: `sh dockerbuild.sh`
3. Replace the port 1344 with your desired port in dockerrun.sh
4. Start the docker image: `sh dockerrun.sh`
5. Test the connectivity with netcat.

# Exploit Details

Since we can control what is prepended to the secret data on the bit level, we
can manipulate the number of bits from the flag that are included in the first
block of the ciphertext.

Also, since the IVs are predictable using a non-secure permutation routine, we
can manipulate the first plaintext block reliably.

Let flag = b1b2b3b4 ... b128.

To obtain b1, we can do the following:

Let IV1 = seed
Let IV2 = permute(IV2)
Let m1 = 000...0 where len(m1) = 127

Submit m1 to the oracle to encrypt m1 || flag which means the first block will
be:

p1 = 000...0b1
c1 = encrypt(IV1 ^ p1)

Now, create a comparison submission to check if b1 is 0.

m2 = IV1 ^ IV2
p2 = IV1 ^ IV2
c2 = encrypt(IV2 ^ IV1 ^ IV2)
c2 = encrypt(IV1)

If b1 = 0,

c1 = encrypt(IV1) since x ^ 0 = x

Thus, if c1 = c2, then b1 = 0 else b1 = 1.

To obtain the rest of the bits, repeat this process with

m1 = 000...0 where len(m1) = 128 - bit position
m2 = IV1 ^ IV2 ^ (m1 || known bits || 0)
