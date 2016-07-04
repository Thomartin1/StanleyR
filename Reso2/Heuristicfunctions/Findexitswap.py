import datetime
import Order

 #for the moment we only take the first spot available, there is no waiting time.
def findexitswap(parking,swapavailable,tf):
    # for num in range(1,100):
    #      location="0.%s.0"%(num)
    #      if(location in parking.keys()):
    #          if (parking[location]=='none' and swapavailable[num-1]<=tf) :
    #              temp=swapavailable[num-1]
    #              return (location,temp)

    nextime= min(swapavailable)
    # print("Prochaine place dispo à %s"%(nextime))
    for num in range(1,len(swapavailable)+1):
        if(nextime==swapavailable[num-1]):
            location="0.%s.0"%(num)
            return(location,nextime)
