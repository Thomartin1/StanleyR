from random import randint
import ModelRobots as MR


def giveorder(robots,order):
    assigned=False
    #je cherche un robot etant libre
    for i in range robots.keys():
        #le premier que je trouve, je lui donne l'ordre
        if robots[i].occupied== False:
            robots[i].setorder(order)
            assigned=True
            break
    #sinon, je donne l'ordre à un robot au pif,
    #qui va le mettre dans sa "to do" list
    if !assigned:
        i = randint(0,len(robots.keys()))
        robots[i].giveorder(order)
