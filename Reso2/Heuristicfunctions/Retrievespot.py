#Retrieve the current location of a customer in the parking
def Retrievelocation(parking,target):
    for i in parking.keys():
        if parking[i]==target:
            return i

#Retrieve the ID of a customer concerned by the action of a given timestamp
def GetCustomerId(customers, stamp):
    for cust in customers.keys():
        if (stamp == customers[cust][0] or stamp == customers[cust][1]):
            return cust
