

def asignswapspot(parking):
    for place in parking.keys():

        row=int(place.split(".")[0])
        depth=int(place.split(".")[1])
        column=int(place.split(".")[2])

        asignedpspot=1000000000

        #on ne verifie que les places de swap
        if(row==0 and depth==0):
            #on verifie si la place de swap est libre
            if(parking[place]=="none"):
                # on regarde si la nouvelle place dispo est plus proche de l'entre que la precedente
                if(column <= asignedpspot):
                    #on modifie la valeur
                    asignedpspot=column
    #on renvoie l'id de a place qui va bien
    return("0.0.%s"%(column))