import datetime

class Voyage:
    name = "voyage"

    def __init__(self, outFlight, returnFlight,
                 flightCaptain=None, flightAssistant=None,
                 headAttendant=None, flightAttendants=None):
        self.outFlight = outFlight
        self.returnFlight = returnFlight
        self.flightCaptain = flightCaptain
        self.flightAssistant = flightAssistant
        self.headAttendant = headAttendant
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

    def fieldsRules(self):
        return [
            ("departureOut",
             "Departure out flight (ex. 2018-10-09 23:52:48)",
             "\d{4}(-\d{2}){2}\s\d{2}(:\d{2}){2}"),
            ("seatSoldOut",
             "Number of seats sold out flight (ex. 35)",
             "\d+"),
            ("departureRet",
             "Departure return flight (ex. 2018-10-15 23:52:48)",
             "\d{4}(-\d{2}){2}\s\d{2}(:\d{2}){2}"),
            ("seatSoldRet",
             "Number of seats sold return flight (ex. 35)",
             "\d+"),
            ("airplane",
             "Select Airplane",
             "SEL")
        ]

