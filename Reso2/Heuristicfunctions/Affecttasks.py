import csv
import Models.Robot as Mr
import datetime


def affecttasks(parking,robots, orderlist,demand):
    for i in range(0, len(orderlist)):
        #i chose the first available robot
        listtimes=[]

        for ind in range(0,len(robots)):
            listtimes.append(robots[ind].nextavailable)
        nextdispo=min(listtimes)

        for ind in range(0,len(robots)):
            if robots[ind].nextavailable==nextdispo:
                index = ind

        print("robot# %s" %(index))
        # the order is given to this robot and updated
        robots[index].setorder(parking, orderlist[i])
        print(robots[index].orderexec)
        # the robot is unavailable until the task is complete
        robots[index].nextavailable=robots[index].orderexec.effectiveend
        print("########################",robots[index].orderexec.effectiveend)
        # the task is considered as complete and is writen down in the csv.
        robots[index].marktask(parking,demand[robots[index].orderexec.identity][0],demand[robots[index].orderexec.identity][1],1)
