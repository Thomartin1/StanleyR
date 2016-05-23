import ModelRobots
import SpotFinder as SF
import ModelOrders as MO
import GiveOrder as GO
import Getinfo as GI



def extractcar(customers,assignedspot,parking,robots,place,tf,stamps,target):
    #Je donne l'ordre au robot de sortir la voiture de telle place vers telle place. 

        #Boucler sur la profondeur
        # Si jamais il y a une voiture devant, il faut que je la deplace ( et la replace). 
        #(penser aux limitatons du nombre de robots ainsi que les temps d'attente)

    # Je commence par regarder les voitures devant et les replace si c'est le cas.
    if(place is not None): 
        row= int(place.split('.')[0])
        targetdepth=int(place.split('.')[1])
        column=int(place.split('.')[2])
        exist = True
        depth=1
        checkposition="%s.1.%s"%(row, column)
        print("tagetplace is",place)
        concernedspot=[]
        while (depth<targetdepth):
            if(parking[checkposition]=="none"):
                pass
            else:
                concernedspot.append(checkposition)
                newlocation=SF.Findplace(parking)
                neworder=MO.Task(place,newlocation,tf,parking[checkposition])
                GO.giveorder(robots,neworder)
                parking[newlocation]= parking[checkposition]
            depth +=1
            checkposition="%s.%s.%s"%(row, depth, column)
            print("checkposition is",checkposition)
            if(checkposition in parking.keys()):
                exist = True
            else:
                exist = False
        for i in concernedspot:
            parking[i]="none"

        #ensuite je m'occupe de la voiture de depart. 
        neworder=MO.Task(place,assignedspot,tf,parking[place])
        GO.giveorder(robots,neworder)



    nextconcernedplace=[]
    index = stamps.index(tf)
    for i in range (1,3):
        index +=1
        if(index <=len(stamps)-1):
            nexttf=stamps[index]
            #on va maintenant voir si il s'agit d'une depose ou d'une recuperation. 
            # Si jamais il s'agit d'une recup, je lui dit de bouger le voiture genant potentiellement 
            #la voiture concernee. 
            typeaction = GI.CheckTypeAction(customers, nexttf)
            if(typeaction==False):
                #ca veut dire qu'on a affaire à une recupération de vehicule. 
                # dans ce cas je fais pareil que precedement mais sans sortir la voiture target. 
                nexttarget = GI.GetCustomerId(customers,nexttf)
                placeofnext=GI.Retrievelocation(parking,nexttarget)
                nextplace=SF.Findplace(parking)
                nextorder=MO.Task(placeofnext,nextplace,tf,nexttarget)
                GO.giveorder(robots,nextorder)
                parking[nextplace]=nexttarget
                nextconcernedplace.append(placeofnext)

    for i in nextconcernedplace:
        parking[i]="none"