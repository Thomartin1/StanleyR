import csv
import sys
import datetime

def CreateTimeFrames(PATH):
    listinteresting=[]
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines,None)
        for line in lines:
            listinteresting.append(line[1])
            listinteresting.append(line[2])

    ## On sort toutes ces dates.
    listinteresting = sorted(listinteresting)

    ## Et on suprime les doublons.
    noduplicate = [listinteresting[0]]
    for i in range(1,len(listinteresting)):
        if (listinteresting[i]!=listinteresting[i-1]):
            noduplicate.append(listinteresting[i])

    return noduplicate

#On cree un dictionnaire avec comme clef la position de la place. 
# plus tard, on mettra l'id du client à cette place en face. 
def CreateParking(PATH, param):
    parking={}
    if param==0:
        with open(PATH, 'rb') as file:
            lines = csv.reader(file, delimiter=' ')
            next(lines, None)
            for line in lines:
                parking[line[0]]="none"

    if param==1:
        for i in range(1,21):
            parking["0.%s.0"%i]="none"
            for row in range(1,6):
                for depth in range(1, row+1):
                    for column in range(1,40):
                        parking["%s.%s.%s"%(row, depth, column)]="none"

    return parking


def datareader(pathparking,pathtime,pathdemand):
    tf=CreateTimeFrames(pathdemand)
    parking = CreateParking(pathparking,0)   #changer en 0 pour utiliser le csv

    return [tf,parking]