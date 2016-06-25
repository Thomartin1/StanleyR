import Models.Robot as MR
import Order

def setuprob(robtot,time):
    robots=[]
    for i in range(0,robtot):
        rob=MR.Robot(i,time)
        robots.append(rob)
    return robots
