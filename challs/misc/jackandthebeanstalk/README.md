# Jack and the Beanstalk
Brief information on how to set up this challenge

## Question Text
Jack is giving away free magical beans!

**Hint**: Jack planted seeds already. Jack also owns 2 pythons.

Play it here: `nc play.spgame.site 9999`

*Creator -  Kelvin Neo (@deathline75)*

## Setup Guide
Serve the program by running 'socketserver.py' using Python 2.7.

## How to Play
Enter a number between 1 to 100. If you guess the next number correctly 10 times, you will win a prize.

## Solution
The first number given by the program is the seed for the whole entire program.
1. Open Python 2.7 Shell
2. Import random library using `import random`
3. Run random.seed(numberGiven) 
4. Run random.randint(1,100) to receive the number to input into the socket.
5. Run random.randint(1,100) again to confirm the next number on screen.
6. Do Step 4-5 9 more times to get the flag
