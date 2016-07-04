import datetime

def GetCustomerId(customers, stamp):
    for cust in customers.keys():
        if (stamp == customers[cust][0] or stamp == customers[cust][1]):
            return cust

#Retrieve the current location of a customer in the parking
def Retrievelocation(identity,parking,tf):
    print("########")
    print(identity)
    print("########")
    for i in parking.keys():
        if parking[i]==identity:
            position=i

    row=int(position.split('.')[0])
    depth=int(position.split('.')[1])
    column=int(position.split('.')[2])

    blockingcars={}
    if(depth>1):
        for i in range(1,depth):
            spot="%s.%s.%s"%(row,i,column)
            if(parking[spot]!='none'):
                blockingcars[spot]=parking[spot]

    return(position,blockingcars)
