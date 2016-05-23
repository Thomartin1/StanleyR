

def Findplace(parking):
#on va explorer le parking en prenant la place la plus proche. 
#ne connaissantpas trop le parking, om prend comme place reference "0.0.0"
    found = False
    for column in range(1, 10000):
        for row in range(1,10000):
            for depth in range(1,10000):
                location="%s.%s.%s"%(row, depth, column)
                if(location in parking.keys()):
                    if(parking[location]=="none"):
                        selected = location
                        found = True
                    if(found):
                        break
            if(found):
                break
        if(found):
            break
    return selected

# En l'etat la fonction retourne la place la plus proche du point 0.0.0 
# Elle ne se préocupe pas de ce qui va se passer ensuite, de si elle fout la merde etc....
# Du coup elle est loin d'être optimale. 