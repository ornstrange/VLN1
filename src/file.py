import csv
from datetime import datetime
from objects.airplane import Airplane
from objects.employee import Employee
from objects.destination import Destination
from objects.flight import Flight
from objects.voyage import Voyage
from objects.collection import Collection
from random import randint

class File:
    def write(self,f, arr):
        # writes a list of objects to a
        # csv file
        header = vars(arr[0]) # header row
        f.write(",".join(list(header.keys())) + "\n")
        for object in arr: # data rows
            f.write(str(object) + "\n")

    def writeEmployees(self, employees):
        with open("data/employees.csv", "w") as f:
            self.write(f,employees)

    def writeAirplanes(self, airplanes):
        with open("data/airplanes.csv", "w") as f:
            self.write(f,airplanes)

    def writeVoyages(self, voyages):
        with open("data/voyages.csv", "w") as f:
            self.write(f,voyages)

    def writeDestinations(self, destinations):
        with open("data/destinations.csv", "w") as f:
            self.write(f,destinations)

    def writeFlight(self, flights):
        with open("data/flights.csv","w") as f:
            self.write(f,flights)

    def readAirplanes(self):
        with open("data-yeet/airplanes.csv", "r") as f:
            csv_reader = csv.DictReader(f)
            planes = []
            for row in csv_reader:
                plane = Airplane(
                    row["id"],
                    row["type"],
                    row["model"],
                    row["maker"],
                    row["nrSeats"])
                planes.append(plane)
        return Collection(planes)

    def readEmployees(self):
        with open("data-yeet/employees.csv") as f:
            csv_reader = csv.DictReader(f)
            employees = []
            for row in csv_reader:
                employee = Employee(
                    row["name"],
                    row["ssn"],
                    row["address"],
                    row["mobile"],
                    row["email"],
                    row["rank"],
                    row["license"])
                employees.append(employee)
        return Collection(employees)

    def readDestinations(self):
        with open("data-yeet/destinations.csv") as f:
            csv_reader = csv.DictReader(f)
            destinations = []
            for row in csv_reader:
                destination = Destination(
                    row["id"],
                    row["destination"],
                    row["country"],
                    int(row["flightTime"]),
                    row["distance"],
                    row["contactName"],
                    row["contactNr"])
                destinations.append(destination)
        return Collection(destinations)

    def readFlights(self, airplanes, destinations):
        with open("data-yeet/flights.csv") as f:
            csv_reader = csv.DictReader(f)
            flights = []
            for row in csv_reader:
                flight = Flight(airplanes.filter(("id", row["airplane"])),
                                destinations.filter(("id", row["destination"])),
                                datetime.strptime(row["departure"],"%Y-%m-%dT%H:%M:%S"),
                                row["flightNr"],
                                int(row["seatSold"]))
                flights.append(flight)
        return Collection(flights)

    def readVoyages(self, flights, employees):
        with open("data-yeet/voyages.csv") as f:
            csv_reader = csv.DictReader(f)
            voyages = []
            for row in csv_reader:
                flightAttendsSsn = row["flightAttendants]"].split(";")
                fligthAttends = []
                for fas in flightAttendsSsn:
                    fligthAttends.append(employees.filter(("ssn", fas)))
                voyage = Voyage(
                    flights.filter("id", row["outFlight"]),
                    flights.filter("id", row["returnFlight"]),
                    employees.filter("ssn", row["flightCaptain"]),
                    employees.filter("ssn", row["flightAssistant"]),
                    employees.filter("ssn", row["headAttendant"]),
                    fligthAttends)
                voyages.append(voyage)
        return Collection(voyages)

    def read(self):
        # runs every read function in the correct order
        # returns a dictionary of the collections
        airplanes = self.readAirplanes()
        employees = self.readEmployees()
        destinations = self.readDestinations()
        flights = self.readFlights(airplanes, destinations)
        voyages = self.readVoyages(flights, employees)
        return {"airplanes": airplanes,
                "employees": employees,
                "destinations": destinations,
                "flights": flights,
                "voyages": voyages}


if __name__ == "__main__":
    file = File()
    airplanes = file.readAirplanes()
    employees = file.readEmployees()
    destinations = file.readDestinations()
    flightsArr = []
    voyArr = []

    f = open("data-yeetyeet/UPDATEDSTUDENTDATA/PastFlights.csv", "r")
    _header = f.readline()
    lastDate = None
    while True:
        l1 = f.readline().split(",")
        l2 = f.readline().split(",")

        if l1 == [''] or l2 == ['']:
            break

        flightNr = "NA"
        bla = 0
        for char in l1[2]:
            bla += ord(char)
        flightNr += f"{bla % 100:02}"
        dayCounter = 0
        if datetime.strptime(l1[3], "%Y-%m-%dT%H:%M:%S").day == lastDate:
            dayCounter += 1
        else:
            dayCounter = 0
        flightNr += str(dayCounter * 2)
        lastDate = datetime.strptime(l1[3], "%Y-%m-%dT%H:%M:%S").day

        f1 = Flight(
            airplanes.filter(("id", l1[5])),
            destinations.filter(("id", l1[2])),
            datetime.strptime(l1[3], "%Y-%m-%dT%H:%M:%S"),
            flightNr,
            randint(20,60)
        )
        f2 = Flight(
            airplanes.filter(("id", l2[5])),
            destinations.filter(("id", l2[2])),
            datetime.strptime(l2[3], "%Y-%m-%dT%H:%M:%S"),
            flightNr[:-1] + str(int(flightNr[-1]) + 1),
            randint(20,60)
        )
        fas = []
        for p in l1[9].split(";"):
            fas.append(employees.filter(("ssn", p)))
        voy = Voyage(
            f1,
            f2,
            employees.filter(("ssn", l1[6])),
            employees.filter(("ssn", l1[7])),
            employees.filter(("ssn", l1[8])),
            fas
        )
        flightsArr.append(f1)
        flightsArr.append(f2)
        voyArr.append(voy)
    flights = Collection(flightsArr)
    voyages = Collection(voyArr)

    file.writeEmployees(employees.all)
    file.writeDestinations(destinations.all)
    file.writeAirplanes(airplanes.all)
    file.writeFlight(flights.all)
    file.writeVoyages(voyages.all)

