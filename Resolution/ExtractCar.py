import ModelRobots
import SpotFinder as SF
import ModelOrders as MO
import GiveOrder as GO



def extractcar(assignedspot,parking,robots,place,tf,target):
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
        depth=0
        checkposition=place
        while (exist and depth<targetdepth):
            if(parking[checkposition]=="none"):
                pass
            else:
                newlocation=SF.Findplace(parking)
                neworder=MO.Task(place,newlocation,tf,parking[checkposition])
                GO.giveorder(robots,neworder)
            depth +=1
            checkposition="%s.%s.%s"%(row, depth, column)
            if(checkposition in parking.keys()):
                exist = True
            else:
                exist = False

            #ensuite je m'occupe de la voiture de depart. 
            neworder=MO.Task(place,assignedspot,tf,parking[place])
            GO.giveorder(robots,neworder)



##IL reste à bouger les autres voitures. 