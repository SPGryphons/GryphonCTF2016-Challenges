# Pokemon Gryphon
All server side files are in service. Server and solution both requires Python 3+. `pokeserver.py` is the main server, and requires `coloredstatus.py` and `pokemons.txt`. `solution.py` is the solution for the challenge.

## Question Text
Our brand new take on Pokemon Go!
Can you catch them all? Don't get caught spoofing though!
`nc play.spgame.site 8000` to start playing!

**Commands:**
`catch`: when a Pokemon appears near you
`spoof x,y`: e.g. "spoof 56,-35" to spoof GPS co-ords to x=56, y=-35 (integers only)

## Setup Guide
```sh
$ cd service
$ ./pokeserver.py [port]
```

## How to Play
There are a total of 151 pokemons available, and the player has to catch all of them to get the flag.

The server hosts a virtual 200m x 200m map (x=100 to x=-100, y=100 to y=-100), requiring the player to navigate around it with `spoof x,y`, where x and y are the coordinates they wish to move to. The server will inform the player of the location of the first pokemon and their current location, with this information, the player has to continuously spoof their location towards the pokemon, and use `catch` once the pokemon appears. The server will then spawn the next pokemon for the player to catch in a random spot, the player will have to move towards it using `spoof`, and `catch` once it appears, and so on until all 152 pokemons are caught.

The server will detect the distance between each spoof, and will kick the player if that distance is more than 5m.

## Solution
The player will have to incorporate the use of programming (loops, network sockets, regex) and basic mathematical concepts to solve this challenge. To avoid alerting the server that they are spoofing, the player cannot simply "teleport" to the pokemon and catch it. One solution is to use pythagoras theorem to calculate the distance between their current location and the nearest pokemon, and from there, formulate the points to spoof (which is around 5m apart from each other) to form a spoofing route.

The solution program, `solution.py`, can be found in the service folder. Run the solution client with `./solution.py [port]`.


