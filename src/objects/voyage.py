import datetime

class Voyage:
    name = "voyage"

    def __init__(self, outFlight, returnFlight, flightCaptain,
                 flightAssistant, headAttendant, flightAttendants):
        self.outFlight = outFlight
        self.returnFlight = returnFlight
        self.flightCaptain = flightCaptain
        self.flightAssistant = flightAssistant
        self.headAttendant = headAttendant
        if type(flightAttendants).__name__ == "Collection":
            self.flightAttendants = flightAttendants.all
        else:
            self.flightAttendants = flightAttendants

    def status(self):
        # Gives flight status by comparing flight schedule to present time.
        timeNow = datetime.now()
        outFlight = self.outFlight
        returnFlight = self.returnFlight
        if timeNow < outFlight.departure:
            return "Not started"
        if timeNow < outFlight.arrival:
            return "Heading out"
        if timeNow < returnFlight.departure:
            return "Landed out"
        if timeNow < returnFlight.arrival:
            return "Heading home"
        return "Finished"

    def __str__(self):
        # csv representation
        voyageDict = vars(self)
        voyageDictVals = list(voyageDict.values())
        for i in range(len(voyageDictVals)):
            if type(voyageDictVals[i]).__name__ == "Flight":
                voyageDictVals[i] = voyageDictVals[i].id
            if type(voyageDictVals[i]).__name__ == "Employee":
                voyageDictVals[i] = voyageDictVals[i].ssn
            if type(voyageDictVals[i]).__name__ == "list":
                voyageDictVals[i] = ";".join([x.ssn for x in voyageDictVals[i]])
        valuesStr = [str(x) for x in voyageDictVals]
        return ",".join(valuesStr)

    def header(self):
        return ",".join(vars(self))

