# Structure of a robot:
import sys
import csv
import datetime
import Order

# A robot is caracterized by:
# - num: its number
# - task: the order he has been given
# - nextavailable: the moment it'll be available

class Robot:
    def __init__(self,numbot,timestamp):
        self.num=numrobot
        self.nextavailable = timestamp

    def setorder(self, foo_task):
        orderexec=foo_task
        orderexec.update(start)

    def marktask(self,cust_arrival,cust_departure,Nbrobonduty):
        printincsv(self.num,cust_arrival,cust_departure,Nbrobonduty)
