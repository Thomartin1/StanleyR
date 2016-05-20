import Reader.py as r
from SetUp.py import setuprobots



def GlobalLoop():

    [stamps,typeaction,parking]=r.datareader(pathparking,pathtime,pathdemand)
    [robots,customers]=setuprobots(4,stamps[0])


    for tf in stamps:
        typeaction = CheckTypeAction(customers, stamps)
        asignedspot=asignswapspot(parking)

        if(typeaction):
            place=Findplace(parking)
            neworder=Task(asignedspot,place,tf,target)
            giveorder(robots,neworder)

        if(typeaction ==False):
            asignedspot=asignswapspot(parking)
            extractcar()



    #prevision pour la suite. 
    #boucler sur les utilisateurs dans le parking.
    # boucle sur la profondeur possible:

            #si il y a un depart A LA PROCHAINE TF. 

            #si il y a un départ dans 2 TF ( et que je dois bouger la voiture) et que la voiture est a la profondeur 

            #si il y a un depart dans 3 TF et que la voiture est a la profondeur 2