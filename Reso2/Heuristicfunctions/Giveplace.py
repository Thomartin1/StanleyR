import datetime
import Order

def give_place(parking,swapavailable, orderlist,tf,customerid,cust_arrival,cust_departure):
    for num in range(1,100):
        location="0.%s.0"%(num)
        if(location in parking.keys()):
            if (parking[location]=='none' and swapavailable[num-1]<=tf) :
                swapavailable[num-1]=tf
                placement=Order.Task("0.0.0",location,tf,customerid,"ARRIVEE",parking)
                placement.update(tf)
                placement.printincsv("X",cust_arrival,cust_departure,"Nbrobonduty")

                return (location,tf)

    nextime= min(swapavailable)
    for num in range(1,len(swapavailable)+1):
        if(nextime==swapavailable[num-1]):
            location="0.%s.0"%(num)
            placement=Order.Task("0.0.0",location,tf,customerid,"ARRIVEE",parking)
            placement.update(nextime)
            placement.printincsv("X",cust_arrival,cust_departure,"Nbrobonduty")
            return(location,nextime)
