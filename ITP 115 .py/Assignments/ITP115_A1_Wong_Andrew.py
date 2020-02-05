# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 1
# Description:
# This program creates a Mad Libs story.
# It gets input from the user and prints output.


def main():
    # Read in each word individually
    animal = input("Enter an animal: ")
    adj = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    verb = input("Enter a verb: ")
    ing = input("Enter a verb that ends with 'ing': ")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    num3 = int(input("Enter a third number: "))
    dec = float(input("Enter a number with a decimal: "))

    # print out the story with quotes around the words
    print("\nToday, Ricky the \"" + adj + "\" \"" + animal + "\"",
          "plans to \"" + verb + "\" for \"" + str(dec) + "\"",
          "hours.\nHe did it for \"" + str(num1) + "\" hours the day before yesterday",
          "and \"" + str(num2) + "\" hours\nyesterday with a current",
          "total of \"" + str(num1+num2) + "\" hours.",
          "Tomorrow he is \"" + ing + "\"\nfor \"" + str(num3) + "\" hours,",
          "how \"" + adj2 + "\" right?")


main()
