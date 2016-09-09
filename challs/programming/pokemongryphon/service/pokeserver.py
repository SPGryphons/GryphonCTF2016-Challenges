#!/usr/bin/python3

# Pokemon Gryphon Server
# Optixal

import socket, sys, time, datetime, random, math
import coloredstatus as cs
from time import sleep
from _thread import *

if len(sys.argv) != 2:
    print(cs.status, "Usage:", sys.argv[0], "[port]")
    sys.exit(1)

host = '0.0.0.0'
port = int(sys.argv[1])

timeout = 5
locationmax = 100
locationmin = -100
min_catch_proximity = 5
max_spoof_distance = 5

flag = "GCTF{y0u_c4u6h7_7h3m_4ll_!}"

pokemons = list(config.split("#")[0].strip() for config in open("pokemons.txt", "r") if config.strip() and config.split("#")[0].strip())
pokemons.reverse()

pikachu = """\x1b[1m\x1b[93m\
░░░░░░░░█░▀▄░░░░░░░░░░▄▄███▀ 
░░░░░░░░█░░░▀▄░▄▄▄▄▄░▄▀░░░█▀ 
░░░░░░░░░▀▄░░░▀░░░░░▀░░░▄▀ 
░░░░░░░░░░░▌░▄▄░░░▄▄░▐▀▀
░░░░░░░░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█ 
░░░░░░░░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█ 
░░░░░░░▄▀▀▐▀▀░░░░░░░▀▀▌▄▄▄░░░█ 
░░░░░░░█░░░▀▄░░░░░░░▄▀░░░░█▀▀▀ 
░░░░░░░░▀▄░░▀░░▀▀▀░░▀░░░▄█▀\x1b[0m
"""

# Custom Exception
class PokemonError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Get Current Time
def gettime():
    return '{0:%d/%m/%y %H:%M:%S}'.format(datetime.datetime.now()) + " -"

# Check Whether In Proximity With Pokemon
def isnearpokemon(a, b):
    if len(a) != 2 or len(b) != 2:
        return False
    return True if math.hypot(a[0] - b[0], a[1] - b[1]) < min_catch_proximity else False

# Check For Teleport
def isteleporting(a, b):
    if len(a) != 2 or len(b) != 2:
        return True
    return True if math.hypot(a[0] - b[0], a[1] - b[1]) > max_spoof_distance else False

# Log Captured Flags
def logflag(host, port, timetaken):
    with open("flag_log.txt", "a") as f:
        f.write(gettime() + " Flag captured by " + host + ':' + str(port) + " after " + timetaken + "\n")

# Client Thread
def client(conn, addr):
    print(cs.openlabel, gettime(), "New connection from", addr[0] + ':' + str(addr[1])) 
    conn.send(str.encode("\n" + pikachu + "\n"))
    conn.send(str.encode(cs.good + " Welcome to Pokemon Gryphon!\n"))
    conn.send(str.encode(cs.good + " By Optixal\n\n"))
    conn.send(str.encode(cs.status + " Use 'spoof x,y' to move around (don't get caught teleporting)!\n"))
    conn.send(str.encode(cs.status + " Hint: Be sure not to spoof more than 5m from your current location!!\n\n"))
    conn.send(str.encode(cs.status + " Use 'catch' to catch a Pokemon only when they appear near you!\n"))
    conn.send(str.encode(cs.status + " Hint: Your pokeradar will tell you where is the nearest pokemon,\n"))
    conn.send(str.encode(cs.status + " Hint: but, they will only appear once you are within 5m of it!!\n\n"))
    sleep(0.2)
    
    conn.settimeout(timeout)
    client_start_time = time.time()
    
    client_end_time = time.time() - client_start_time

    try:
        currentx = random.randint(locationmin, locationmax)
        currenty = random.randint(locationmin, locationmax)
        current_coord = (currentx, currenty)

        for pokemon in pokemons:
            xlocation = random.randint(locationmin, locationmax)
            ylocation = random.randint(locationmin, locationmax)
            pokemon_coord = (xlocation, ylocation)
            
            # Receive
            while True:
                if isnearpokemon(current_coord, pokemon_coord):
                    conn.sendall(str.encode(cs.good + " A wild " + pokemon + " appears!\n" + cs.status + " What do you do?: "))
                else:
                    conn.sendall(str.encode(cs.status + " Nearest pokemon is at (X=" + str(xlocation) + ",Y=" + str(ylocation) + ")\n" + cs.status + " Your current location is (X=" + str(currentx) + ",Y=" + str(currenty) + ")\n" + cs.status + " What do you do?: "))
                
                data = conn.recv(2048).decode("UTF-8")
                
                if not data:
                    raise PokemonError("null data")

                data = list(data.strip().split(" "))
                if data[0] == "spoof" and len(data) == 2:
                    spoofed_coord = tuple(data[1].split(","))
                    spoofed_coord = tuple(int(x) for x in spoofed_coord)

                    if len(spoofed_coord) != 2:
                        raise PokemonError("invalid spoofing")

                    if isteleporting(current_coord, spoofed_coord):
                        raise PokemonError("teleporting")
                
                    currentx = spoofed_coord[0]
                    currenty = spoofed_coord[1]
                    current_coord = spoofed_coord

                elif data[0] == "catch" and len(data) == 1:
                    if not isnearpokemon(current_coord, pokemon_coord):
                        raise PokemonError("trying to catch nothing")
                    conn.send(str.encode(cs.good + " You caught " + pokemon + "!\n\n"))
                    break
                else:
                    raise PokemonError("bad input")
             
        client_end_time = int(time.time() - client_start_time)
        timetaken = str(client_end_time % 3600 // 60) + "min " + str(client_end_time % 60) + "sec"
        conn.send(str.encode(cs.good + " Congratulations, you caught them all! " + flag + "\n"))
        print(cs.flaglabel, gettime(), "Flag captured by", str(addr[0]) + ':' + str(addr[1]) + " after " + timetaken)
        #logflag(addr[0], addr[1], timetaken) 
    
    except socket.timeout:
        conn.send(str.encode("\n" + cs.error + " You were kicked from Pokemon Gryphon for not having a continuous connection!\n"))
        print(cs.kicklabel, gettime(), "Kicked", addr[0] + ':' + str(addr[1]), "for being too slow")
    except PokemonError as pe:
        try:
            conn.send(str.encode("\n" + cs.error + " You were kicked from Pokemon Gryphon for " + pe.value + "!\n"))
            print(cs.kicklabel, gettime(), "Kicked", addr[0] + ':' + str(addr[1]), "for", pe.value)
        except BrokenPipeError:
            print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]), "due to broken pipe") 
    except (BrokenPipeError, ConnectionResetError):
        print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]), "due to broken pipe") 
    except:
        conn.send(str.encode("\n" + cs.error + " You were kicked for bad input!\n"))
        print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]), "due to an error")
    finally:
        conn.close()
        # print(cs.closelabel, gettime(), "Connection closed from", addr[0] + ':' + str(addr[1]))

# Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_start_time = time.time()

try:
    s.bind((host, port))
    print(cs.good, gettime(), "Server started on", host + ':' + str(port) + '!')
except socket.error as e:
    print(str(e))

s.listen(128)
print(cs.status, gettime(), "Waiting for connections...")

try:
    while True:
        conn, addr = s.accept()
        start_new_thread(client, (conn, addr))
except KeyboardInterrupt:
    print("\n" + cs.status, gettime(), "Stopping server...")
finally:
    s.close()
    server_end_time = int(time.time() - server_start_time)
    print(cs.good, gettime(), "Server stopped!")
    print(cs.status, gettime(), "Ran for", str(server_end_time // 86400) + "days", str(server_end_time % 86400 // 3600) + "hrs", str(server_end_time % 3600 // 60) + "min", str(server_end_time % 60) + "sec")

