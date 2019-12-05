class Collection:
    def __init__(self, data):
        self.all = data

    def __getitem__(self, index):
        return self.all[index]

    def sort(self, key):
        #sorts a list using key
        try:
            return sorted(self.all, key=lambda x: vars(x)[key]) 
        except KeyError:
            return self.all

    def filterKeyVal(self, arr, key, val):
        # filters a list using key, value
        try:
            return list(filter(lambda x: vars(x)[key] == val, arr))
        except (KeyError, ValueError):
            return None

    def filter(self, *args):
        # filters all elements using a list of
        # (key, value) tuples
        filtered = self.all
        try:
            for key, val in args:
                if type(key).__name__ == "datetime":
                    begin, end = key, val
                    filtered = self.filterDate(filtered, begin, end)
                else:
                    filtered = self.filterKeyVal(filtered, key, val)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            return filtered if len(filtered) > 1 else filtered[0]
        except (KeyError, ValueError):
            return None

    def filterDate(self, begin, end):
        # filters a list using a begin and end date
        try:
            return list(filter(lambda x: begin <= x.departure <= end, arr))
        except (ValueError, KeyError):
            return None

"""
planes = Collection([
    Airplane(5,"a","bruh","b",10),
    Airplane(1,"c","dude","d",20),
    Airplane(10,"p","trans","b",50)])

print(planes.all)
print(planes.sort("id"))
print(planes.sort("type"))
print(planes.filter(("id",5)))
print(planes.filter(("model","b")))

seatSold1 = 50
plane2 = Airplane(5,"t1","djok","boeing",101)
dest1 = Destination("ru","ruair",18000,25000,"slavko","112")
dest22 = Destination("is","wowair",dest.flightTime.seconds,dest.distance,"palli","5554889")
outFlight1 = Flight(plane, dest, datetime.strptime("28 11 2019", "%d %m %Y"), "test1")
retFlight1 = Flight(plane, dest2, datetime.strptime("29 11 2019", "%d %m %Y"), "test2")
captn1 = Employee("Kalli","1234567890","Hraun 2","555-1234","868-3322","kalli@kallz.is", "captn", "737 max")
asstn1 = Employee("Palli","1234567890","Hraun 4","555-4321","868-2323","palli@pallz.is", "asstn", "737 max")
topfa1 = Employee("Gugga","1234567908","Hraun 6","555-1234","868-3322","guggz@kallz.is", "top")
other1 = Employee("Pugga","1234567908","Hraun 8","555-4321","868-2323","puggz@pallz.is", "basic")
voyage1 = Voyage(seatSold1, outFlight1, retFlight1, captn1, asstn1, topfa1, [other1])

print(voyage1)
"""
