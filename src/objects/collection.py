# test purposes
from airplane import Airplane

class Collection:
    def __init__(self, data):
        self.all = data

    def sort(self, key):
        try:
            return sorted(self.all, key=lambda x: vars(x)[key])
        except KeyError:
            return self.all

    def filterKeyVal(self, key, val):
        # filters a list using key, value
        try:
            return filter(arr, lambda x: vars(x)[key] == val)
        except (KeyError, ValueError):
            return None

    def filter(self, data):
        # filters all elements using a list of
        # (key, value) tuples
        filtered = self.all
        try:
            for key, val in data:
                filtered = self.filterKeyVal(key, val)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            return filtered
        except (KeyError, ValueError):
            return None


class Employees:
    def __init__(self, pilots=None, flightAttendants=None):
        self.pilots = pilots if pilots else []
        self.flightAttendants = flightAttendants if flightAttendants else []
        self.all = self.pilots if self.pilots else []
        if flightAttendants:
            self.all += self.flightAttendants


emps = Collection([Airplane(5,"a","b",10), Airplane(1,"c","d",20)])

print(emps.all)
print(emps.sort("id"))

