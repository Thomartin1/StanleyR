import ModelRobots as MR
import csv
import datetime


## We setup the data, customers and robots. 

##On fait un gros dico dasn lequel on met en clef l'id du client 
## et de l'autre cote  [date arrivee, date depart]
def Get_customers(path):
    customerlist={}
    with open(path, 'rt') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            lin = line[0].split('\t')
            customernum= lin[0].split('_')[1]
            customerlist[customernum]=[lin[1],lin[2]]
    reservations.close()
    return customerlist

## Les robots sont mis dans un dictionnaire 
def setuprobots(botnum, starttime):
    robots={}

    for i in range(0,botnum):
        sttime=str(starttime)
        robots[i]=MR.Robot(i,sttime)

    return(robots)
