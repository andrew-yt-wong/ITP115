# Andrew Wong
# ITP 115, Spring 2020
# Lab 14-2
# awong827@usc.edu


def readFile(fileName):
    fileIn = open(fileName, "r")
    wordDict = {}
    lineNum = 1
    for line in fileIn:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word = word.lower().strip(".,:;?' ")
            if word != "":
                if word not in wordDict:
                    wordDict[word] = []
                wordDict[word].append(lineNum)
        lineNum += 1
    fileIn.close()
    return wordDict


def sortKeys(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    return keys


def main():
    wordDict = readFile("story.txt")
    print("Here is the concordance for the file \'story.txt\'")
    keys = sortKeys(wordDict)
    for key in keys:
        print(key + ":", wordDict[key])


main()