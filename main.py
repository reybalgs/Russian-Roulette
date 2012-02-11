# Russian rouletteG
#
# A small, no-frills "Russian Roulette" game written in Python.

from player import *
from game import *

print 'Welcome to Russian Roulette.py!'
print 'Please choose a gametype: [a] oneshot [b] lastman'

choice = raw_input()

if choice == 'a':
    # This just puts 1 player into the game.
    # TODO: Add more players into the game, preferably bots

    game = Game("oneshot") # Initialize the game

    name = raw_input("Please enter your name: ")
    newPlayer = Player(name)

    game.playerList.append(newPlayer)
    print name + ' has been added into the game'

    game.start()

else:
    print 'Nothing follows'
    # TODO: Do the lastman gamemode flow
