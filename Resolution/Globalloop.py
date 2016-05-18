from Reader.py import datareader
from SetUp.py import setuprobots



def GlobalLoop():

    [stamps,parking]=datareader(pathparking,pathtime,pathdemand)

    robots=setuprobots(4,stamps[0])

    for tf in timeframes:
        #si il y a une arrivée.
        asignedspot=asignswapspot(parking)
        if(typeevent== arrival):
            #je place la voiture
            findplace()
            giveorder()


        #si il y a un depart:
        if(typeevent == departure):
            asignedspot=asignswapspot(parking)
            extractcar()



    #prevision pour la suite. 
    #boucler sur les utilisateurs dans le parking.
    # boucle sur la profondeur possible:

            #si il y a un depart A LA PROCHAINE TF. 

            #si il y a un départ dans 2 TF ( et que je dois bouger la voiture) et que la voiture est a la profondeur 

            #si il y a un depart dans 3 TF et que la voiture est a la profondeur 2