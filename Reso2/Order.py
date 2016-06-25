import datetime
import csv
import sys


# We consider that the parking has a rectangular structure and robots can move along
# sides of the row.
def ComputeDisplacementDuration(beginspot,endspot,movespeed=0.12,getspeed=0.5,rowmax=40):
# Noter que movespeed et get speed sont plutot des temps pour parcourir une certaine distance. Plus ils sont grand , moins grande est la vitesse
    #je parse pour obtenir le entiers sorrespondant aux colones/profondeurs/rangees des places concernees
    beginlocation=beginspot.split('.')
    endlocation=endspot.split('.')

    row1=int(beginlocation[0])
    depth1=int(beginlocation[1])
    column1=int(beginlocation[2])

    row2=int(endlocation[0])
    depth2=int(endlocation[1])
    column2=int(endlocation[2])

    #je prends en consideration le fait qu''une place ( debut ou fin) puisse etre un place de swap (id = 0.X.0)
    if(column1==0 & row1==0):
        time=abs(depth1-column2)*movespeed+row2*movespeed+depth2*getspeed
    elif(column2==0 & row2==0):
        time=abs(depth2-column1)*movespeed+row1*movespeed+depth1*getspeed
    else:
        #dans le cas des 2 places classiques, on a 2 chemins potentiellement optimaux, il faut les departager.
        time1 = (abs(column1-column2)*movespeed+(depth2+depth1)*getspeed+(row1+row2)*movespeed)
        time2 = (abs(column1-column2)*movespeed+(depth2+depth1)*getspeed+(2*rowmax-row1-row2)*movespeed)
        time=min(time1,time2)
        #Je ressort le temps de trajet du robot.
        time = datetime.timedelta(0,time*60)
    return time

## We have to stock durations in a huge matrix for wierd parking.
##HERE



#This is the structure of an order.
#We use it to compute
class Task:
    def __init__(self,beginspot,endspot,ordertime,customerid,typeaction,parking):

        # order parameters are set
        self.begin=beginspot
        self.end=endspot
        self.startfrom= ordertime
        # self.duration = ComputeDisplacementDuration(self.begin,self.end)
        self.duration = datetime.timedelta(0,180)
        self.identity=customerid
        self.type=typeaction

        # the target spot is reserved.
        parking[self.end]=self.identity

    def update(self,start):
        self.effectivestart = start
        self.effectiveend = start + self.duration
        self.delay=self.effectivestart-self.startfrom

    def printincsv(self,robnum,cust_arrival,cust_departure,Nbrobonduty):
        # log = open('activitylog.csv','a')
        print()
        print()
        print()
        print()
        print()
        print(str(self.startfrom))
        print(str(self.type))
        print(str(robnum))
        print(str(self.identity))
        print(str(cust_arrival))
        print(str(self.effectivestart))
        print(str(self.effectiveend))
        print(str(cust_departure))
        print(str(self.delay))
        print(str(self.begin))
        print(str(self.end))
        print()
        print()
        print()
        print()
        print()
        # inforow="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(self.startfrom,self.type,robnum,self.identity,cust_arrival,self.effectivestart,self.effectiveend,cust_departure,self.delay,"nbdeposit","Nbstorage","Nbrobonduty",self.begin,self.end)
        # log.write(inforow)
        # log.close()
