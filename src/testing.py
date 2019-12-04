
import csv

with open("Aircraft.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile)

    for row in spamreader:
        print(",".join(row))


#filestream = open("./testData/Aircraft.csv","r")

#if filestream:
    
    #for line in filestream: 
        #print(line.strip())