# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 4-1

import random


def main():
    # Print the welcome message
    print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!\n(Welcome to the Pig Elvish translator!)")

    # Default true to start the loop
    cont = True
    while cont:
        capital = False
        threeOrLess = False

        # Prompt user for a word
        userInput = input("\nPlease enter a word you would like to translate: ")
        translation = userInput

        # Check character count and capitalization
        if userInput[0].isupper():
            capital = True
        if len(userInput) <= 3:
            threeOrLess = True

        # Replace k's and put first letter at end
        translation = translation.lower().replace("k", "c").capitalize()

        # Use for loops to move the first letter to last letter
        wordUpdate = ""
        for letter in translation:
            if not letter.isupper():
                wordUpdate = wordUpdate + letter
        for letter in translation:
            if letter.isupper():
                wordUpdate = wordUpdate + letter
        translation = wordUpdate.lower()

        # Add random letter or en depending on length
        if threeOrLess:
            translation = translation + "en"
        else:
            num = random.randrange(5)
            if num == 0:
                translation = translation + "a"
            elif num == 1:
                translation = translation + "ë"
            elif num == 2:
                translation = translation + "i"
            elif num == 3:
                translation = translation + "o"
            else:
                translation = translation + "u"

        # Recapitalize
        if capital:
            translation = translation.capitalize()

        # Print out the word and reprompt to continue
        print("\'" + userInput + "\' in elvish is: " + translation)
        newInput = input("\nWould you like to translate another word? (y/n): ").lower()
        if newInput == "n":
            cont = False
    print("\nOodbyega! Aveha aen icenë ayden!\n(Goodbye! Have a nice day!)")


main()
