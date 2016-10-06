California Dreaming
-------------------

Reversing python extensions written in C.

# Question Text

```
I want to go to California but I've forgotten the PIN and pass phrase to my bank
account. Now I can't buy my plane ticket! Please help me out.

(https://youtu.be/xrfVaPNMCM8)
```

*Creator -  amon (@nn_amon)*

# Setup Guide

0. Provide the participants with the tar.gz file in distrib.

# Exploit Details

Reverse the python extension california.so to find that it exports three
methods: 'dreams', 'mama', 'papa'.

'dreams' sets a global variable pin to the provided PIN and checks it against
the correct value (73313). If returns if the value is correct.

'mama' checks the passphrase. It should be 'Be Sure To Wear Flowers In Your
Hair'.

'papa' takes a 16 byte MD5 digest. The method xors the packed value of the pin
with the digest. This is the transform string. Now, the encrypted flag string is
xored against the transform string and returned.

Working solution is in service/solution.py
