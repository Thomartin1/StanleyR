import ModelRobot.py as MR

def Get_customers(path):
    customerlist={}
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            customernum= line[0].split('_')[1]
            customerlist[customernum]=[line[1],line[2]]
    return customerlist


def setuprobots(botnum, starttime, pathcust):
    # il faut mettre en place le dictionnaire des robots
    # il faut mettre en place  la liste des clients.?????
    robots={}

    for i in range(0,botnum):
        robots[i]=MR.Robot(i,starttime)

    customers=Get_customers(pathcust)

    return(robots,customers)
