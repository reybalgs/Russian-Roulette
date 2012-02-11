# Gun.py

# This function contains everything there is to know in order to use and control
# the gun that is supposed to be used in the game.

import random

class Gun():
    """ The gun is actually a list with a size of 6, and within its index are
        randomly placed 1's, a 1 connotates a filled chamber while a 0 is
        otherwise.

    """
    def __init__(self):
        self.cylinder = [] # Initialize the empty cylinder
        
        while len(self.cylinder) < 5: # While we don't have 6 empty chambers yet
            self.cylinder.append(0)

        # Now we will get a random number, and use that as the index number where
        # we will put the 1 value (loaded bullet).

        random.seed()
        bulletIndex = random.randint(0,5)
        
        # Now let's put that bullet in the selected index.
        self.cylinder.insert(bulletIndex, 1)

        # Now let's put the cylinder location into the first cylinder.
        self.currentCylinder = 0

    def shoot(self):
        """ 'Shoots' the gun. While this is in effect, the gun just puts the
            value of the current cylinder into a buffer, moves the location
            of the current cylinder (rotating the cylinder), the returns
            the buffered value.

        """
        print self.cylinder
        print 'Location before shooting: ' + str(self.currentCylinder)

        cylinderValue = self.cylinder[self.currentCylinder] # Put it in the buffer

        if self.cylinder[self.currentCylinder] == 1: # There's a bullet
            # Let's reset it to 0
            print 'There\'s a bullet!'
            self.cylinder[self.currentCylinder] = 0
            self.reload()

        if self.currentCylinder == 5:
            # We're at the last location in the cylinder
            self.currentCylinder = 0
        else:
            self.currentCylinder += 1

        print 'Location after shooting: ' + str(self.currentCylinder)
        return cylinderValue

    def reload(self):
        """ Reloads the gun, or to put it in more general terms, removes all
            the rounds in the gun (if any), then puts a fresh new bullet
            in a random location.

            NOTE: This does not reset the location of the current cylinder,
            unlike the __init__ function.

        """
        
        bulletIndex = 0 # A simple counter variable

        while bulletIndex < 5:
            self.cylinder[bulletIndex] = 0
            bulletIndex += 1

        # Now let's put a random bullet somewhere

        random.seed()
        bulletIndex = random.randint(0,5)

        # Put the bullet in the selected index
        self.cylinder.pop()
        self.cylinder.insert(bulletIndex, 1)

        print self.cylinder

        raw_input()

    def spin(self):
        """ Spins the cylinder of the gun, effectively "shuffling" the
            arrangement and getting a random cylinder ready to be fired.

        """

        random.seed()
        self.currentCylinder = random.randint(1, 6)

        # Announce that the cylinder has been spun
        print 'The gun\'s cylinder has been spun!'
