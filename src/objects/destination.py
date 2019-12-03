from datetime import timedelta

class Destination:
    def __init__(self, country, airport, flightTime, distance, contactName, contactNr):
        self.country = country
        self.airport = airport
        self.flightTime = timedelta(seconds=flightTime)
        self.distance = distance
        self.contactName = contactName
        self.contactNr = contactNr

    def __str__(self):
        # csv representation
        output = ""
        destDict = vars(self)
        for val in destDict.values():
            output += f"{val},"
        return output[:-1] # strip last comma
