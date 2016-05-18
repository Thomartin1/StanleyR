import datetime

import ModelParking

## On cree les timeframes qui vont servir de checkpoint dans le temps. 
def CreateTimeFrames(PATH):
    listinteresting=[]
    with open(path, 'rb') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines,None)
        for line in lines:
            listinteresting.append(line[1])
            listinteresting.append(line[2])

    ## On sort toutes ces dates.
    listinteresting = sorted(listinteresting)

    ## Et on suprime les doublons.
    noduplicate = [listinteresting[0]]
    for i in range(1,len(listinteresting)):
        if (listinteresting[i]!=listinteresting[i-1]):
            noduplicate.append(listinteresting[i])

    return noduplicate