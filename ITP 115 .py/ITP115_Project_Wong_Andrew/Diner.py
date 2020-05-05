# Andrew Wong, awong827
# ITP 115, Spring 2020
# Final Project
# Description:
# Diner Class


from MenuItem import MenuItem


# ---- Diner ------------------------------------------------------------------
#
# -----------------------------------------------------------------------------
class Diner(object):
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # ---- __init__ -----------------------------------------------------------
    #
    # Input:        string
    # Output:       none
    # Side Effect:  none
    # Description:  constructor for Diner class
    # -------------------------------------------------------------------------
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    # ---- getName ------------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  getter for name instance variable
    # -------------------------------------------------------------------------
    def getName(self):
        return self.name

    # ---- getOrder -----------------------------------------------------------
    #
    # Input:        none
    # Output:       float
    # Side Effect:  none
    # Description:  getter for order instance variable
    # -------------------------------------------------------------------------
    def getOrder(self):
        return self.order

    # ---- getStatus ----------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  getter for status instance variable
    # -------------------------------------------------------------------------
    def getStatus(self):
        return self.status

    # ---- updateStatus -------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  increase diner's status by 1
    # -------------------------------------------------------------------------
    def updateStatus(self):
        self.status += 1

    # ---- addToOrder ---------------------------------------------------------
    #
    # Input:        MenuItem
    # Output:       none
    # Side Effect:  none
    # Description:  adds menu item to end of list
    # -------------------------------------------------------------------------
    def addToOrder(self, item):
        self.order.append(item)

    # ---- printOrder ---------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  print message containing all menu items ordered
    # -------------------------------------------------------------------------
    def printOrder(self):
        for item in self.order:
            print("-", item)

    # ---- calculateMealCost --------------------------------------------------
    #
    # Input:        none
    # Output:       float
    # Side Effect:  none
    # Description:  total cost of order items
    # -------------------------------------------------------------------------
    def calculateMealCost(self):
        total = 0
        for item in self.order:
            total += item.getPrice()
        return total

    # ---- __str__ ------------------------------------------------------------
    #
    # Input:        none
    # Output:       string
    # Side Effect:  none
    # Description:  allows object to be printable
    # -------------------------------------------------------------------------
    def __str__(self):
        name = "\tDiner " + self.name + " is currently "
        status = Diner.STATUSES[self.status] + "."
        return name + status
