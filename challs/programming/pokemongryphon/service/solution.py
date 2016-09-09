#!/usr/bin/python3

import socket, sys, re, math

if len(sys.argv) != 3:
    print("[*] Usage:", sys.argv[0], "[server]", "[port]")
    sys.exit(1)

server = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to", server + ':' + str(port) + "...")

s.connect((server, port))
result = s.recv(4096).decode("UTF-8")

current_coord = (0, 0)
current_coord_extracted = False

# Buffer
while (len(result) > 0):
    print(result, end='')

    # Catch Pokemon If Pokemon Appears
    if "appears" in result:
        s.send(str("catch").encode())

    # Move to Pokemon
    elif "Nearest" in result:
        result = list(result.split("\n"))
        
        # Initial Extraction of Current Coordinates
        if not current_coord_extracted:
            try:
                m = re.match(r"^.*\(X=(?P<X>\-?\d+),Y=(?P<Y>\-?\d+)\)", result[1])
                current_coord = (int(m.group('X')), int(m.group('Y')))
                current_coord_extracted = True
            except AttributeError:
                sys.exit("Pattern not found when extracting current location!")
        
        # Extract Pokemon's Location
        try:
            m = re.match(r"^.*\(X=(?P<X>\-?\d+),Y=(?P<Y>\-?\d+)\)", result[0])
            pokemon_coord = (int(m.group('X')), int(m.group('Y')))
        except AttributeError:
            sys.exit("Pattern not found when extracting Pokemon's location!")

        # Total Distance Between Current Location and Pokemon
        d = math.sqrt(((current_coord[0] - pokemon_coord[0]) ** 2) + ((current_coord[1] - pokemon_coord[1]) ** 2))

        # Ratio of (Max Spoof Distance)/(Total Distance)
        r = 4 / d

        # New Coords to Spoof
        newx = round(current_coord[0] + (pokemon_coord[0] - current_coord[0]) * r)
        newy = round(current_coord[1] + (pokemon_coord[1] - current_coord[1]) * r)
        print("BOT: Spoofing x=" + str(newx) + ", y=" + str(newy))

        # Replace Old Coord with New Coord
        current_coord = (newx, newy)

        # Spoof Location
        s.send(str("spoof " + str(newx) + "," + str(newy)).encode())

    elif "Use" in result or "Hint" in result or "Welcome" in result:
        pass
    else:
        pass

    result = s.recv(1024).decode("UTF-8")

