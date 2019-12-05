from datetime import timedelta

class Destination:
    def __init__(self, id, destination, flightTime,
                 distance, contactName, contactNr):
        self.id = id
        self.destination = destination
        self.flightTime = timedelta(seconds=flightTime)
        self.distance = distance
        self.contactName = contactName
        self.contactNr = contactNr


    def __str__(self):
        destinationDict = vars(self)  # makes dictionary form self
        valuesStr = [str(x) for x in destinationDict.values()]
        return ",".join(valuesStr)

    def __repr__(self):
        output = "Destination: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
            print(output)
        return output.strip() + "]"

__repr__(self)
