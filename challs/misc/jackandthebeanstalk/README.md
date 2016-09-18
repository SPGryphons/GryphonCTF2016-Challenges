# Jack and the Beanstalk
Brief information on how to set up this challenge

## Question Text
Jack is giving away free magical beans!

**Hint**: Jack planted seeds already.

Play it here: `nc play.spgame.site 9999`

## Setup Guide
Serve the program by running 'socketserver.py' using Python 2.7.

## How to Play
Enter a number between 1 to 100. If you guess the next number correctly 10 times, you will win a prize.

## Solution
The first number given by the program is the seed for the whole entire program.
Run random.seed(numberGiven) then keep running random.randint(1,100) to get the next number.
