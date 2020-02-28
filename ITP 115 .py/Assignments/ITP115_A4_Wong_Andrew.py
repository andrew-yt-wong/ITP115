# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 4
# Description:
# Character Counter & D20 Dice Game (in one file)

import random


def main():
    # Part 1 - Character Counter
    print("PART 1 - Character Counter")

    # Prompt the user for a sentence
    sentence = input("Please Enter a sentence: ").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    specialCounter = 0

    # Loop and calculate the numbers
    for letter in sentence:
        if letter not in alphabet and letter != ' ':
            specialCounter += 1

    # Print the message and special characters
    print("\nHere is the character distribution:\n")
    print("special characters: ", end="")
    for num in range(specialCounter):
        print("*", end="")
    print()

    # Loop through the string for each alphabetical character
    for alpha in alphabet:
        alphaCount = 0
        for letter in sentence:
            if letter == alpha:
                alphaCount += 1
        print(alpha, end="")
        print(": ", end="")
        if alphaCount == 0:
            print("NONE")
        else:
            for num in range(alphaCount):
                print("*", end="")
            print()

    # Part 2 - D20 Dice Game
    print("\nPART 2 - D20 Dice Game")

    # Start a total score variable
    total = 0

    # Loop over the game 10 times
    for num in range(10):

        # Choose a random case for this roll
        case = random.randrange(1, 5)
        print("\nYou are playing for CASE", case)
        print("You will win for the following numbers:")
        if case == 1:
            for roll in range(1, 21):
                if roll % 2 == 0:
                    print(roll, end=" ")
        elif case == 2:
            for roll in range(1, 21):
                if roll % 2 != 0:
                    print(roll, end=" ")
        elif case == 3:
            for roll in range(5, 11):
                print(roll, end=" ")
        elif case == 4:
            for roll in range(10, 21):
                if roll % 2 == 0:
                    print(roll, end=" ")
        else: # case == 5
            for roll in range(1, 21):
                if roll % 3 == 0:
                    print(roll, end=" ")

        # Roll and get the value
        print("\n\nNow rolling ...")
        roll = random.randrange(1, 20)
        print("You rolled a", roll, end="")
        print("!")

        # Check whether we won this round or not
        if case == 1:
            if roll % 2 == 0:
                print("You won 50 points! :)")
                total += 50
            else:
                print("You didn't win :(")
        elif case == 2:
            if roll % 2 != 0:
                print("You won 50 points! :)")
                total += 50
            else:
                print("You didn't win :(")
        elif case == 3:
            if 4 < roll < 11:
                print("You won 50 points! :)")
                total += 50
            else:
                print("You didn't win :(")
        elif case == 4:
            if roll % 2 == 0 and roll > 9:
                print("You won 50 points! :)")
                total += 50
            else:
                print("You didn't win :(")
        else: # case == 5:
            if roll % 3 == 0:
                print("You won 50 points! :)")
                total += 50
            else:
                print("You didn't win :(")

    # Print out the total score
    print("\nYour total score is:", total)
    print("Thanks for playing!")


main()
