import csv
class Airplane:
    name = "airplane"

    def __init__(self, id, type, model, maker, nrSeats):
        self.id = id
        self.type = type
        self.model = model
        self.maker = maker
        self.nrSeats = nrSeats

    def __str__(self):
        # csv representation
        airplaneDict = vars(self)
        valuesStr = [str(x) for x in airplaneDict.values()]
        return ",".join(valuesStr)

    def header(self):
        return ",".join(vars(self))


data = list(csv.reader(open("/Users/Arnar/VLN1/src/data/airplanes.csv")))
testing = (data[1])
print(testing)