# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 6-1


def main():
    # Obtain sentences and create lists
    sentence = input("Please enter a sentence (including numbers): ")
    sentenceList = list(sentence)
    onlyNumbersList = list()
    onlyLettersList = list()
    numberList = list()
    letterList = list()

    # Create dashed lists
    for char in sentenceList:
        if char.isalpha():
            numberList.append(char)
            letterList.append("-")
            onlyLettersList.append(char)
        elif char.isdigit():
            numberList.append("-")
            letterList.append(char)
            onlyNumbersList.append(char)

    # Print out the breakdowns
    print("\nHere is the sentence breakdown:\n\nLETTERS:")
    if len(onlyLettersList):
        print("".join(letterList))
        print("Letters occur at the following positions:")
        for i in range(len(sentenceList)):
            if sentenceList[i].isalpha():
                print(i, end=" ")
    else:
        print("NONE")

    print("\n\nNUMBERS:")
    if len(onlyNumbersList):
        print("".join(numberList))
        print("Numbers occur at the following positions:")
        for i in range(len(sentenceList)):
            if sentence[i].isdigit():
                print(i, end=" ")
    else:
        print("NONE")


main()
