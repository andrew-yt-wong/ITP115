# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 7
# Description:
# Program simulates a game of rock-paper-scissors

import random


# ---- displayMenu --------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: Prints the menu for the game
# Description: Displays the menu and rules of the game
# -------------------------------------------------------
def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.")
    print("The rules of the game are:")
    print("\tRock smashes scissors")
    print("\tScissors cut paper")
    print("\tPaper covers rock")
    print("\tIf both the choices are the same, it's a tie")


# ---- getComputerChoice --------------------------------
#
# Input: None
# Output: int
#
# Side Effect: None
# Description: Choose a random number between 0-2
# -------------------------------------------------------
def getComputerChoice():
    return random.randrange(3)


# ---- getPlayerChoice ----------------------------------
#
# Input: None
# Output: int
#
# Side Effect: Prints out the options
# Description: Gets the players choice from user input
# -------------------------------------------------------
def getPlayerChoice():

    # Loops until a valid number between 0-2 is given
    validInput = False
    while not validInput:
        print("Please choose (0) for rock, (1) for paper or (2) for scissors")
        userInput = input("")
        if userInput.isdigit():
            userInputInt = int(userInput)
            if 2 >= userInputInt >= 0:
                return userInputInt


# ---- playRound ----------------------------------------
#
# Input: int, int
# Output: int
#
# Side Effect: Prints out the choices and winner
# Description: Given the two options, determines who wins
# -------------------------------------------------------
def playRound(computerChoice, playerChoice):

    # Print out the player option
    if playerChoice == 2:
        print("You chose Scissors.")
    elif playerChoice == 1:
        print("You chose Paper.")
    else:
        print("You chose Rock.")

    # Print out the computer option
    if computerChoice == 2:
        print("The computer chose Scissors.")
    elif computerChoice == 1:
        print("The computer chose Paper.")
    else:
        print("The computer chose Rock.")

    # Print out if the player has won
    if playerChoice == 2 and computerChoice == 1:
        print("Scissors cut paper. Player wins!")
        return 1
    if playerChoice == 1 and computerChoice == 0:
        print("Paper covers rock. Player wins!")
        return 1
    if playerChoice == 0 and computerChoice == 2:
        print("Rock smashes scissors. Player wins!")
        return 1

    # Print out if the computer has won
    if computerChoice == 2 and playerChoice == 1:
        print("Scissors cut paper. Computer wins!")
        return -1
    if computerChoice == 1 and playerChoice == 0:
        print("Paper covers rock. Computer wins!")
        return -1
    if computerChoice == 0 and playerChoice == 2:
        print("Rock smashes scissors. Computer wins!")
        return -1

    # Default if it is a tie
    print("Both choices are the same, it's a tie!")
    return 0


# Returns true or false whether we continue the game
def continueGame():

    # Loop until a valid y or n is given
    validOption = False
    while not validOption:
        option = input("Do you want to continue playing (y or n)? ").lower()
        if option == "y":
            return True
        if option == "n":
            return False


# ---- main ---------------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: Prints out the winner and scores
# Description: The main function to run the game
# -------------------------------------------------------
def main():

    # continue is originally true, initialize the counts
    contGame = True
    computerWins = 0
    playerWins = 0
    ties = 0

    # Loop until game is over
    while contGame:

        # Display menu, get choices, and play the round
        displayMenu()
        computer = getComputerChoice()
        player = getPlayerChoice()
        score = playRound(computer, player)

        # Determine who won and the score to update
        if score == -1:
            computerWins += 1
        elif score == 1:
            playerWins += 1
        else:
            ties += 1

        # Check if we are continuing
        contGame = continueGame()
        print("")

    # Done playing so we print out the totals and end the program
    print("You won", playerWins, "games(s).")
    print("The computer won", computerWins, "games(s).")
    print("You tied with the computer", ties, "times(s).")
    print("\nThanks for playing!")


main()
