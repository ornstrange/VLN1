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

    def __str__(self):
        return f"{self.seatSold},{self.outFlight},{self.returnFlight},{self.flightCaptain},"+\
               f"{self.flightAssistant},{self.headAttendant},{self.flightAttendants}"


if __name__ == "__main__":
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

