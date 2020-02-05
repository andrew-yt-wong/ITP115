# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 3-1


def main():
    numSpaces = 18
    numSymbols = 1
    currentRow = 1
    while currentRow <= 10:
        print(" " * numSpaces, end="")
        print(" ^" * numSymbols)
        numSymbols += 2
        numSpaces -= 2
        currentRow += 1


main()