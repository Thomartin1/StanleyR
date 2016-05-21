import ModelRobots



def extractcar(assignedspot,parking,robots,place,tf,target):
    #Je donne l'ordre au robot de sortir la voiture de telle place vers telle place. 

        #Boucler sur la profondeur
        # Si jamais il y a une voiture devant, il faut que je la deplace ( et la replace). 
        #(penser aux limitatons du nombre de robots ainsi que les temps d'attente)

    # Je commence par regarder les voitures devant et les replace si c'est le cas. 
    row=place.split('/')[0]
    targetdepth=place.split('/')[1]
    column=place.split('/')[2]
    exist = True
    depth=0
    checkposition=place
    while (exist and depth<targetdepth):
        if(parking[checkposition]=="none"):
            pass
        else:
            newlocation=Findplace(parking)
            neworder=Task(place,newlocation,tf,parking[checkposition])
            giveorder(robots,neworder)
        depth +=1
        checkposition="%s.%s.%s"%(row, depth, column)
        if(checkposition in parking.keys()):
            exist = True
        else:
            exist = False

        #ensuite je m'occupe de la voiture de depart. 
        neworder=Task(place,assignedspot,tf,parking[place])
        giveorder(robots,neworder)

