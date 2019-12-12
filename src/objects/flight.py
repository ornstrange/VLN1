class Flight:
    name = "flight"

    def __init__(self, airplane, destination, departure, flightNr, seatSold):
        self.airplane = airplane
        self.destination = destination
        self.departure = departure
        self.arrival = departure + destination.flightTime
        self.flightNr = flightNr
        self.seatSold = seatSold
        self.id = self.createId()

    def createId(self):
        flightId = str(self.departure.year)
        flightId += str(self.departure.month)
        flightId += str(self.departure.day)
        flightId += str(self.departure.hour)
        flightId += str(self.departure.minute)
        flightId += str(self.departure.second)
        flightId = int(flightId)
        flightId = hex(flightId)[2:]
        return flightId

    def __str__(self):
        # csv representation
        flightDict = vars(self)
        flightDictVals = list(flightDict.values())[:-1]
        for i in range(len(flightDictVals)):
            if type(flightDictVals[i]).__name__ == "Airplane":
                flightDictVals[i] = flightDictVals[i].id
            elif type(flightDictVals[i]).__name__ == "Destination":
                flightDictVals[i] = flightDictVals[i].id
            elif type(flightDictVals[i]).__name__ == "datetime":
                flightDictVals[i] = flightDictVals[i].strftime("%Y-%m-%dT%H:%M:%S")
        valuesStr = [str(x) for x in flightDictVals]
        return ",".join(valuesStr)

    def header(self):
        headerRow = vars(self)
        headerRowNoId = list(headerRow)[:-1]
        return ",".join(headerRowNoId)

    def fieldsRules(self):
        return [
            ("departure",
             "Departure date (ex. 2018-10-09 23:52:48)",
             "\d{4}(-\d{2}){2}\s\d{2}(:\d{2}){2}"),
            ("seatSold",
             "Number of seats sold (ex. 35)",
             "\d+")
        ]

