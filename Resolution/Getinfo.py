import datetime


# On prend une date et on check si elle correspond à une entrée ou une sortie
#retourne True si c'est une entree, False si c'est une sortie. 
def CheckTypeAction(customers, stamp):
    # print("CheckTypeAction")
    for cust in customers.keys():
        # print("---------------") 
        # print(stamp)
        # print(customers[cust][0])
        # print(customers[cust][0])
        if stamp == customers[cust][0]:
            return True
        elif stamp == customers[cust][1]:
            return False

## Retourne l'ID  du client concerné par le timestamp. 
def GetCustomerId(customers, stamp):
    for cust in customers.keys(): 
        if (stamp == customers[cust][0] or stamp == customers[cust][1]):
            return cust    

def Retrievelocation(parking,target):
    for i in parking.keys():
        if parking[i]==target:
            return i
