# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 1-1


def main():
    # Print box
    print(" _\n| |\n| |\n|_|\n")

    # Print Message
    print("You don't frighten us, English pig-dogs!" +
          "\nGo and boil your bottoms, sons of a silly person!" +
          "\n\t\t-\"Monty Python and the Holy Grail\"")

    # Get user inputs and print it out
    month = input("What month are we in?: ")
    day = input("What day is it?: ")
    dayOfMonth = int(input("What day of the month is today?: "))
    print("Today is", day, month, dayOfMonth, "and Tomorrow will be", month, dayOfMonth+1)


main()
