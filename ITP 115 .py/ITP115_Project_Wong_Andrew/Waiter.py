# Andrew Wong, awong827
# ITP 115, Spring 2020
# Final Project
# Description:
# Waiter Class


from Diner import Diner
from Menu import Menu


# ---- Waiter -----------------------------------------------------------------
#
# -----------------------------------------------------------------------------
class Waiter(object):

    # ---- __init__ -----------------------------------------------------------
    #
    # Input:        Menu
    # Output:       none
    # Side Effect:  none
    # Description:  constructor for Waiter class
    # -------------------------------------------------------------------------
    def __init__(self, menu):
        self.diners = []
        self.menu = menu

    # ---- addDiner -----------------------------------------------------------
    #
    # Input:        Diner
    # Output:       none
    # Side Effect:  none
    # Description:  add Diner to list of diners
    # -------------------------------------------------------------------------
    def addDiner(self, diner):
        self.diners.append(diner)

    # ---- getNumDiners -------------------------------------------------------
    #
    # Input:        none
    # Output:       int
    # Side Effect:  none
    # Description:  gets number of diners
    # -------------------------------------------------------------------------
    def getNumDiners(self):
        return len(self.diners)

    # ---- printDinerStatuses -------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  print all diners
    # -------------------------------------------------------------------------
    def printDinerStatuses(self):
        for status in Diner.STATUSES:
            print("Diners who are " + status + ":")
            for diner in self.diners:
                if Diner.STATUSES[diner.status] == status:
                    print(diner)

    # ---- takeOrders ---------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  check for diners that are ordering
    # -------------------------------------------------------------------------
    def takeOrders(self):
        for diner in self.diners:
            if diner.status == 1:
                for item in Menu.MENU_ITEM_TYPES:
                    self.menu.printMenuItemsByType(item)
                    print(diner.name + ", please select a " + item + " menu item number.")
                    validOrder = False
                    while not validOrder:
                        order = input("> ")
                        if order.isdigit() and 0 <= int(order) < self.menu.getNumMenuItemsByType(item):
                            diner.addToOrder(self.menu.getMenuItem(item, int(order)))
                            validOrder = True
                print()
                print(diner.name + " ordered:")
                diner.printOrder()

    # ---- ringUpDiners -------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  loop through and check for paying diners
    # -------------------------------------------------------------------------
    def ringUpDiners(self):
        for diner in self.diners:
            if diner.status == 3:
                print("\n" + diner.name + ", your meal cost $" + str(diner.calculateMealCost()))

    # ---- removeDoneDiners ---------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  remove leaving diners
    # -------------------------------------------------------------------------
    def removeDoneDiners(self):
        for diner in self.diners:
            if diner.status == 4:
                print("\n" + diner.name + ", thank you for dining with us! Come again soon!")
        for i in range(len(self.diners) - 1, -1, -1):
            if self.diners[i].status == 4:
                self.diners.pop(i)

    # ---- advanceDiners ------------------------------------------------------
    #
    # Input:        none
    # Output:       none
    # Side Effect:  none
    # Description:  attend to diners at various stages
    # -------------------------------------------------------------------------
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.diners:
            diner.updateStatus()
