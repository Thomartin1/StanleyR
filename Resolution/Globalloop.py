import ModelParking
import Creationgraph
import ModelOrders as MO
import ModelRobots

import Reader as R
import SetUp as SU
import Getinfo as GI
import SpotFinder as SF
import SwapSpot as SS
import GiveOrder as GO
import ExtractCar as EC



def GlobalLoop(pathparking,pathdemand):

    [stamps,parking]=R.datareader(pathparking,pathdemand)
    robots=SU.setuprobots(1,stamps[0])
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
            place=SF.Findplace(parking)
            neworder=MO.Task(asignedspot,place,tf,target)
            GO.giveorder(robots,neworder)
            parking[asignedspot]="none"
            parking[place]=target

        elif(typeaction == False):
            print("retrieve")
            place=GI.Retrievelocation(parking,target)
            print(place)
            EC.extractcar(asignedspot,parking,robots,place,tf,target)
            parking[asignedspot]= target
            parking[place]="none"


    #prevision pour la suite. 
    #boucler sur les utilisateurs dans le parking.
    # boucle sur la profondeur possible:

            #si il y a un depart A LA PROCHAINE TF. 

            #si il y a un départ dans 2 TF ( et que je dois bouger la voiture) et que la voiture est a la profondeur 

            #si il y a un depart dans 3 TF et que la voiture est a la profondeur 2




pathparking="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/model_parking.csv"
pathdemand="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/demandtest.csv"
GlobalLoop(pathparking,pathdemand)
