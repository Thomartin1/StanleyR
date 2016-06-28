import csv
import Models.Robot as Mr
import datetime


def affecttasks(parking,robots, orderlist,demand,swapavailable):
    for i in range(0, len(orderlist)):
        #I chose the first available robot
        listtimes=[]
        for ind in range(0,len(robots)):
            listtimes.append(robots[ind].nextavailable)
        nextdispo=min(listtimes)

        #the swap spot availability is updated with time the robot will take care of the car placed there.
        if(orderlist[i].type=="rangement"):
            # print("ajust swapavailable")
            # print(nextdispo)
            num=int(orderlist[i].begin.split('.')[1])
            swapavailable[num-1]=max(nextdispo,swapavailable[num-1])

        # we get the od of the robot that'll take care of the car
        for ind in range(0,len(robots)):
            if robots[ind].nextavailable==nextdispo:
                index = ind


        # print("robot# %s" %(index))
        # the order is given to this robot and updated
        robots[index].setorder(parking, orderlist[i])
        # print(robots[index].orderexec)
        # the robot is unavailable until the task is complete
        robots[index].nextavailable=robots[index].orderexec.effectiveend

        if(orderlist[i].type=="exit"):
            num=int(orderlist[i].end.split('.')[1])
            swapavailable[num-1]=max(demand[robots[index].orderexec.identity][1],robots[index].orderexec.effectiveend)
        # print("########################",robots[index].orderexec.effectiveend)
        # the task is considered as complete and is writen down in the csv.
        robots[index].marktask(parking,demand[robots[index].orderexec.identity][0],demand[robots[index].orderexec.identity][1],1)
        print("")
        print("")
        print(orderlist[i].type)
        print(orderlist[i].identity)
        print(orderlist[i].begin)
        print(orderlist[i].end)
        print(orderlist[i].effectiveend)
        print(orderlist[i].delay)
        print("")
        print("")
