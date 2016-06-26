import csv
import sys
import datetime
import os

import Order as O
import Models.Parking as Mp
import Models.Robot as Mr
import Models.TimeFraming as MT
import Readers.Demand as RD
import Readers.Parking as RP
import Readers.Robsetup as RR
import Readers.Setupcsv as RS
from Heuristicfunctions.Checkaction import CheckTypeAction
from Heuristicfunctions.Retrievespot import Retrievelocation , GetCustomerId
from Heuristicfunctions.Findspot import findspot
from Heuristicfunctions.Giveplace import give_place
from Heuristicfunctions.Queue_In import queue_in
from Heuristicfunctions.Affecttasks import affecttasks

def Globalloop(pathparking,pathdemand):

    customers=RD.Get_customers(pathdemand)
    stamps=MT.CreateTimeFrames(pathdemand)
    (parking,swapavailable)=RP.CreateParking(pathparking, 0,stamps[0])
    robots=RR.setuprob(1,stamps[0])

    RS.setupcsv()

    #print(customers)
    i=1
    for tf in stamps:
        print("action# %s"%i)
        i+=1
        orderlist=[]
        # print(parking)

        typeaction=CheckTypeAction(customers, tf)
        identity=GetCustomerId(customers, tf)

        if typeaction :
            #represent the customer looking and waiting for a spot
            (parkspot,nextime)=give_place(parking,swapavailable,orderlist,tf,identity,customers[identity][0],customers[identity][1])
            print(swapavailable[0])
            print(swapavailable[1])
            print(swapavailable[2])
            #write the corresponding row in the log
            # printaction(kwargs**) ## celle-ci me pose soucis......)
            print("voiture deposee en %s"%(parkspot))
            #find a fitting spot in the parking (back-end)
            targetspot=findspot(parking,customers)
            print("voiture emenee en %s"%(targetspot))
            #give the order to move the car
            queue_in(customers,orderlist,parkspot,targetspot,nextime,identity, "rangement",parking)

        # ##########print(orderlist)
        #if the next action is a car leaving the parking
        # if typeaction==False:
        #     currentspot=Retrievelocation(parking,target)
        #     #we find a free SwapSpot
        #     spot=findswapt(parking)
        #     # we set the objective time 3 misn before
        #     tftarget= tf-datetim.timedelta(second=3)
        #     #we move the blocking Cars
        #     extractcars(parking,)
        #     #we move the corresponding car
        #     queue_in(kwargs**)
        affecttasks(parking, robots, orderlist, customers,swapavailable)




pathparking="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/parkingtest.csv"
pathdemand="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/demandtest.csv"

Globalloop(pathparking, pathdemand)
