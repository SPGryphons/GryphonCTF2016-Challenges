#!/usr/bin/env python
# source file: ThreadServerWithTmout.py
# This version using threading module, timeout exception and message Queue to solve the blocking issues.
# Using standard Thread class to invoke multi-thread execution of a function.
# Easier to use, but missing some inter-thread synchronization feature.
import socket
import threading
import Queue
import random

def handler(con,q):
    # con is the TCP socket connected to the client
    con.settimeout(3.0)
    try:
        num = random.randint(1,100)
        random.seed(num)
        con.sendall("My numbers are always between 1 (inclusive) to 100 (exclusive)!\n");
        con.sendall("Guess my number 10 times and you get a prize!\n\n");
        for i in range(10):
            con.sendall("My number is: " + str(num) + "\n")
            con.sendall("Guess my next number: ")
            data = con.recv(1024).strip()
            if data.isdigit():
                guess_num = int(data)
                num = random.randint(1,100)
                if num != guess_num:
                    con.sendall("Oh no! That's not my number!\n")
                    con.close()
                    return
                else:
                    con.sendall("Well done!\n")
                    num = random.randint(1,100)
            else:
                    con.sendall("That's not a valid number!\n")
                    con.close()
                    return
        con.sendall("This is my prize to you: GCTF{RNG_g@m3_700_str0nk}\n")
        print "client connection is closed"    
    except Exception, e:
        print "client connection is closed"    
    con.close()
    return

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 9999))
serversocket.listen(5) # become a server socket, maximum 5 connections
print "Server starts listening ..."
stopFlag=False
serversocket.settimeout(3.0) # setup a 3 seconds timeout to exit the blocking state
while True:
    if not stopFlag:
        try:
            connection, address = serversocket.accept() 
            print "start a new connection"
             # setup and start a new thread to run an instance of handler() 
            t = threading.Thread(target=handler, args=(connection,10))
            t.start()
        except KeyboardInterrupt:
            stopFlag = True
            break
        except Exception as inst:
            print inst
            if str(inst) != "timed out": # timed out exception is okay, else must quit.
                break

serversocket.close()        
print "Server stops"
