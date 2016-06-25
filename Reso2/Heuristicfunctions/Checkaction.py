import datetime

#we check wether the action concerned is an arrival or a departure.

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
