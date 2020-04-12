# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Assignment 9
# Description:
# Language Translator


# ---- getLanguages -------------------------------------
#
# Input: string
# Output: list of strings
#
# Side Effect:
#   None
# Description:
#   Open the CSV file and get the header row with the
#   languages and put it into a list. Close the file and
#   return the list.
# -------------------------------------------------------
def getLanguages(fileName = "languages.csv"):
    fileIn = open(fileName, "r")
    header = fileIn.readline()
    languages = header.split(",")
    fileIn.close()
    return languages


# ---- getSecondLanguage --------------------------------
#
# Input: list of strings
# Output: string
#
# Side Effect:
#   Display to the user the languages that are
#   available for translation.
# Description:
#   Get input from the user for the second language.
#   They must enter in a valid language. The user’s
#   input is not case sensitive. Return the language.
# -------------------------------------------------------
def getSecondLanguage(langList):
    print("Translate", langList[0], "words to one of the following languages:", end="")
    printCount = -1
    for lang in langList:
        if printCount == -1:
            printCount += 1
        else:
            if printCount % 7 == 0:
                print("\n\t", end="")
            print(lang, end="")
            printCount += 1
            if printCount % 7 != 0:
                print(" ", end="")

    validInput = False
    while not validInput:
        secondLang = input("Enter a language: ").lower().capitalize()
        if secondLang in langList:
            validInput = True
            print()
            return secondLang
        else:
            print("This program does not support", secondLang)


# ---- readFile -----------------------------------------
#
# Input: list of strings, string, string
# Output: list of strings
#
# Side Effect:
#   None
# Description:
#   Open the CSV file and read the header row to skip it.
#   Use the langList and langStr parameters to determine
#   which column of data to save. Loop through the rest
#   of the file to create a list of words.
#   Close the file and return the list.
# -------------------------------------------------------
def readFile(langList, langStr = "English", fileName = "languages.csv"):
    index = langList.index(langStr)
    langWords = list()
    fileIn = open(fileName, "r")
    fileIn.readline()
    for line in fileIn:
        line = line.strip()
        wordList = line.split(",")
        langWords.append(wordList[index])
    fileIn.close()
    return langWords


# ---- createResultsFile --------------------------------
#
# Input: string, string
# Output: None
#
# Side Effect:
#   None
# Description:
#   Open the results text file such that if there is
#   an existing file, it will be overwritten.
#   Write text to the file stating the second language.
#   Close the file.
# -------------------------------------------------------
def createResultsFile(language, resultsFile):
    fileOut = open(resultsFile, "w")
    print("Words translated from English to", language, file=fileOut)
    fileOut.close()


# ---- translateWords -----------------------------------
#
# Input: list of strings, list of strings, string
# Output: None
#
# Side Effect:
#   None
# Description:
#   Translate the given words
# -------------------------------------------------------
def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile, "a")
    wordsLeft = True
    while wordsLeft:
        word = input("\nEnter a word to translate: ").lower()
        if word in englishList:
            translation = secondList[englishList.index(word)]
            if translation == "-":
                print(word, "did not have a translation.")
            else:
                print(word, "is translated to", translation)
                print(word, "=", translation, file=fileOut)
        else:
            print(word, "is not in the English list.")
        validOption = False
        while not validOption:
            option = input("Another word (y or n)? ").lower()
            if option == "n":
                validOption = True
                wordsLeft = False
            elif option == "y":
                validOption = True
    print("\nTranslated words have been saved to", resultsFile)
    fileOut.close()


# ---- main ---------------------------------------------
#
# Input: None
# Output: None
#
# Side Effect:
#   None
# Description:
#   main program
# -------------------------------------------------------
def main():
    print("Language Translator")
    langList = getLanguages()
    langStr = getSecondLanguage(langList)
    englishList = readFile(langList)
    secondList = readFile(langList, langStr)
    fileName = input("Enter a name for the results file (return key for " + langStr + ".txt): ")
    if fileName == "":
        fileName = langStr + ".txt"
    createResultsFile(langStr, fileName)
    translateWords(englishList, secondList, fileName)


main()
