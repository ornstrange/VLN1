import csv

with open("Aircraft.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile)
    with open("AircraftType.csv", newline="") as csvfile:
        type = csv.reader(csvfile)

    for row in spamreader:
        row = list(row)
        row = row[0]
        print(row)



    




