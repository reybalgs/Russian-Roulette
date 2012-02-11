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
    game = Game("oneshot") # Initialize the game

    numPlayers = 0 # Initialize the number of players

    while numPlayers <= 0: # Loop while the user isn't inputting a useful value
        numPlayers = input("How many players are playing? ")
        if numPlayers <= 0:
            print 'Try again, stupid!'

    # Now let's ask for the player's names one by one
    playerCounter = 1 # A counter variable

    while playerCounter <= numPlayers:
        ask_string = 'Enter the name of Player #' + str(playerCounter) + ': '
        newPlayer = Player(raw_input(ask_string))
        game.addPlayerToGame(newPlayer)
        playerCounter += 1

    game.start()

else:
    print 'Nothing follows'
    # TODO: Do the lastman gamemode flow
