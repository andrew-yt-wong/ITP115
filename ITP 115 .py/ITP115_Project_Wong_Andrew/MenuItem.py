# Andrew Wong, awong827
# ITP 115, Spring 2020
# Final Project
# Description:
# MenuItem Class


# ---- MenuItem ---------------------------------------------------------------
#
# -----------------------------------------------------------------------------
class MenuItem(object):

    # ---- __init__ -----------------------------------------------------------
    #
    # Input:        string, string, float, string
    # Output:       none
    # Side Effect:  none
    # Description:  constructor for MenuItem class
    # -------------------------------------------------------------------------
    def __init__(self, name, type, price, description):
        self.name = name
        self.type = type
        self.price = price
        self.description = description

    # ---- getName ------------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  getter for name instance variable
    # -------------------------------------------------------------------------
    def getName(self):
        return self.name

    # ---- getType ------------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  getter for type instance variable
    # -------------------------------------------------------------------------
    def getType(self):
        return self.type

    # ---- getPrice -----------------------------------------------------------
    #
    # Input:        none
    # Output:       float
    # Side Effect:  none
    # Description:  getter for price instance variable
    # -------------------------------------------------------------------------
    def getPrice(self):
        return self.price

    # ---- getDescription -----------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  getter for description instance variable
    # -------------------------------------------------------------------------
    def getDescription(self):
        return self.description

    # ---- setName ------------------------------------------------------------
    #
    # Input:        string
    # Output:       none
    # Side Effect:  none
    # Description:  setter for name instance variable
    # -------------------------------------------------------------------------
    def setName(self, name):
        self.name = name

    # ---- setType ------------------------------------------------------------
    #
    # Input:        string
    # Output:       none
    # Side Effect:  none
    # Description:  setter for type instance variable
    # -------------------------------------------------------------------------
    def setType(self, type):
        self.type = type

    # ---- setPrice -----------------------------------------------------------
    #
    # Input:        float
    # Output:       none
    # Side Effect:  none
    # Description:  setter for price instance variable
    # -------------------------------------------------------------------------
    def setPrice(self, price):
        self.price = price

    # ---- setDescription -----------------------------------------------------
    #
    # Input:        string
    # Output:       float
    # Side Effect:  none
    # Description:  setter for description instance variable
    # -------------------------------------------------------------------------
    def setDescription(self, description):
        self.description = description

    # ---- __str__ ------------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  allows object to be printable
    # -------------------------------------------------------------------------
    def __str__(self):
        firstLine = self.name + " (" + self.type + "): $" + str(self.price)
        secondLine = "\n\t" + self.description
        return firstLine + secondLine
