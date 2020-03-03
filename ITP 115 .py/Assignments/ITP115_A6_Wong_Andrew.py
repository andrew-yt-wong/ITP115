# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 6
# Description:
# Airline Tickets that store people's tickets and print out them out


# Global Variables
TOTAL_SEATS = 10


def main():
    # Start with no filled seats and initialize them to empty
    numFilledSeats = 0
    seatingChart = list()
    for i in range(TOTAL_SEATS):
        seatingChart.append("")

    # While we don't quit, keep the program running
    quitting = False
    while not quitting:
        # Print out the menu
        print("1: Assign Seat")
        print("2: Print Seat Map")
        print("3: Print Boarding Pass")
        print("-1: Quit")

        # Ask for a value until given a proper one
        validValue = False
        value = input("\n> ")
        valueInt = 0
        while not validValue:
            # Validate the value
            if value.isdigit():
                valueInt = int(value)
                if valueInt < 1 or valueInt > 3:
                    value = input("Please enter choice: ")
                else:
                    validValue = True
            else:
                if value == "-1":
                    valueInt = int(value)
                    validValue = True
                else:
                    value = input("Please enter choice: ")

        # Check which value we got, else by default is -1
        if valueInt == 1:
            # Check the capacity
            if numFilledSeats == 10:
                print("Next flight leaves in 3 hours.")
            else:
                name = input("Please enter your first name: ")
                seatingChart[numFilledSeats] = name
                numFilledSeats += 1
        # Print out all of the seats
        elif valueInt == 2:
            print("***************************************")
            # Run a for loop to print out all of the seats
            for i in range(TOTAL_SEATS):
                if len(seatingChart[i]) == 0:
                    name = "Empty"
                else:
                    name = seatingChart[i]
                print("\tSeat #" + str(i + 1) + ":\t" + name)
            print("***************************************\n")
        # Access which type of search
        elif valueInt == 3:
            print("Type 1 to get Boarding Pass by seat number")
            print("Type 2 to get Boarding Pass by name")
            validType = False
            typeInt = 0
            # Make sure you get a valid response of 1 or 2
            while not validType:
                myType = input("")
                if myType.isdigit():
                    typeInt = int(myType)
                    if typeInt > 2 or typeInt < 1:
                        print("Invalid Choice, please enter a valid number")
                    else:
                        validType = True
                else:
                    print("Invalid Choice, please enter a valid number")

            # If 1, just access it and check if it's empty
            if typeInt == 1:
                seat = input("What is the seat number: ")
                if seat.isdigit():
                    seatNum = int(seat)
                    if seatNum > 10 or seatNum < 1:
                        print("Invalid number--no boarding pass found\n")
                    elif len(seatingChart[seatNum - 1]) == 0:
                        print("Invalid number--no boarding pass found\n")
                    else:
                        print("\n======= BOARDING PASS =======")
                        print("\tSeat #:", seatNum)
                        print("\tPassenger Name: " + seatingChart[seatNum - 1])
                        print("=============================\n")
                else:
                    print("Invalid number--no boarding pass found\n")

            # Run linear search
            else:
                name = input("Enter passenger name: ")
                found = False
                for i in range(TOTAL_SEATS):
                    if seatingChart[i].lower() == name.lower():
                        print("\n======= BOARDING PASS =======")
                        print("\tSeat #:", (i + 1))
                        print("\tPassenger Name: " + seatingChart[i])
                        print("=============================\n")
                        found = True
                if not found:
                    print("No passenger with name " + name + " was found\n")
        else:
            print("Have a nice day!")
            quitting = True


main()
