# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 8
# Description:
# Program simulates a game of TicTacToe

import TicTacToeHelper


# ---- isValidMove --------------------------------------
#
# Input: list, int
# Output: boolean
#
# Side Effect: None
# Description: Return True if spot is open, False if not
# -------------------------------------------------------
def isValidMove(boardList, spot):
    if spot.isdigit():
        if 0 <= int(spot) <= 9:
            if boardList[int(spot)].isdigit():
                return True
    return False


# ---- updateBoard --------------------------------------
#
# Input: list, int, string
# Output: None
#
# Side Effect: None
# Description: Takes current board and places new letter
# -------------------------------------------------------
def updateBoard(boardList, spot, playerLetter):
    boardList[int(spot)] = playerLetter


# ---- playGame -----------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: Prints out the board
# Description: Initialize empty board and plays the game
# -------------------------------------------------------
def playGame():
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    numMoves = 0
    currentPlayer = "x"
    while TicTacToeHelper.checkForWinner(boardList, numMoves) == "n":
        TicTacToeHelper.printUglyBoard(boardList)
        spotInvalid = True
        while spotInvalid:
            spot = input("Player " + currentPlayer + ", pick a spot: ")
            if isValidMove(boardList, spot):
                updateBoard(boardList, spot, currentPlayer)
                spotInvalid = False
            else:
                print("Invalid move, please try again.")
        if currentPlayer == "x":
            currentPlayer = "o"
        else:
            currentPlayer = "x"
        numMoves += 1
    TicTacToeHelper.printUglyBoard(boardList)
    print("\nGame Over!")
    if TicTacToeHelper.checkForWinner(boardList, numMoves) == "x":
        print("Player x is the winner!")
    elif TicTacToeHelper.checkForWinner(boardList, numMoves) == "o":
        print("Player o is the winner!")
    else:
        print("Stalemate reached!")


# ---- main ---------------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: None
# Description: Keep playing game until user quits
# -------------------------------------------------------
def main():
    print("Welcome to Tic Tac Toe!")
    quitGame = False
    while not quitGame:
        playGame()
        validResponse = False
        while not validResponse:
            response = input("Would you like to play another round (y/n): ").lower()
            if response == "n":
                quitGame = True
                validResponse = True
            elif response == "y":
                validResponse = True
            else:
                print("Invalid response, please try again.")
    print("Goodbye!")


main()
