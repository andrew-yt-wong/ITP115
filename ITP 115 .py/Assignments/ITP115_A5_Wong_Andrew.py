# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 5
# Description:
# Word Jumbled and Encryption

import random


def main():
    # Word Jumbled
    wordBank = ["trash", "dog", "feline", "school", "professor"]

    # Pick a random word from the wordBank
    word = random.choice(wordBank)
    scrambledWord = list(word[:])

    # Shuffle the word using a for loop
    for letter in range(len(scrambledWord) - 1, 0, -1):
        index = random.randrange(len(scrambledWord))
        temp = scrambledWord[letter]
        scrambledWord[letter] = scrambledWord[index]
        scrambledWord[index] = temp

    # Convert the word back into a string
    print("The jumbled word is \"" + "".join(scrambledWord) + "\"")

    # Loop until they guess correctly
    numGuesses = 0
    guessedCorrectly = False
    while not guessedCorrectly:
        guess = input("Please enter your guess: ").lower()
        numGuesses += 1
        if guess == word:
            print("You got it!")
            print("It took you", numGuesses, "tries.")
            guessedCorrectly = True
        else:
            print("Try again.")

    # Encryption
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetList = list(alphabet)

    # Get their message
    message = input("\nEnter a message: ").lower()

    # Loop until a valid shift number is given
    isValid = False
    shift = 0
    while not isValid:
        shiftBy = input("Enter a number to shift by (0-25): ")
        if shiftBy.isnumeric() and 0 <= int(shiftBy) <= 25:
            isValid = True
            shift = int(shiftBy)
        else:
            print("Invalid, please try again.")

    # Create the cipher list
    cipherList = list()
    for index in range(0, len(alphabetList)):
        newIndex = index + shift
        if newIndex > 25:
            newIndex -= 26
        cipherList.append(alphabetList[newIndex])

    # Encrypt the message
    print("Encrypting message...")
    encryptedMessage = ""
    for letter in message:
        if letter.isalpha():
            index = alphabetList.index(letter)
            letter = cipherList[index]
        encryptedMessage += letter

    print("\tEncrypted message:", encryptedMessage)

    # Decrypt the message
    print("Decrypting message...")
    decryptedMessage = ""
    for letter in encryptedMessage:
        if letter.isalpha():
            index = cipherList.index(letter)
            letter = alphabetList[index]
        decryptedMessage += letter

    # Compare the decrypted to the original
    print("\tDecrypted message:", decryptedMessage)
    print("\tOriginal message:", message)


main()
