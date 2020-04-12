# Andrew Wong, awong827
# ITP 115, Spring 2020
# Assignment 10
# Description:
# Animal Daycare


# ---- Animal -----------------------------------------------------------------
#
# -----------------------------------------------------------------------------
class Animal(object):

    # ---- __init__ -----------------------------------------------------------
    #
    # Input:        int, int, int, int, int, string, string
    # Output:       none
    # Side Effect:  none
    # Description:  constructor for Animal class
    # -------------------------------------------------------------------------
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

    # ---- play ---------------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  increase happiness by 10, increase hunger by 5
    # -------------------------------------------------------------------------
    def play(self):
        if self.happiness > 90:
            self.happiness = 100
        else:
            self.happiness += 10
        if self.hunger > 95:
            self.hunger = 100
        else:
            self.hunger += 5

    # ---- feed ---------------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  decrease hunger by 10
    # -------------------------------------------------------------------------
    def feed(self):
        if self.hunger < 10:
            self.hunger = 0
        else:
            self.hunger -= 10

    # ---- giveMedicine -------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  decrease happiness by 20, increase health by 20
    # -------------------------------------------------------------------------
    def giveMedicine(self):
        if self.happiness < 20:
            self.happiness = 0
        else:
            self.happiness -= 20
        if self.health > 80:
            self.health = 100
        else:
            self.health += 20

    # ---- sleep --------------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  increase energy by 20, increase age by 1
    # -------------------------------------------------------------------------
    def sleep(self):
        if self.energy > 80:
            self.energy = 100
        else:
            self.energy += 20
        self.age += 1

    # ---- __str__ ------------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  allows object to be printable
    # -------------------------------------------------------------------------
    def __str__(self):
        name = "Name: " + self.name + " the " + self.species + "\n"
        health = "Health: " + str(self.health) + "\n"
        happiness = "Happiness: " + str(self.happiness) + "\n"
        hunger = "Hunger: " + str(self.hunger) + "\n"
        energy = "Energy: " + str(self.energy) + "\n"
        age = "Age: " + str(self.age) + "\n"
        stars = "********************************"
        return name + health + happiness + hunger + energy + age + stars


# ---- loadAnimals ------------------------------------------------------------
#
# Input:        string
# Output:       list of Animals
# Side Effect:  file opened and closed
# Description:  open file, store information into list
# -----------------------------------------------------------------------------
def loadAnimals(fileName):
    fileIn = open(fileName, "r")
    animalList = list()
    for line in fileIn:
        line = line.strip()
        lineList = line.split(",")
        hunger = int(lineList[0])
        happiness = int(lineList[1])
        health = int(lineList[2])
        energy = int(lineList[3])
        age = int(lineList[4])
        name = lineList[5]
        species = lineList[6]
        animal = Animal(hunger, happiness, health, energy, age, name, species)
        animalList.append(animal)
    fileIn.close()
    return animalList


# ---- displayMenu ------------------------------------------------------------
#
# Input:        none
# Output:       none
# Side Effect:  prints menu
# Description:  prints menu of possible options
# -----------------------------------------------------------------------------
def displayMenu():
    print("\n1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Exit")


# ---- selectAnimal -----------------------------------------------------------
#
# Input:        list of Animals
# Output:       Animal
# Side Effect:  retrieves user input
# Description:  asks user to make selection and returns that choice
# -----------------------------------------------------------------------------
def selectAnimal(animalList):
    validInput = False
    choiceInt = 0
    count = 1
    for animal in animalList:
        print(str(count) + ") " + animal.name + " the " + animal.species)
        count += 1
    while not validInput:
        choice = input("\nPlease select an animal from the list (enter the 1-" + str(len(animalList)) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= len(animalList):
            validInput = True
            choiceInt = int(choice)
        else:
            print("Invalid input, please try again!")
    return animalList[choiceInt - 1]


# ---- main -------------------------------------------------------------------
#
# Input:        none
# Output:       none
# Side Effect:  none
# Description:  call the other functions until the user is done
# -----------------------------------------------------------------------------
def main():
    animalList = loadAnimals("animals.csv")
    userExit = False

    print("Welcome to the Animal Daycare! Here is what we can do: ")
    while not userExit:
        validSelection = False
        selectionInt = 0
        while not validSelection:
            displayMenu()
            selection = input("\nPlease make a selection: ")
            if selection.isdigit() and 1 <= int(selection) <= 7:
                validSelection = True
                selectionInt = int(selection)
            else:
                print("*Invalid selection, please try again.")
        if selectionInt == 1:
            animal = selectAnimal(animalList)
            animal.play()
            print("You played with " + animal.name + " the " + animal.species + "!")
        elif selectionInt == 2:
            animal = selectAnimal(animalList)
            animal.feed()
            print("You fed " + animal.name + " the " + animal.species + "!")
        elif selectionInt == 3:
            animal = selectAnimal(animalList)
            animal.giveMedicine()
            print("You gave " + animal.name + " the " + animal.species + " some medicine!")
        elif selectionInt == 4:
            animal = selectAnimal(animalList)
            animal.sleep()
            print(animal.name + " the " + animal.species + " took a nap!")
        elif selectionInt == 5:
            animal = selectAnimal(animalList)
            print(animal)
        elif selectionInt == 6:
            for animal in animalList:
                print(animal)
        else:
            userExit = True
    print("Goodbye!")


main()
