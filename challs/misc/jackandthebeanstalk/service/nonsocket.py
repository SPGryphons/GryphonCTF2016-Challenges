#!/usr/bin/python
import random
import sys
from select import select

def console_out(data, sep="\n"):
    sys.stdout.write(data + sep)
    sys.stdout.flush()
    
def console_in(prompt):
    timeout = 10
    console_out(prompt, sep="")
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        s = sys.stdin.readline()
        return s
    else:
        console_out("Too slow...")
        exit()

num = random.randint(1,100)
random.seed(num)
console_out("My numbers are always between 1 (inclusive) to 100 (inclusive)!")
console_out("Guess my number 10 times and you get a prize!\n")

for i in range(10):
    console_out("My number is: " + str(num))
    data = console_in("Guess my next number: ").strip()
    if data.isdigit():
        guess_num = int(data.strip())
        num = random.randint(1,100)
        if num != guess_num:
            console_out("Oh no! That's not my number!")
            quit()
        else:
            console_out("Well done!\n")
            num = random.randint(1,100)
    else:
        console_out("That's not a valid number!")
        quit()

console_out("This is my prize to you: GCTF{RNG_g@m3_700_str0nk}")
