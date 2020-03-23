# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 9-1

import random


# coin flips a coin whether it is head or tails and returns it
def coin():
    choice = random.randrange(2)
    if choice == 0:
        return "heads"
    else:
        return "tails"


# experiment that calls coin until 3 heads in a row
def experiment():
    headCountInARow = 0
    totalFlips = 0
    while headCountInARow < 3:
        totalFlips += 1
        flip = coin()
        if flip == "heads":
            headCountInARow += 1
        else:
            headCountInARow = 0
    return totalFlips


# main that calls experiment 10 times and returns the average
def main():
    totalFlips = 0
    for i in range(10):
        totalFlips += experiment()
    print("The average for 3 heads in a row is:", (totalFlips / 10))


main()
