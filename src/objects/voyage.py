class Voyage:
    def __init__(self, seatSold, outFlight, returnFlight, flightCaptain,
                 flightAssistant, headAttendant, flightAttendants):
        self.seatSold = seatSold
        self.outFlight = outFlight
        self.returnFlight = returnFlight
        self.flightCaptain = flightCaptain
        self.flightAssistant = flightAssistant
        self.headAttendant = headAttendant
        self.flightAttendants = flightAttendants
        self.emptySeats = outFlight.airplane.nrSeats - seatSold

    def status(self):
        timeNow = datetime.now()
        outFlight = self.outFlight
        returnFlight = self.returnFlight
        if timeNow < outFlight.departure:
            return "Ekki hafin"
        if timeNow < outFlight.arrival:
            return "Á leið út"
        if timeNow < returnFlight.departure:
            return "Lent úti"
        if timeNow < returnFlight.arrival:
            return "Á leið heim"
        return "Lokið"

    def __str__(self):
        # csv representation
        voyageDict = vars(self)
        voyageDictVals = voyageDict.values()
        for i in range(len(voyageDictVals)):
            if type(voyageDictVals[i]).__name__ == "Flight":
                voyageDictVals[i] = voyageDictVals[i].flightnr
            if type(voyageDictVals[i]).__name__ == "Employee":
                voyageDictVals[i] = voyageDictVals[i].ssn
        valuesStr = [str(x) for x in voyageDictVals]
        return ",".join(valuesStr)

    def __repr__(self):
        # debug repr
            output = "Voyage: ["
            items = vars(self)
            for key in items:
                output += f"{key}: {items[key]}, "
            return output.strip() + "]"

if __name__ == "__main__":
    # tests
    from datetime import timedelta, datetime
    from destination import Destination
    from flight import Flight
    from employee import Employee
    from airplane import Airplane
    seatSold = 50
    plane = Airplane(5,"t1","boeing",101,67)
    dest = Destination("ru","ruair",18000,25000,"slavko","112",6)
    print(plane)

