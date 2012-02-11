# Player.py
#
# This file contains the class for a Player.

class Player():
     """ The player doesn't necessarily have to be human.

         The bots can also use the player class.
     """
     def __init__(self,name):
         """ The init takes the name of the player as an argument.

         """
         self.name = name

         self.alive = 1 # Indicate that the player is still alive
