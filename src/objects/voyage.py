from datetime import datetime

from flight import Flight
from employee import Pilot, FlightAttendant

class Voyage:
    def __init__(self, seatSold, outFlight, returnFlight, flightCaptain,
                 flightAssistant, headAttendant, flightAttendants)
        self.seatSold = seatSold
        self.outFlight = outFlight
        self.returnFlight = returnFlight
        self.flightCaptain = flightCaptain
        self.flightAssistant = flightAssistant
        self.headAttendant = headAttendant
        self.flightAttendants = flightAttendants

    def emptySeats(self):
        return outFlight.airplane.nrSeats - self.seatSold

    def status(self):
        timeNow = datetime.now()
        if timeNow < outFlight.departure:
            return "Ekki hafin"
        if timeNow < outFlight.arrival:
            return "Á leið út"
        if timeNow < returnFlight.departure:
            return "Lent úti"
        if timeNow < returnFlight.arrival:
            return "Á leið heim"
        return "Lokið"

