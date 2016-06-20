import csv
import sys
import datetime
import os

import Models.Order as Mo
import Models.Parking as Mp
import Models.Robot as Mr
import Timeframing as MT
import Readers.Demand as RD
import Readers.Parking as RP

def Globalloop(pathparking,pathdemand):
    parking=RP.CreateParking(pathparking, 0)
    customers=RD.Get_customers(pathdemand)
    print(parking)
    print(customers)


pathparking="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/parkingtest.csv"
pathdemand="/Users/Thomartin/Documents/Ponts_2A/Stanley_Robotics/4160 - ENPC PROJET2A/data_projet_2A/demandtest.csv"
GlobalLoop(pathparking,pathdemand)

Globalloop(pathparking, pathdemand)
