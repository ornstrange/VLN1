from airplane.py import Airplane
from destination.py import Destination
from employee.py import Pilot, FlightAttendant
from voyage.py import Voyage


class Airplanes:
    def __init__(self, airplanes=None)
        self.all = airplanes if airplanes else []


class Voyages:
    def __init__(self, voyages=None)
        self.all = voyages if voyages else []


class Destinations:
    def __init__(self, destinations=None)
        self.all = destinations if destinations else []


class Employees:
    def __init__(self, pilots=None, flightAttendants=None)
        self.pilots = pilots if pilots else []
        self.flightAttendants = flightAttendants if flightAttendants else []
        self.all = self.pilots if self.pilots else []
        if flightAttendants:
            self.all += self.flightAttendants
