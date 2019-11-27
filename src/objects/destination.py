from datetime import timedelta

class Destination:
    def __init__(self, country, airport, flightTime, distance, contactName, contactNr):
        self.country = country
        self.airport = airport
        self.flightTime = timedelta(minutes=flightTime)
        self.distance = distance
        self.contactName = contactName
        self.contactNr = contactNr
