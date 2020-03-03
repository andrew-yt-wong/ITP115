# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 6-2


def main():
    # Get the words and convert them into various lists
    firstWord = input("Please enter a word or statement: ").replace(" ", "").lower()
    secondWord = input("Please enter a second word or statement: ").replace(" ", "").lower()
    firstWordList = list(firstWord)
    fRevCopy = firstWordList[:]
    fCopy = firstWordList[:]
    secondWordList = list(secondWord)
    sCopy = secondWordList[:]
    sRevCopy = secondWordList[:]
    fCopy.sort()
    sCopy.sort()
    fRevCopy.reverse()
    sRevCopy.reverse()

    # Compare all the lists
    if fCopy == sCopy:
        print("The two words you entered are anagrams")
    else:
        print("The two words you entered are not anagrams")

    if firstWordList == fRevCopy:
        print("The first word is a palindrome")
    else:
        print("The first word is not a palindrome")

    if secondWordList == sRevCopy:
        print("The second word is a palindrome")
    else:
        print("The second word is not a palindrome")




main()
