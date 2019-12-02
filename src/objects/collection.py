class Collection:
    def __init__(self, data):
        self.all = data

    def sort(self, key):
        try:
            return sorted(self.all, key=lambda x: vars(x)[key])
        except KeyError:
            return self.all

    def filterOne(self, key, value):
        try:
            return filter(self.all, lambda x: vars(x)[key] == value)
        except (KeyError, ValueError):
            return self.all
    def mainFilter(self, data):
        pass

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

