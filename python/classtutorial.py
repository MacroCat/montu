# No need to worry about this stuff up imported up here,
# this is just used as an example to demostrate how to
# use classes, but are not required to use classes.
# (I'll briefly explain what this does at the end.)
from msvcrt import getch

class Enemy:
    # Variables declared in the class can be accessed
    # from any function within the class without converting
    # it into a global variable, however, they must have self
    # in front of it when it is used.
    life = 3

    # Class functions ALWAYS require the argument
    # 'self' inside the parenthesis.
    def attack(self):
        print("ouch!")
        self.life -= 1

    # Essentially, functions work and are structured the
    # exact same way as they are outside of functions, the
    # only exception being that they require the (self)
    # argument, and that variables need to have "self." before
    # them. (e.g self.life).
    def checkLife(self):
        if self.life <= 0:
            print("I am dead, you win!")
        else:
            print(str(self.life), "life left")

# What this does is converts the class "Enemy" into
# an object "action".
action = Enemy()

print("Press spacebar to hit!")

# This loop runs until the enemy's health reaches zero,
# which will then stop the program.
# To access variables from classes, you need to use the object.
while action.life != 0:

    # This assigns the integer belonging to whatever key is
    # presssed to the variable 'key', and in this case,
    # the spacebar holds the number '32'.
    # (This only works on Windows)
    key = ord(getch())

    # If the spacebar is pressed, this will invoke this statement.
    if key == 32:

        # To access fucntions, similar to variables, you must use
        # the created object.
        action.attack()
        action.checkLife()
