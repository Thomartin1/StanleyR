import csv
import sys
import math
import datetime as dt


def mean(wait_list):
    wait_time = sum(wait_list)
    average = wait_time / len(wait_list)
    return average

def sqrtvariance (wait_list):
    sumsquare = 0
    for i in wait_list:
        sumsquare = sumsquare+ i*i
    square_esp = sumsquare/len(wait_list)

    var = square_esp - mean(wait_list)*mean(wait_list)

    return(math.sqrt(var))


def Time_remaining(moment1, moment2):
    dmYFMT = '%d/%m/%Y %H:%M:%S'
    timeleft =(dt.datetime.strptime(moment1, dmYFMT) - dt.datetime.strptime(moment2, dmYFMT))
    milisec=1000*timeleft.total_seconds()
    if(milisec<=0):
        milisec=0

    return milisec


def Number_ppl_waiting(threshold, wait_list):
    num = 0
    for i in wait_list:
        if (i>=threshold):
            num = num+1

    return num

def Waiting_times():
    wait_list_A = []
    wait_list_D = []
    with open('/Users/Thomartin/StanleyR/Reso2/activitylog.csv', 'rt') as log:
        lines = csv.reader(log, delimiter=',')
        next(lines, None)
        for line in lines:
            if (line[1] =="ARRIVEE"):
                hours= int(line[8].split(':')[0])
                mins= int(line[8].split(':')[1])
                secs= int(line[8].split(':')[2])
                attente= 3600*hours+60*mins+secs
                wait_list_A.append(attente)

            if (line[1] =="DEPART"):

                hours= int(line[8].split(':')[0])
                mins= int(line[8].split(':')[1])
                secs= int(line[8].split(':')[2])
                attente= 3600*hours+60*mins+secs
                wait_list_D.append(attente)


        print("mean waiting time when arriving: %s" %mean(wait_list_A))
        print("sqrt variance when arriving: %s" %sqrtvariance(wait_list_A))
        print("number of people waiting more than 1 min when arriving: %s" %Number_ppl_waiting(60,wait_list_A))
        print("number of people waiting more than 2 min when arriving: %s" %Number_ppl_waiting(120,wait_list_A))
        print("number of people waiting more than 5 min when arriving: %s" %Number_ppl_waiting(300,wait_list_A))
        print("number of people waiting more than 10 min when arriving: %s" %Number_ppl_waiting(600,wait_list_A))

        print("mean waiting time when departing: %s" %mean(wait_list_D))
        print("sqrt variance when departing: %s" %sqrtvariance(wait_list_D))
        print("number of people waiting more than 1 min when departing: %s" %Number_ppl_waiting(60,wait_list_D))
        print("number of people waiting more than 2 min when departing: %s" %Number_ppl_waiting(120,wait_list_D))
        print("number of people waiting more than 5 min when departing: %s" %Number_ppl_waiting(300,wait_list_D))
        print("number of people waiting more than 10 min when departing: %s" %Number_ppl_waiting(600,wait_list_D))
        print("number of people waiting more than 12 min when departing: %s" %Number_ppl_waiting(720,wait_list_D))
        print("number of people waiting more than 100 min when departing: %s" %Number_ppl_waiting(6000,wait_list_D))
        print("number of people waiting more than 10000 min when departing: %s" %Number_ppl_waiting(6000000,wait_list_D))


def Distance_Walked():
    lenght = 5
    totaldist_arrival=0
    totaldist_departure=0
    numberdeparted=0
    numberarrived=0
    with open('test_10_robot_20_depot_demo_proportionnel.csv', 'rb') as log:
        lines = csv.reader(log, delimiter='\t')
        next(lines, None)
        for line in lines:
            if(line[1] =="STORING"):
                IDplace = line[12].split('.')
                location = int(IDplace[1])
                totaldist_arrival = totaldist_arrival+lenght*location
                numberarrived = numberarrived+1

            if(line[1] =="EXITING"):
                IDplace = line[13].split('.')
                location = int(IDplace[1])
                totaldist_departure = totaldist_departure+lenght*location
                numberdeparted = numberdeparted+1

    mean_arrival = totaldist_arrival/numberarrived
    mean_departure = totaldist_departure/numberdeparted
    mean = (totaldist_departure+totaldist_arrival)/(numberarrived + numberdeparted)
    print("During the time period, %s people arrived. They walked an average %s meters"%(numberarrived,mean_arrival))
    print("During the time period, %s people departed. They walked an average %s meters"%(numberdeparted,mean_departure))
    print("Overall, people walk an average %s meters when using the parking"%mean)


Waiting_times()
