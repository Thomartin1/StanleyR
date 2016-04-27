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
    with open('test_10_robot_20_depot_demo_proportionnel.csv', 'rb') as log:
        lines = csv.reader(log, delimiter='\t')
        next(lines, None)
        for line in lines:
            if (line[1] =="ARRIVING"):

                wait_list_A.append(int(line[8]))
            if (line[1] =="EXITING"):
                wait_time=Time_remaining(line[6], line[7])
                # order_time = line[4].split(' ')
                # order_date = order_time[0].split('/')
                # order_moment = order_time[1].split(':')

                # order_day = int(order_date[0])
                # order_hour = int(order_moment[0])
                # order_minute = int(order_moment[1])
                # order_second = int(order_moment[2])


                # exec_time = line[5].split(' ')
                # exec_date = exec_time[0].split('/')
                # exec_moment = exec_time[1].split(':')

                # exec_day = int(exec_date[0])
                # exec_hour = int(exec_moment[0])
                # exec_minute = int(exec_moment[1])
                # exec_second = int(exec_moment[2])

                # wait_time = 1000* (exec_second-order_second)+60000*(exec_minute- order_minute)+3600000*(exec_hour - order_hour) +3600000*24*(exec_day - order_day)

                # if(wait_time>=100000):
                    # print(line)
                    # print(wait_time)
                wait_list_D.append(wait_time)
        # print (wait_list)

        print("mean waiting time when arriving: %s" %mean(wait_list_A))
        print("sqrt variance when arriving: %s" %sqrtvariance(wait_list_A))
        print("number of people waiting more than 1 min when arriving: %s" %Number_ppl_waiting(60000,wait_list_A))
        print("number of people waiting more than 2 min when arriving: %s" %Number_ppl_waiting(120000,wait_list_A))
        print("number of people waiting more than 5 min when arriving: %s" %Number_ppl_waiting(300000,wait_list_A))
        print("number of people waiting more than 10 min when arriving: %s" %Number_ppl_waiting(600000,wait_list_A))

        print("mean waiting time when departing: %s" %mean(wait_list_D))
        print("sqrt variance when departing: %s" %sqrtvariance(wait_list_D))
        print("number of people waiting more than 1 min when departing: %s" %Number_ppl_waiting(60000,wait_list_D))
        print("number of people waiting more than 2 min when departing: %s" %Number_ppl_waiting(120000,wait_list_D))
        print("number of people waiting more than 5 min when departing: %s" %Number_ppl_waiting(300000,wait_list_D))
        print("number of people waiting more than 10 min when departing: %s" %Number_ppl_waiting(600000,wait_list_D))
        print("number of people waiting more than 12 min when departing: %s" %Number_ppl_waiting(720000,wait_list_D))
        print("number of people waiting more than 100 min when departing: %s" %Number_ppl_waiting(6000000,wait_list_D))
        print("number of people waiting more than 10000 min when departing: %s" %Number_ppl_waiting(600000000,wait_list_D))


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


Distance_Walked()
Waiting_times()
