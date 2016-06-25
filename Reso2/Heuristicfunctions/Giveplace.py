import datetime

#for the moment we only take the first spot available, there is no waiting time. 
def give_place(parking,orderlist):
    for num in range(1,10000):
        location="0.%s.0"%(num)
        if parking[location]=='none':
            return (location)
    return("0.0.0")
