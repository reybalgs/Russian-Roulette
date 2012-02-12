# Russian roulette
#
# A small, no-frills "Russian Roulette" game written in Python.

from player import *
from game import *

print 'Welcome to Russian Roulette.py!'
print 'Please choose a gametype: [a] oneshot [b] lastman [c]'
print '                          [c] turbo lastman'
print '                          [d] quit'

choice = raw_input("Your gametype: ")

if choice == 'a':
    game = Game("oneshot")
elif choice == 'b':
    game = Game("lastman")
elif choice == 'c':
    game = Game("turbolastman")
elif choice == 'd':
    print 'Bye!'
    # Once the choice is exit the script will ignore the if below and
    # close itself.

if choice != 'd':
    while (choice != 'a' and choice != 'b' and choice != 'c'): # Invalid inputs
        print 'Invalid input, please try again.'
        choice = raw_input("Gametype: ")

        # Initialize the games again in case of a proper input
        if choice == 'a':
            game = Game("oneshot")
        elif choice == 'b':
            game = Game("lastman")
        elif choice == 'c':
            game = Game("turbolastman")

    numPlayers = 0 # Initialize the number of players

    while numPlayers <= 0: # Loop while the user isn't inputting a useful value
        numPlayers = input("How many players are playing? ")
        while choice == 'b' and numPlayers <= 1:
            print 'You can\'t play alone in a last man standing game!'
            numPlayers = input("Please input again: ")

    # Now let's ask for the player's names one by one
    playerCounter = 1 # A counter variable

    while playerCounter <= numPlayers:
        ask_string = 'Enter the name of Player #' + str(playerCounter) + ': '
        newPlayer = Player(raw_input(ask_string))
        game.addPlayerToGame(newPlayer)
        playerCounter += 1

    game.start()
