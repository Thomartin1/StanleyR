import datetime

def ComputeDisplacementDuration(beginspot,endspot,movespeed=0.12,getspeed=0.5,rowmax=40): 
#Noter que movespeed et get speed sont plutot des temps pour parcourir une certaine distance. Plus ils sont grand , moins grande est la vitesse
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
        print(time) 
    return time
    
# This is were we crete the structure of an order. 
class Task:
    def __init__(self,beginspot,endspot,startdate,customerid):
        self.begin=beginspot
        self.end=endspot
        self.startfrom= startdate
        self.duration = ComputeDisplacementDuration(self.begin,self.end)
        self.endfrom = self.startfrom+datetime.timedelta(minutes=self.duration)
        self.identity=customerid 
