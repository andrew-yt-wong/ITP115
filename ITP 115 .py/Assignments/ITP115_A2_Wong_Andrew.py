# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 2
# Description:
# This program creates a harry potter vending machine.
# It determines change and gives a discount.


def main():
    # Give the user their options
    print("Please select an item from the vending machine:")
    print("\ta) Butterbeer: 58 knuts")
    print("\tb) Quill: 10 knuts")
    print("\tc) The Daily Prophet: 7 knuts")
    print("\td) Book of Spells: 400 knuts")
    print("\te) Book of Spells Family Combo: 600 knuts")
    userInput = input("> ")

    # Make it lowercase so easier checking
    userInput = userInput.lower()

    # Start with a base of 1 Galleon of Knuts
    totalMoney = 493;

    # By default no coupon
    instagramValid = False

    # Check if we have a valid option, otherwise default to option A
    if userInput != "a" and userInput != "b" and userInput != "c" and userInput != "d" and userInput != "e":
        print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
        userInput = "a"

    # Prompt for coupon
    instagram = input("Will you share this on Instagram? (y/n): ")
    instagram = instagram.lower()

    # Check coupon and print the proper message
    if instagram == "y":
        print("Thanks! You will get 5 knuts off your purchase\n")
        instagramValid = True
    elif instagram == "n":
        print("\n")
    else:
        print("You have entered an invalid option. No coupon will be used\n")

    # EXTRA CREDIT: Prompt for any number of Galleons
    numGalleons = 0
    if userInput == "e":
        while numGalleons < 2:
            numGalleons = int(input("How many galleons would you like to pay with? (at least 2): "))
    else:
        while numGalleons < 1:
            numGalleons = int(input("How many galleons would you like to pay with? (at least 1): "))

    # Fix number of Knuts by number of Galleons
    totalMoney *= numGalleons

    # Start printing the receipt
    print("You bought a ", end="")
    if userInput == "a":
        print("Butterbeer for 58 knuts ", end="")
        totalMoney -= 58
    elif userInput == "b":
        print("Quill for 10 knuts ", end="")
        totalMoney -= 10
    elif userInput == "c":
        print("The Daily Prophet for 7 knuts ", end="")
        totalMoney -= 7
    elif userInput == "d":
        print("Book of Spells for 400 knuts ", end="")
        totalMoney -= 400
    else:
        print("Book of Spells Family Combo for 600 knuts ", end="")
        totalMoney -= 600
    print("(with coupon of ", end="")

    # Check if we need to give back to totalMoney because of a coupon
    if instagramValid:
        print("5 ", end="")
        totalMoney += 5
    else:
        print("0 ", end="")

    # Print out how much they are paying with and how much change they get
    print("knuts) and paid with", numGalleons, "galleon(s).")
    print("Here is your change (" + str(totalMoney) + " knuts):")

    # Get the change
    print("Galleons:", totalMoney // 493)
    totalMoney %= 493
    print("Sickles:", totalMoney // 29)
    totalMoney %= 29
    print("Knuts:", totalMoney)


main()
