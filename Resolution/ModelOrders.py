import datetime

def ComputeDisplacementDuration(beginspot,endspot, movespeed= 10):
    beginlocation=beginspot.split('.')
    endlocaiton=endspot.split('.')
    time = ........+..........+........
    
# This is were we crete the structure of an order. 
class Task:
    def __init__(beginspot,endspot,startdate,customerid):
        self.begin=beginspot
        self.end=endspot
        self.startfrom= startdate
        self.duration = ComputeDuration(self.begin,self.end)
        self.endfrom = self.startfrom + self.duration
        self.identity=customerid 
