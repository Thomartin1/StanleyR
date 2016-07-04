import csv
import datetime# We read the demand csv, take the times and order them to create frames.

# we return a list: [t0,t1,t2,t3,t4,t5,t6,t7,t8,t9, etc...]
# t0 is the first arrival and  txx the last departure.

def CreateTimeFrames(path):
    listinteresting=[]
    with open(path, 'rt') as reservations:
        lines= csv.reader(reservations, delimiter='\t')
        next(lines,None)
        for line in lines:
            # lin = line[0].split('\t')
            lin = line
            arrival = datetime.datetime.strptime(lin[1], '%d/%m/%Y %H:%M:%S')
            departure = datetime.datetime.strptime(lin[2], '%d/%m/%Y %H:%M:%S')
            listinteresting.append(arrival)
            listinteresting.append(departure)

    ## Sorting all times
    listinteresting = sorted(listinteresting)

    ## Delete duplicates.
    noduplicate = [listinteresting[0]]
    for i in range(1,len(listinteresting)):
        if (listinteresting[i]!=listinteresting[i-1]):
            noduplicate.append(listinteresting[i])
    reservations.close()
    return noduplicate
