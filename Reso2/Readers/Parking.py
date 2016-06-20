# we will assume the parking has a certain rectangular shape.
# if the shape is different there has to be matrix defining travel time.
# the parking is a dictionnaire {placeid: customer_id}

# 0 in input means you want to read a precise parking.
# 1 in input means you want to use the standart test parking.
def CreateParking(path, param):
    parking={}
    if param==0:
        with open(path, 'rt') as parkstruct:
            lines = csv.reader(parkstruct, delimiter='\t')
            next(lines, None)
            for line in lines:
                lin=line[0].split('\t')
                parking[lin[0]]="none"

    if param==1:
        for i in range(1,21):
            parking["0.%s.0"%i]="none"
            for row in range(1,6):
                for depth in range(1, row+1):
                    for column in range(1,40):
                        parking["%s.%s.%s"%(row, depth, column)]="none"
    parkstruct.close()
    return parking