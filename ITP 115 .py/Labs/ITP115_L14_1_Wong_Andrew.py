# Andrew Wong
# ITP 115, Spring 2020
# Lab 14-1
# awong827@usc.edu


def readFile(fileName):
    fileIn = open(fileName, "r")
    letters = {}
    for line in fileIn:
        line = line.strip()
        for letter in line:
            letter = letter.lower()
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    return letters
    fileIn.close()


def sortKeys(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    return keys


def main():
    print("Displaying letter frequency of the Gettysburg Address")
    letters = readFile("gettysburg.txt")
    keys = sortKeys(letters)
    for key in keys:
        print(key, letters[key])


main()
