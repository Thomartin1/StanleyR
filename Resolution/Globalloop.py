import ModelParking
import Creationgraph
import ModelOrders as MO
import ModelRobots
import datetime

import Reader as R
import SetUp as SU
import Getinfo as GI
import SpotFinder as SF
import SwapSpot as SS
import GiveOrder as GO
import ExtractCar as EC



def GlobalLoop(pathparking,pathdemand):

    [stamps,parking]=R.datareader(pathparking,pathdemand)
    robots=SU.setuprobots(2,stamps[0])
    customers=SU.Get_customers(pathdemand)

    # print(stamps)
    # print(customers)

    for tf in stamps:
        # print("tf")
        typeaction = GI.CheckTypeAction(customers, tf)
        asignedspot=SS.asignswapspot(parking)
        target = GI.GetCustomerId(customers,tf)

        # print(typeaction)
        if(typeaction):
            parking[asignedspot]=target
            print("depose")
            place=SF.Findplace(parking, stamps, customers,tf)
            neworder=MO.Task(asignedspot,place,tf,target)
            GO.giveorder(robots,neworder)
            parking[asignedspot]="none"
            parking[place]=target

        elif(typeaction == False):
            print("retrieve")
            place=GI.Retrievelocation(parking,target)
            print(place)
            print("asingnedSPOT IS",asignedspot)
            print("PLACEIS",place)
            EC.extractcar(customers,asignedspot,parking,robots,place,tf,stamps,target)
            parking[asignedspot]= target
            parking[place]="none"




pathparking="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/parkingtest.csv"
pathdemand="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/demandtest.csv"
GlobalLoop(pathparking,pathdemand)
