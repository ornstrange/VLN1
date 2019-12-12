from datetime import timedelta

class Destination:
    name = "destination"

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

    def header(self):
        return ",".join(vars(self))

    def fieldsRules(self):
        return [
            ("id",
             "Identification Number (ex. KEF)",
             "[A-Z]{3}"),
            ("destination",
             "City / Town (ex. Keflavik)",
             "[A-Z][a-z]+"),
            ("country",
             "Country (ex. Iceland)",
             "[A-Z][a-z]+"),
            ("flightTime",
             "Flighttime in minutes (ex. 530)",
             "\d+"),
            ("distance",
             "Distance in meters (ex. 1000000)",
             "\d+"),
            ("contactName",
             "Contact Name (ex. Paul)",
             "[a-zA-Z]+"),
            ("contactNr",
             "Contact Number (ex. 911)",
             "\d+")
        ]

