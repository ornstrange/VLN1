from copy import deepcopy
from datetime import datetime
from .flight import Flight
import re

class Collection:
    def __init__(self, data, name):
        self.all = data
        self.name = name

    def __getitem__(self, index):
        return self.all[index]

    def sort(self, key):
        # sorts a list using key
        try:
            self.all = sorted(self.all, key=lambda x: vars(x)[key])
            return self
        except KeyError:
            return self

    def filterKeyVal(self, key, val, arr):
        # filters a list using key, value
        try:
            return list(filter(lambda x: vars(x)[key] == val, arr))
        except (KeyError, ValueError):
            return None

    def filterDate(self, begin, end, arr):
        # filters a list using a begin and end date
        try:
            return list(filter(lambda x: begin <= x.outFlight.departure <= end, arr))
        except (ValueError, KeyError):
            return None

    def filterRegex(self, key, reg, arr):
        # filters a list using a key, bla
        try:
            return list(filter(lambda x: re.search(reg, vars(x)[key]),arr, re.IGNORECASE))
        except (KeyError, ValueError):
            return None

    def filter(self, *args):
        # filters all elements using a list of
        # (key, value) tuples
        filtered = deepcopy(self.all)
        try:
            for op, key, val in args:
                if op == "d":
                    begin, end = key, val
                    filtered = self.filterDate(begin, end, filtered)
                elif op == "?":
                    reg = val
                    filtered = self.filterRegex(key, reg, filtered)
                elif op == "=":
                    filtered = self.filterKeyVal(key, val, filtered)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            if len(filtered) == 1:
                return filtered[0]
            else:
                return Collection(filtered, self.name)
        except (KeyError, ValueError):
            return None

    def createFlight(self, fields):
        _sum = 0
        for char in fields["destination"].id:
            _sum += ord(char)
        destId = f"{_sum % 100:02}"
        curDayStartStr = fields["departure"].split(" ")[0]+" 00:00:00"
        curDayStart = datetime.strptime(curDayStartStr,"%Y-%m-%d %H:%M:%S")
        curDayEndStr = fields["departure"].split(" ")[0]+" 23:59:59"
        curDayEnd = datetime.strptime(curDayEndStr,"%Y-%m-%d %H:%M:%S")
        flightsToday = self.filter(('d', curDayStart, curDayEnd))
        if flightsToday:
            curFlightNumber = f"{len(flightsToday) * 2:02}"
        else:
            curFlightNumber = "00"
        flightNr = "NA" + destId + curFlightNumber
        return Flight(
            fields["airplane"],
            fields["destination"],
            datetime.strptime(fields["departure"], "%Y-%m-%d %H:%M:%S"),
            flightNr,
            int(fields["seatSold"])
        )

