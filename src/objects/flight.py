from airplane import Airplane
from destination import Destination

class Flight:
    def __init__(self, airplane, destination, departure, flightNr):
        self.airplane = airplane
        self.destination = destination
        self.departure = departure
        self.arrival = self.departure + self.destination.flightTime
        self.flightNr = flightNr

    def __str__(self):
        # csv representation
        output = ""
        flightDict = vars(self)
        for val in flightDict.values():
            output += f"{val},"
        return output[:-1] # strip last comma
