from datetime import timedelta

class Destination:
    def __init__(self, id, destination, country,
                 flightTime, distance, contactName, contactNr):
        self.id = id
        self.destination = destination
        self.country = country
        self.flightTime = timedelta(seconds=flightTime)
        self.distance = distance
        self.contactName = contactName
        self.contactNr = contactNr

    def __str__(self):
        # csv representation
        destDict= vars(self)
        destDictVals = list(destDict.values())
        for i in range(len(destDictVals)):
            if type(destDictVals[i]).__name__ == "timedelta":
                destDictVals[i] = destDictVals[i].seconds
        valuesStr = [str(x) for x in destDictVals]
        return ",".join(valuesStr)

    def __repr__(self):
        # debug repr
        output = "Destination: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"
