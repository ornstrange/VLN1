class Flight:
    def __init__(self, airplane, destination, departure, flightNr):
        self.airplane = airplane
        self.destination = destination
        self.departure = departure
        self.arrival = departure + destination.flightTime
        self.flightNr = flightNr

    def __str__(self):
        # csv representation
        flightDict = vars(self)
        flightDictVals = flightDict.values()
        for i in range(len(flightDictVals)):
            if type(flightDictVals[i]).__name__ == "Airplane":
                flightDictVals[i] = flightDictVals[i].id
            if type(flightDictVals[i]).__name__ == "Destination":
                flightDictVals[i] = flightDictVals[i].country
        valuesStr = [str(x) for x in flightDictVals]
        return ",".join(valuesStr)

    def __repr__(self):
        # debug repr
        output = "Flight: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"

