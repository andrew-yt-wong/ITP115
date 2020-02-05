# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 2-1


def main():
    # Prompt the user for the inputs
    size = input("What size coffee do you want (S, M, L)? ")
    temp = int(input("What temperature would you like (in degrees)? "))
    type = input("What type of beans / blend would you like? ")
    cream = input("Would you like room for cream (y/n)? ")

    # Start the printed sentence (tabbed)
    print("\tYou ordered a ", end="")

    # Print large, medium, or small depending on the input
    if size == "L" or size == "l":
        print("large ", end="")
    elif size == "M" or size == "m":
        print("medium ", end="")
    else:
        print("small ", end="")

    # Print hot if its 90 degrees F or above
    if temp >= 90:
        print("hot ", end="")
    else:
        print("cold ", end="")

    # Print the type of coffee
    print(type, end="")

    # Print cream or no cream
    if cream == "Y" or cream == "y":
        print(" with cream")
    else:
        print(" with no cream")


main()
