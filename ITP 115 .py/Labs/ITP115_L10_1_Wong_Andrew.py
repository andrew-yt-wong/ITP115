# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 10-1


# ---- readDictionaryFile -------------------------------
#
# Input: string
# Output: list of strings
#
# Side Effect: None
# Description: Read in each word and store it in a list
# -------------------------------------------------------
def readDictionaryFile(fileName):
    fileIn = open(fileName, "r")
    dictionaryList = list()
    for line in fileIn:
        word = line.strip()
        dictionaryList.append(word)
    fileIn.close()
    return dictionaryList


# ---- checkWord ----------------------------------------
#
# Input: list of strings, string
# Output: boolean
#
# Side Effect: None
# Description: Return True if in dictionary
# -------------------------------------------------------
def checkWord(dictionaryList, word):
    for words in dictionaryList:
        if words == word:
            return True
    return False


# ---- main --------------------------------------------
#
# Input: None
# Output: None
#
# Side Effect: Prints the instructions
# Description: Calls the dictionary and checks words
# -------------------------------------------------------
def main():
    print("Welcome to the Spell Checker!")
    fileName = input("Please enter the dictionary file you wish to read in: ")
    word = input("Please enter the word you wish to spell check: ")
    dictionaryList = readDictionaryFile(fileName)
    if checkWord(dictionaryList, word):
        print("That word is in the dictionary.")
    else:
        print("That word is NOT in the dictionary, so it must be spelled wrong.")


main()
