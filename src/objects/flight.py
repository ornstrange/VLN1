class Flight:
    def __init__(self, airplane, destination, departure, flightNr, seatSold):
        self.airplane = airplane
        self.destination = destination
        self.departure = departure
        self.arrival = departure + destination.flightTime
        self.flightNr = flightNr
        self.seatSold = seatSold

    def __str__(self):
        # csv representation
        flightDict = vars(self)
        flightDictVals = flightDict.values()
        for i in range(len(flightDictVals)):#loops through lenght of flightDictVals
            if type(flightDictVals[i]).__name__ == "Airplane":#if Airplane is found
                flightDictVals[i] = flightDictVals[i].id
            if type(flightDictVals[i]).__name__ == "Destination":#if Destination is found
                flightDictVals[i] = flightDictVals[i].id
        valuesStr = [str(x) for x in flightDictVals]
        return ",".join(valuesStr)#returns in a new list

    def __repr__(self):
        # debug repr
        output = "Flight: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"

