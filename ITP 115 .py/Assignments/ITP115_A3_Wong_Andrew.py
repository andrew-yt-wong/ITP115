# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 3
# Description:
# Using while loops, get the largest and smallest user inputted integer


def main():
    # Initialize to start asking
    cont = True
    while cont:
        noInputs = False
        validNum = False
        while not validNum:
            # Ask for a single integer, assumes will get valid (not -1)
            userInt = int(input("Input an integer greater than or equal to 0 or -1 to quit:\n> "))

            # Initialize max, min, sum, and count
            maxInt = userInt
            minInt = userInt
            totalSum = userInt
            count = 1

            # Check if it was valid
            if userInt > -1:
                validNum = True
            elif userInt == -1:
                validNum = True
                noInputs = True
            else:
                print("\nInvalid input, please enter a proper input");

        if not noInputs:
            # Loop until -1 is given
            while userInt != -1:
                userInt = int(input("> "))

                # Check if we should be adding to the count/sum
                if userInt != -1:
                    count += 1
                    totalSum += userInt

                    # Check if we need to update min
                    if minInt > userInt:
                        minInt = userInt

                    # Check if we need to update max
                    if maxInt < userInt:
                        maxInt = userInt

            # Display the largest, smallest, and average values
            print("The largest number is", maxInt)
            print("The smallest number is", minInt)
            print("The average number is", totalSum / count)

        # Prompt the user to check if we should continue a new process
        validAnswer = False
        while not validAnswer:
            userInput = input("\nWould you like to enter another set of numbers? (y/n): ").lower()
            if userInput == "n":
                cont = False
                validAnswer = True
            elif userInput == "y":
                cont = True
                validAnswer = True
            else:
                print("\nInvalid Option, please try again!");

    # Function complete, let the user know you are leaving!
    print("\nGoodbye!")


main()
