import ModelRobot.py as MR

def setuprobots(botnum, starttime):
    # il faut mettre en place le dictionnaire des robots
    # il faut mettre en place  la liste des clients.?????
    robots={}

    for i in range(0,botnum):
        robots[i]=MR.Robot(i,starttime)

    return(robots)
