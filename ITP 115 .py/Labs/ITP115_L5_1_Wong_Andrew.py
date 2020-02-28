# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 5-1
import random


def main():
    quitProgram = False
    articles = ['a', 'the']
    nouns = ['person', 'place', 'thing']
    verbs = ['danced', 'ate', 'frolicked']
    while not quitProgram:
        print("\tWelcome to the Sentence Generator\n\tMenu")
        print("\t1) View Words\n\t2) Add Words\n\t3) Remove Words")
        print("\t4) Generate Sentence\n\t5) Exit\n")
        option = input("> ")
        if option.isdigit():
            optionInt = int(option)
            if optionInt == 1:
                print("articles: [", end="")
                for word in articles:
                    print("\'" + word + "\'", end="")
                    if word != articles[len(articles) - 1]:
                        print(", ", end="")
                print("]\nnouns: [", end="")
                for word in nouns:
                    print("\'" + word + "\'", end="")
                    if word != nouns[len(nouns) - 1]:
                        print(", ", end="")
                print("]\nverbs: [", end="")
                for word in verbs:
                    print("\'" + word + "\'", end="")
                    if word != verbs[len(verbs) - 1]:
                        print(", ", end="")
                print("]\n")
            elif optionInt == 2:
                validOption = False
                while not validOption:
                    newAdd = input("Enter 1) for nouns or 2) for verbs: ")
                    if newAdd.isdigit():
                        newAddInt = int(newAdd)
                        if newAddInt == 1:
                            nouns.append(input("Enter the word: "))
                            validOption = True
                            print("")
                        elif newAddInt == 2:
                            verbs.append(input("Enter the word: "))
                            validOption = True
                            print("")
                        else:
                            print("Invalid Choice.\n")
                    else:
                        print("Invalid Choice.\n")
            elif optionInt == 3:
                validOption = False
                while not validOption:
                    newRemove = input("Enter 1) for nouns or 2) for verbs: ")
                    if newRemove.isdigit():
                        newRemoveInt = int(newRemove)
                        removeWord = input("Enter the word: ")
                        if newRemoveInt == 1:
                            if removeWord in nouns:
                                nouns.remove(removeWord)
                            else:
                                print("word not in list")
                            validOption = True
                            print("")
                        elif newRemoveInt == 2:
                            if removeWord in verbs:
                                verbs.remove(removeWord)
                            else:
                                print("word not in list")
                            validOption = True
                            print("")
                        else:
                            print("Invalid Choice.\n")
                    else:
                        print("Invalid Choice.\n")
            elif optionInt == 4:
                print(random.choice(articles), random.choice(nouns),
                      random.choice(verbs), random.choice(articles),
                      random.choice(nouns), "\n")
            elif optionInt == 5:
                print("Program will exit\nHave a great day!")
                quitProgram = True
            else:
                print("Invalid Choice.\n")
        else:
            print("Invalid Choice.\n")


main()
