import Order
import datetime
import Models.Robot
from Heuristicfunctions.Queue_In import queue_in
from Heuristicfunctions.Findspot import findspot


def movecars(currentspot,carinfront,orderlist,parking,demand,initialtime):

    row=int(currentspot.split('.')[0])
    depth=int(currentspot.split('.')[1])
    column=int(currentspot.split('.')[2])

    # print("")
    # print("")
    # print(currentspot)
    # print(carinfront)
    # print("")
    # print(depth)
    # print("")

    if(len(carinfront)>0):
        for i in range(1,depth):
            spot="%s.%s.%s"%(row,i,column)
            # print(spot)
            newspot=findspot(parking,demand)
            queue_in(demand,orderlist,spot,newspot,initialtime,carinfront[spot],"relocation",parking)
