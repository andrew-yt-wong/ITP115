# Andrew Wong, awong827
# ITP 115, Spring 2020
# Final Project
# Description:
# Menu Class


from MenuItem import MenuItem


# ---- Menu -------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # ---- __init__ -----------------------------------------------------------
    #
    # Input:        string
    # Output:       none
    # Side Effect:  none
    # Description:  constructor for Menu class
    # -------------------------------------------------------------------------
    def __init__(self, fileName):
        self.menuItemDictionary = {}
        for item_type in Menu.MENU_ITEM_TYPES:
            self.menuItemDictionary[item_type] = []
        fileIn = open(fileName, "r")
        for line in fileIn:
            line = line.strip()
            item = line.split(",")
            menuItem = MenuItem(item[0], item[1], float(item[2]), item[3])
            self.menuItemDictionary[item[1]].append(menuItem)
        fileIn.close()

    # ---- getMenuItem --------------------------------------------------------
    #
    # Input:        string, int
    # Output:       MenuItem
    # Side Effect:  none
    # Description:  get MenuItem from dictionary
    # -------------------------------------------------------------------------
    def getMenuItem(self, item_type, index):
        return self.menuItemDictionary[item_type][index]

    # ---- printMenuItemsByType -----------------------------------------------
    #
    # Input:        string
    # Output:       none
    # Side Effect:  none
    # Description:  print header with type of menu items with the list
    # -------------------------------------------------------------------------
    def printMenuItemsByType(self, item_type):
        print("\n-----" + item_type.upper() + "-----")
        for i in range(0, self.getNumMenuItemsByType(item_type)):
            print(str(i) + ") ", end="")
            print(self.menuItemDictionary[item_type][i])

    # ---- getNumMenuItemsByType ----------------------------------------------
    #
    # Input:        string
    # Output:       int
    # Side Effect:  none
    # Description:  get number of menu items for that type
    # -------------------------------------------------------------------------
    def getNumMenuItemsByType(self, item_type):
        return len(self.menuItemDictionary[item_type])
