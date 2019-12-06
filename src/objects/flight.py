import uuid

class Flight:
    namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

    def __init__(self, airplane, destination, departure, flightNr, seatSold):
        self.airplane = airplane
        self.destination = destination
        self.departure = departure
        self.arrival = departure + destination.flightTime
        self.flightNr = flightNr
        self.seatSold = seatSold
        self.id = uuid.uuid3(Flight.namespace, str(self.departure))

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

