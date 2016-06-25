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
        self.num=numbot
        self.nextavailable = timestamp

    def setorder(self,parking,foo_task):
        self.orderexec=foo_task
        effectivestart=max(self.nextavailable, self.orderexec.startfrom)
        self.orderexec.update(effectivestart)

    def marktask(self,parking,cust_arrival,cust_departure,Nbrobonduty):
        parking[self.orderexec.begin]='none'
        self.orderexec.printincsv(self.num,cust_arrival,cust_departure,Nbrobonduty)
