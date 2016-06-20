import sys
import csv
import datetime
import ModelOrders

# This is were we crete the structure of a robot. 
# les caracteristiques d;un robot sont:
# - num                l'id du robot
# - occupied           si il est occupe ou non 
# - effectivestart     quand il commence vraiment l'ordre qui lui est affecte
# - timeavailable       quadn il fini vraiment l'ordre affecte// quand il sera dispo
# - currenttask        l'ordre qu'il est en train d'effectuer
# - listtasks           la liste des prochains ordres
# - currentspot        permet de calsuler le temps de trajet pour aller affectuer une nouvelle tache. 
# - delay              le retard avec lequel le robot a pris la tache
# - waitingtime        le temps que le robot a attendu avant de se mettre a la tache suivante. 

# attention, dans les ordres on ne compte que ceux qui impliquent un deplacement de voiture. 
# currentspot prend l'id de la place de debut de l'ordre des que l'ordre est affecte au robot. Il prend l'id de la place d'arrivee des que l'ordre est fini. 

class Robot:
    def __init__(self,numrobot, timestamp):
        self.num = numrobot
        self.timeavailable = timestamp
        self.occupied = False
        self.currentspot = "0.0.0"
        self.listtasks = []

    def setorder(self,order):
        # print("setorder")
        if self.occupied :
            self.listtasks.append(order)
            print(self.num,"  ",self.currentspot,"  ",self.currenttask.end, "       ",self.effectivestart,"  ",self.timeavailable,"  ",self.delay,"TOOOODOOOOO")
        else:
            self.occupied = True
            # transit=ModelOrders.ComputeDisplacementDuration(self.currentspot,order.begin)
            self.currenttask = order
            self.currentspot = order.begin
            # print(type(self.timeavailable))
            # print(self.timeavailable)
            # print(type(order.startfrom))
            # print(order.startfrom)
            self.effectivestart = max(self.timeavailable,order.startfrom)
            self.delay = self.effectivestart- order.startfrom
            self.waitingtime = order.startfrom - self.timeavailable
            self.timeavailable = self.effectivestart+datetime.timedelta(minutes=ModelOrders.ComputeDisplacementDuration(self.currentspot,order.end))
            print(self.num,"  ",self.currentspot,"  ",self.currenttask.end, "       ",self.effectivestart,"  ",self.timeavailable,"  ",self.delay,"Sur le champ")


    def taskcompleted(self):
        if(self.occupied):
            # je note la tache actuelle comme finie et passe a la prchaine si il y en a une dans la liste. 
            self.occupied=False
            self.currentspot = self.currenttask.end
            if (len(self.listtasks)>0):
                self.setorder(self.listtasks[0])
                self.listtasks.pop(0)

