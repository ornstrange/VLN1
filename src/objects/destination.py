from datetime import timedelta

class Destination:
    def __init__(self,id, destination, flightTime, distance, contactName, contactNr):
        self.id = id
        self.destination = destination
        self.flightTime = timedelta(seconds=flightTime)
        self.distance = distance
        self.contactName = contactName
        self.contactNr = contactNr


    def __str__(self):
        # csv representation
        destinationDict = vars(self)
        valuesStr = [str(x) for x in destinationDict.values()]
        return ",".join(valuesStr)

    def __repr__(self):
        # debug repr
        output = "Destination: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"
