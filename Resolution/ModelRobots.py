import sys
import csv
import datetime
import ModelOrders

# This is were we crete the structure of a robot. 

class Robot:
    def __init__(numrobot, timestamp):
        self.num = numrobot
        self.timeavailable = timestamp
        self.occupied = False

    def giveorder(order):
        if self.occupied :
            self.listtasks.append(order)
        elif time.available > order.starttime:
            self.listtasks.append(order)
        else:
            self.occupied = True
            self.currenttask = order

    def taskcompleted():
        self.occupied=False
        if (self.listtasks.size()>0):
            self.occupied=True
            self.currenttask=self.listtasks[0]
            self.listtasks.pop[0]

