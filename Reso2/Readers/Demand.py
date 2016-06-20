import csv
import datetime
import sys

# I get all the reservations from a csv file. We assunme no one
# will arrive or leave late.
# I return a dictionnaire {custnum:[arrival,departure]}
def Get_customers(path):
    customerlist={}
    with open(path, 'rt') as reservations:
        lines = csv.reader(reservations, delimiter='\t')
        next(lines, None)
        for line in lines:
            lin = line[0].split('\t')
            customernum= lin[0].split('_')[1]
            arrival = datetime.datetime.strptime(lin[1], '%d/%m/%Y %H:%M:%S')
            departure = datetime.datetime.strptime(lin[2], '%d/%m/%Y %H:%M:%S')
            customerlist[customernum]=[arrival,departure]
    reservations.close()
    return customerlist
