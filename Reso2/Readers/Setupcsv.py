import os
import csv

# Here we create a new csv file with default name activitylog.csv
# We delete the file first if one already exists

def setupcsv(name="activitylog.csv"):
    if(os.path.isdir('/Users/Thomartin/StanleyR/Reso2/%s'%(name))):
        os.remove(name)
    with open(name,'wt')as log:
        wr = csv.writer(log, quoting=csv.QUOTE_ALL)
        wr.writerow(['Timestamp','Type','BotID','VehiculeID','ArrivedAt','StartAt','FinisheAt','LeaveAt','TimeBLK','NBdeposit','NbStorage','Nb_Rob_on_Duty','Origin','Destination'])
        log.close()
