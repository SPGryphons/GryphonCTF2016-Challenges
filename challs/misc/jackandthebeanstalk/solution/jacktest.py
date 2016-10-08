#!/usr/bin/python
import random
import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('play.spgame.site', 9999))
print s.recv(4096)
data = s.recv(4096)

if "Guess" in data:
    seed = 0
    try:
        seed = re.findall('[0-9]+', data)[1]
    except:
        print "ERROR: ", data
        
    random.seed(int(seed))
    print "Seed is:", seed
    
    nextnum = str(random.randint(1,100))
    print data, nextnum
    s.sendall(nextnum)
    
    print s.recv(4096)
    
    for i in range(9):
        random.randint(1,100)
        print s.recv(4096),
        nextnum = str(random.randint(1,100))
        print nextnum
        s.sendall(nextnum)
        print s.recv(4096)
    
    print s.recv(4096)
        
s.close()