import Order
import datetime

def queue_in(demand,orderlist,beginspot,endspot,ordertime,customerid, typeaction,parking):
    ordre = Order.Task(beginspot,endspot,ordertime,customerid,typeaction,parking)
    # print(type(demand[customerid][0]))
    # print(type(demand[customerid][1]))
    orderlist.append(ordre)
