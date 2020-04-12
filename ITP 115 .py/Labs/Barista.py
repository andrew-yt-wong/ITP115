# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 12-2


from Coffee import Coffee

class Barista(object):
    MAX_ORDER = 5

    def __init__(self, name):
        self.name = name
        self.orders = list()

    def takeOrder(self):
        desc = input("What drink do you want? ")
        size = input("What size would you like? ")
        customer = input("What is your name? ")
        order = Coffee(size, desc, customer)
        self.orders.append(order)
        print(order)

    def isAcceptingOrders(self):
        if len(self.orders) < Barista.MAX_ORDER:
            return True
        return False

    def makeDrinks(self):
        print("Here are the completed orders:")
        for order in self.orders:
            order.setCompleted()
            print("\t", end="")
            print(order)

    def __str__(self):
        return "My name is " + self.name
