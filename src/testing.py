import csv

with open("Aircraft.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile)

    for row in spamreader:
        print(",".join(row))

