filestream = open("./testData/Aircraft.csv","r")

if filestream:
    
    for line in filestream: 
        print(line.strip())