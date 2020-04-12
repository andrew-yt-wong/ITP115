# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 11-1

import random


# ---- Die ----------------------------------------------
#
# -------------------------------------------------------
class Die(object):
    # ---- __init__ -----------------------------------------
    #
    # Input: int
    # Output: None
    #
    # Side Effect: None
    # Description: Die class constructor
    # -------------------------------------------------------
    def __init__(self, numSides = 6):
        self.sides = numSides
        self.rollValue = 0

    # ---- roll ---------------------------------------------
    #
    # Input: None
    # Output: None
    #
    # Side Effect: None
    # Description: Simulates rolling a die
    # -------------------------------------------------------
    def roll(self):
        self.rollValue = random.randrange(1, self.sides + 1)

    # ---- __str__ ------------------------------------------
    #
    # Input: None
    # Output: string
    #
    # Side Effect: None
    # Description: Returns a string of sides and rollValue
    # -------------------------------------------------------
    def __str__(self):
        return "Die has " + str(self.sides) + " sides and rolled " + str(self.rollValue)


# ---- calculateSum -----------------------------------------
#
# Input: Die, Die
# Output: int
#
# Side Effect: None
# Description: Roll each die, return the sum
# -------------------------------------------------------
def calculateSum(die1, die2):
    die1.roll()
    die2.roll()
    print(die1)
    print(die2)
    return die1.rollValue + die2.rollValue


# ---- main ---------------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: None
# Description: Main method
# -------------------------------------------------------
def main():
    die1 = Die()
    die2 = Die()
    default1 = input("Use the default number of sides for first die (y/n)? ").lower()
    if default1 == "n":
        numSides1 = int(input("How many sides? "))
        die1 = Die(numSides1)
    default2 = input("Use the default number of sides for second die (y/n)? ").lower()
    if default2 == "n":
        numSides2 = int(input("How many sides? "))
        die2 = Die(numSides2)
    numRolls = int(input("How many times do you want to roll the die? "))
    for i in range(0, numRolls):
        dieSum = calculateSum(die1, die2)
        print("The sum of Dice 1 and Dice 2 is", dieSum)


main()
