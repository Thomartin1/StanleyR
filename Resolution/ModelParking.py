import sys
import csv
import datetime


##On lit un csv qui permet de creer le dictionnaire du parking    id_place: id_client
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

## On lit un csv qui permet de creer la dictionnaire des clients du type   idclient:[date_entre, date_sortie]
def CreateCustomerList(PATH):
    customerlist={}
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            customernum= line[0].split('_')[1]
            customerlist[customernum]=[line[1],line[2]]
    return customerlist




class Parking:
    ## On crée une instance de parking, au timeframe donné, en suivant le model csv de parking. 
    ## La classe contient: -spots(le dico des places)
    ##                     -le timeframenum
    ##                     -la liste des clients qui sont dans les parking en ce moment. 
    def __init__(pathpark,timeframenum,param):
        self.spots= CreateParking(pathpark)
        parkinginitial = CreateParking(pathpark,param)
        self.timeframes= timeframenum
        self.customerlist = {}

    ## On ajoute un client dans le parking.
    ##  /!\ Cela n'ajoute pas le client dans le dictionnaire du parking, mais seulements 
    def AddCustomer(id,customerlisttot):
        self.customerlist[id]=[customerlisttot[1][id],customerlisttot[2][id]]
        
    # Calcul le dictionnaire des temps restants pour chaque place.  Et retourne none pour les places ou il y a pas de voiture.  
    def RemainingTime(timestamp):
        for place in self.spots.key():
            if (self.spot[place]=="none"):
                remainingtime[place]="none"
            else:
                remainingtime[place]= timedelta(customerlist[self.spot[place]][1], timestamp)