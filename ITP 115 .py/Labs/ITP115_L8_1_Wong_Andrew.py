# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 8-1


# Wants to continue function that checks whether the user is going to continue
def wantsToContinue():
    # Loop until a valid response is given
    validResponse = False
    while not validResponse:
        # Retrieve the response and capitalize it
        response = input("Do you want to continue (y/n)? ").upper()
        # Check whether we continue or not, if it is invalid we will loop
        if response == "Y":
            validResponse = True
            return True
        elif response == "N":
            validResponse = True
            return False


# Converts a given temperature given the type of conversion and temp
def temperatureConverter(conversionType, inputTemperature):
    # Check which type of conversion if any and return the value
    if conversionType == 1:
        return (inputTemperature - 32) * 5 / 9
    elif conversionType == 2:
        return (inputTemperature * 9 / 5) + 32
    else:
        print("Invalid conversion code")
        return 0


# Main Function that calls the other two functions
def main():
    # Continue while the user wants to
    cont = True
    while cont:
        print("Welcome to the Temperature Converter 1.0")
        conversionType = int(input("Enter 1 for F->C, or 2 for C->F: "))
        inputTemperature = int(input("Enter input temperature: "))
        convertedTemp = temperatureConverter(conversionType, inputTemperature)
        print("The converted temperature is", convertedTemp)
        cont = wantsToContinue()
        print("")


main()
