import csv

def initializeFlight():
    with open("data-yeetyeet/UPDATEDSTUDENTDATA/PastFlights.csv","r") as f:
        flightList = []
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            if row["arrivingAt"]
            flightList.append([row["aircraftID"],row["arrivingAt"],row["departure"],"fNum",50])

    return flightList

listinn = initializeFlight()
print(listinn[0])

from datetime import datetime
from objects.flight import Flight
from objects.voyage import Voyage
from random import randint

f = open("data-yeetyeet/UPDATEDSTUDENTDATA/PastFlights.csv", "r")
_header = f.readline()
lastDate = None
while True:
    try:
        l1 = f.readline().split(",")
        l2 = f.readline().split(",")

        flightNr = "NA"
        bla = 0
        for char in l1[2]:
            bla += ord(char)
        flightNr += f"{bla % 100:02}"
        dayCounter = 0
        if datetime.strptime(l1[3], "%Y-%m-%dT%H:%M:%S").day() == lastDate:
            dayCounter += 1
        else:
            dayCounter = 0
        flightNr += str(dayCounter * 2)
        
        f1 = Flight(
            l1[5],
            l1[2],
            datetime.strptime(l1[3], "%Y-%m-%dT%H:%M:%S"),
            flightNr,
            randint(20,60)
        )
        f2 = Flight(
            l2[5],
            l2[2],
            datetime.strptime(l2[3], "%Y-%m-%dT%H:%M:%S"),
            flightNr[:-1] + str(int(flightNr[-1]) + 1),
            randint(20,60)
        )
        voy = Voyage(
            f1.flightNr,
            f2.flightNr,
            
        )
    except:
        break