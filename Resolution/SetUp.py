import ModelRobots as MR


## We setup the data, customers and robots. 

##On fait un gros dico dasn lequel on met en clef l'id du client 
## et de l'autre cote  [date arrivee, date depart]
def Get_customers(path):
    customerlist={}
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            customernum= line[0].split('_')[1]
            customerlist[customernum]=[line[1],line[2]]
    return customerlist

## Les robots sont mis dans un dictionnaire 
def setuprobots(botnum, starttime):
    robots={}

    for i in range(0,botnum):
        robots[i]=MR.Robot(i,starttime)

    return(robots,customers)
