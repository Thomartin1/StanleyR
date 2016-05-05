import sys
import csv
# Here we create the right parking model based on a csv file.

def CreateTestParking():
    parking={}
    for i in range(1,21):
        parking["0.%s.0"%i]=NULL
    for row in range(1,6):
        for depth in range(1, row+1):
            for column in range(1,40):
                parking["%s.%s.%s"%(row, depth, column)]=NULL
    return parking

def CreateParking(PATH):
    parking={}
    with open(PATH, 'rb') as file:
        lines = csv.reader(file, delimiter=' ')
        next(lines, None)
        for line in lines:
            parking[line[0]]=NULL
    return parking

def CreateCustomerList(PATH):
    customerlist={}
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            customernum= line[0].split('_')[1]
            customerlist[customernum]=[line[1],line[2]]
    return customerlist

def CreateTimeFrames(PATH):
    timeframelist={}
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        i = 1
        for line in lines:
            timeframenumber = i
            timeframelist[timeframelist]=[line[1],line[2]]
            i++
    return timeframelist


class Parking:
    def __init__(pathpark,timeframenum):
        self.spots= CreateParking(pathpark)
        parkinginitial = CreateParking(pathpark)
        self.timeframes= timeframenum
        self.customerlist = {}

    #pas focntionnelle
    def AddCustomer(id,customerlist):
        self.customerlist[id]=[customerlist[1][id],customerlist[2][id]]
        
    #pas fonctionnelle
    def RemainingTime(timestamp):


        
