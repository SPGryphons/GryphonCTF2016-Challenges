A Forest
--------

An assembly based puzzle where a listing of x86 instructions are given and a
register to provide the value of after the evaluation of the instructions.

# Question Text

```
It is time to test your 1337 skills of doing assembly in your head. You get ten
seconds to evaluate the given x86-64 code listing and give us the value of the
register that has been randomly chosen from those modified. Assembly! Again, and
again, and again, and again, and again...

(https://youtu.be/xik-y0xlpZ0)

nc play.spgame.site 1351
```

*Creator -  amon (@nn_amon)*

# Setup Guide

0. Install docker on the hosting system
2. Build the docker image with: `sh dockerbuild.sh`
3. Replace the port 1351 with your desired port in dockerrun.sh
4. Start the docker image: `sh dockerrun.sh`
5. Test the connectivity with netcat.

# Exploit Details

Use keystone to assemble the x86-64 listing and unicorn to emulate the
instructions and get the values after they have run.

Working solution is in service/exploit.py.
