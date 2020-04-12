# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 12-2


class Coffee(object):
    STATUSES = ["ordered", "completed"]

    def __init__(self, size, desc, customer):
        self.size = size
        self.desc = desc
        self.customer = customer
        self.statusIndex = 0

    def setCompleted(self):
        self.statusIndex = 1

    def __str__(self):
        return self.size + " " + self.desc + " for " + self.customer + " (" + Coffee.STATUSES[self.statusIndex] + ")"
