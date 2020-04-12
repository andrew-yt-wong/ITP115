# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 10-2


# ---- readFile -----------------------------------------
#
# Input: string
# Output: list of words
#
# Side Effect: None
# Description: Read in each word and store it in a list
# -------------------------------------------------------
def readFile(fileName):
    fileIn = open(fileName, "r")
    dictionaryList = list()
    for line in fileIn:
        word = line.strip()
        dictionaryList.append(word)
    fileIn.close()
    return dictionaryList


# ---- findWord -----------------------------------------
#
# Input: list of strings, string
# Output: boolean
#
# Side Effect: None
# Description: Returns True if word is in dictionary
# -------------------------------------------------------
def findWord(wordsList, searchWord):
    for word in wordsList:
        if word == searchWord:
            return True
    return False


# ---- writeFile --------------------------------------------
#
# Input: list of strings, string
# Output: None
#
# Side Effect: None
# Description: Loop through and print words to file
# -------------------------------------------------------
def writeFile(outputList, fileName):
    fileOut = open(fileName, "w")
    for word in outputList:
        print(word, file=fileOut)
    fileOut.close()


# ---- main --------------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: Prints the instructions
# Description: Calls the dictionary and checks words
# -------------------------------------------------------
def main():
    print("Welcome to Word Checker")
    fileIn = input("Enter the name of the file you wish to read in: ")
    fileOut = input("Enter the name of the file you wish to write to: ")
    word = input("Enter the word you wish to check: ")
    wordsList = readFile(fileIn)
    if not findWord(wordsList, word):
        wordsList.append(word)
        print(word, "has been added to the dictionary.")
    else:
        print(word, "is already in the dictionary.")
    writeFile(wordsList, fileOut)
    print("The word list has been written to", fileOut)


main()
