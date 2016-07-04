import datetime

def findspot(parking,customers):
    for depth in range(1,6):
        for row in range(1,6):
            for column in range(0,40):
                location="%s.%s.%s"%(row, 6-depth, column)
                if location in parking.keys():
                    if parking[location]=='none':
                        print("youpi")
                        return location

    # nswap=3
    # for i in range(0,nswap):
    #     location="0.%s.0"%(i+1)
    #
    # return location




# def findspot(parking, stamps, customers,tf):
# #on va explorer le parking en prenant la place la plus proche.
# #ne connaissantpas trop le parking, om prend comme place reference "0.0.0"
#     index=stamps.index(tf)
#     concernedcustomers=[]
#     for i in range(0,3):
#         concernedcustomers.append(GI.GetCustomerId(customers,stamps[min(index+i+1,len(stamps)-1)]))
#     found = False
#     for column in range(1, 10000):
#         for row in range(1,10000):
#             for depth in range(1,10000):
#                 location="%s.%s.%s"%(row, depth, column)
#                 nextloc="%s.%s.%s"%(row, depth+1, column)
#
#
#                 if(location in parking.keys() and nextloc in parking.keys()):
#                     if((parking[location]=="none") and (parking[nextloc] not in concernedcustomers)):
#                         selected = location
#                         found = True
#
#
#                 elif(location in parking.keys()):
#                     if(parking[location]=="none"):
#                         selected = location
#                         found = True
#
#
#
#             if(found):
#                 break
#         if(found):
#             break
#     return selected

# En l'etat la fonction retourne la place la plus proche du point 0.0.0
# Elle ne se préocupe pas de ce qui va se passer ensuite, de si elle fout la merde etc....
# Du coup elle est loin d'être optimale.
