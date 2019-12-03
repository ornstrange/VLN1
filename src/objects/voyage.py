class Voyage:
    def __init__(self, seatSold, outFlight, returnFlight, flightCaptain,
                 flightAssistant, headAttendant, flightAttendants):
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
        outFlight = self.outFlight
        returnFlight = self.returnFlight
        if timeNow < outFlight.departure:
            return "Ekki hafin"
        if timeNow < outFlight.arrival:
            return "Á leið út"
        if timeNow < returnFlight.departure:
            return "Lent úti"
        if timeNow < returnFlight.arrival:
            return "Á leið heim"
        return "Lokið"

    """def __str__(self):
        return f"{self.seatSold},{self.outFlight},{self.returnFlight},{self.flightCaptain},"+\
               f"{self.flightAssistant},{self.headAttendant},{self.flightAttendants}""""

    def __str__(self):
        # csv representation
        voyageDict = vars(self)
        voyageDictVals = voyageDict.values()
        for i in range(len(voyageDictVals)):
            if type(voyageDictVals[i]).__name__ == "Flight":
                voyageDictVals[i] = voyageDictVals[i].flightnr
            if type(voyageDictVals[i]).__name__ == "Employee":
                voyageDictVals[i] = voyageDictVals[i].ssn
        valuesStr = [str(x) for x in flightDictVals]
        return ",".join(valuesStr)

        def __repr__(self):
        # debug repr
        output = "Voyage: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"


"""if __name__ == "__main__":
    from datetime import timedelta, datetime
    from destination import Destination
    from flight import Flight
    from employee import Employee
    from airplane import Airplane
    seatSold = 50
    plane = Airplane(5,"t1","boeing",101)
    dest = Destination("ru","ruair",18000,25000,"slavko","112")
    dest2 = Destination("is","wowair",dest.flightTime.seconds,dest.distance,"palli","5554889")
    outFlight = Flight(plane, dest, datetime.strptime("28 11 2019", "%d %m %Y"), "test1")
    retFlight = Flight(plane, dest2, datetime.strptime("29 11 2019", "%d %m %Y"), "test2")
    captn = Employee("Kalli","1234567890","Hraun 2","555-1234","868-3322","kalli@kallz.is", "captn", "737 max")
    asstn = Employee("Palli","1234567890","Hraun 4","555-4321","868-2323","palli@pallz.is", "asstn", "737 max")
    topfa = Employee("Gugga","1234567908","Hraun 6","555-1234","868-3322","guggz@kallz.is", "top")
    other = Employee("Pugga","1234567908","Hraun 8","555-4321","868-2323","puggz@pallz.is", "basic")
    voyage = Voyage(seatSold, outFlight, retFlight, captn, asstn, topfa, [other])

    print(voyage)
    print(voyage.emptySeats())

    seatSold1 = 50
    plane2 = Airplane(5,"t1","boeing",101)
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


    seatSold2 = 50
    plane2 = Airplane(5,"t1","boeing",101)
    dest1 = Destination("ru","ruair",18000,25000,"slavko","112")
    dest22 = Destination("is","wowair",dest.flightTime.seconds,dest.distance,"palli","5554889")
    outFlight2 = Flight(plane, dest, datetime.strptime("28 11 2019", "%d %m %Y"), "test1")
    retFlight2 = Flight(plane, dest2, datetime.strptime("29 11 2019", "%d %m %Y"), "test2")
    captn2 = Employee("Kalli","1234567890","Hraun 2","555-1234","868-3322","kalli@kallz.is", "captn", "737 max")
    asstn2 = Employee("Palli","1234567890","Hraun 4","555-4321","868-2323","palli@pallz.is", "asstn", "737 max")
    topfa2 = Employee("Gugga","1234567908","Hraun 6","555-1234","868-3322","guggz@kallz.is", "top")
    other2 = Employee("Pugga","1234567908","Hraun 8","555-4321","868-2323","puggz@pallz.is", "basic")
    voyage2 = Voyage(seatSold2, outFlight2, retFlight2, captn2, asstn2, topfa2, [other2])

    print(voyage2)"""
