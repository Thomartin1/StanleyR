import csv
import sys
import math
import datetime as dt


# customerlist est un ditionnaire {customer: [date arrivee, date sortie]}


def Get_customers(path):
    customerlist={}
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            customernum= line[0].split('_')[1]
            customerlist[customernum]=[line[1],line[2]]
    return customerlist

# Le temps est en milisecondes ici. Comme dans le csv qu'ils nous ont filé. 
def Time_remaining(customernum, customerlist, moment):
    dmYFMT = '%d/%m/%Y %H:%M:%S'
    timeleft =1000*(dt.datetime.strptime(customerlist[str(customernum)][1], dmYFMT) - dt.datetime.strptime(moment, dmYFMT))
    if(timeleft.total_seconds() <=0):
        timeleft=0
    return timeleft

# la je cree un parking selon des specification harcodées (nombre de lignes colone etc...)
def Create_test_parking():
    Parking={}
    for i in range(1,21):
        Parking["0.%s.0"%i]=NULL
    for row in range(1,6):
        for depth in range(1, row+1):
            for column in range(1,40):
                Parking["%s.%s.%s"%(row, depth, column)]=NULL
    return Parking
# Parking est un dictionaire qui resemble à ca: [placenum: customernum, etc...]
# Du coup avec Parking et Customerlist on a tout ce qu'il faut. 
def Create_parking_fromCSV(PATHfile):
    Parking = {}
    with open(PATHfile, 'rb') as model:
        lines = csv.reader(model, delimiter ='\t')
        next(lines, None)
        for line in lines:
            Parking[line[2]]=NULL  # modifier avec la bonne colone qui correspond.  

# Scoring du rangement du parking. 
#
# def ScoreParking_Simple(moment):
#     customerlist=Get_customers('data_full_occupation.csv')
#     with open('test_10_robot_20_depot_demo_full.csv', 'rb') as log:
#         lines = csv.reader(log, delimiter='\t')
#         next(lines, None)
#         for line in lines:
#             #mettre l'actualisation du dico des places, et 
        