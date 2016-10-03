Drag Race
---------

Simple buffer overflow with conveniently placed printfs to print important
pointers and the value of the return address to help noobs to pwn.

# Question Text

```
Do Aleph One proud.

nc xxx.xxx.xxx.xxx 1346
```

*Creator -  amon (@nn_amon)*

# Setup Guide

0. Install docker on the hosting system
1. Replace the flag in distribute/flag
2. Build the docker image with: `sh dockerbuild.sh`
3. Replace the port 1346 with your desired port in dockerrun.sh
4. Start the docker image: `sh dockerrun.sh`
5. Test the connectivity with netcat.

# Exploit Details

Just overwrite the eip with the address of give\_shell().

Working exploit is in service/exploit.sh
