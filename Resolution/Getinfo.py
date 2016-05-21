import datetime


# On prend une date et on check si elle correspond à une entrée ou une sortie
#retourne True si c'est une entree, False si c'est une sortie. 
def CheckTypeAction(customers, stamp):
    for cust in customers.keys(): 
        if stamp == cust[0]:
            return True
        elif stamp == cust[1]:
            return False

## Retourne l'ID  du client concerné par le timestamp. 
def GetCustomerId(customers, stamp):
    for cust in customers.keys(): 
        if (stamp == cust[0] or stamp == cust[1]):
            return cust    