import csv
from datetime import datetime
from objects.airplane import Airplane
from objects.employee import Employee
from objects.destination import Destination
from objects.flight import Flight
from objects.voyage import Voyage
from objects.collection import Collection

class File:
    def writeArray(self,f, arr):
        # writes a list of objects to a
        # csv file
        f.write(arr[0].header() + "\n") # header row
        for object in arr: # data rows
            f.write(str(object) + "\n")

    def writeEmployees(self, employees):
        with open("data/employees.csv", "w") as f:
            self.writeArray(f,employees)

    def writeAirplanes(self, airplanes):
        with open("data/airplanes.csv", "w") as f:
            self.writeArray(f,airplanes)

    def writeVoyages(self, voyages):
        with open("data/voyages.csv", "w") as f:
            self.writeArray(f,voyages)

    def writeDestinations(self, destinations):
        with open("data/destinations.csv", "w") as f:
            self.writeArray(f,destinations)

    def writeFlights(self, flights):
        with open("data/flights.csv","w") as f:
            self.writeArray(f,flights)

    def write(self, key, data):
        # writes a collection of objects
        # to the correct file
        if key == "airplanes":
            self.writeAirplanes(data.all)
        elif key == "destinations":
            self.writeDestinations(data.all)
        elif key == "employees":
            self.writeEmployees(data.all)
        elif key == "voyages":
            self.writeVoyages(data.all)
        elif key == "flights":
            self.writeFlights(data.all)

    def readAirplanes(self):
        with open("data/airplanes.csv", "r") as f:
            csv_reader = csv.DictReader(f)
            planes = []
            for row in csv_reader:
                plane = self.newAirplane(row)
                planes.append(plane)
        return Collection(planes, "airplanes")

    def newAirplane(self, row):
        return Airplane(
            row["id"],
            row["type"],
            row["model"],
            row["maker"],
            row["nrSeats"])

    def readEmployees(self):
        with open("data/employees.csv") as f:
            csv_reader = csv.DictReader(f)
            employees = []
            for row in csv_reader:
                employee = self.newEmployee(row)
                employees.append(employee)
        return Collection(employees, "employees")

    def newEmployee(self, row):
        # new employee from csv row
        return Employee(
            row["name"],
            row["ssn"],
            row["address"],
            row["mobile"],
            row["email"],
            row["rank"],
            row["license"])

    def readDestinations(self):
        with open("data/destinations.csv") as f:
            csv_reader = csv.DictReader(f)
            destinations = []
            for row in csv_reader:
                destination = self.newDestination(row)
                destinations.append(destination)
        return Collection(destinations, "destinations")

    def newDestination(self, row):
        # new destination from csv row
        return Destination(
            row["id"],
            row["destination"],
            row["country"],
            int(row["flightTime"]),
            row["distance"],
            row["contactName"],
            row["contactNr"])

    def readFlights(self, airplanes, destinations):
        with open("data/flights.csv") as f:
            csv_reader = csv.DictReader(f)
            flights = []
            for row in csv_reader:
                flight = self.newFlight(row, airplanes, destinations)
                flights.append(flight)
            return Collection(flights, "flights")

    def newFlight(self, row, airplanes, destinations):
        # new flight from csv row
        return Flight(
            airplanes.filter(("=", "id", row["airplane"])),
            destinations.filter(("=", "id", row["destination"])),
            datetime.strptime(row["departure"],"%Y-%m-%dT%H:%M:%S"),
            row["flightNr"],
            int(row["seatSold"]))

    def readVoyages(self, flights, employees):
        with open("data/voyages.csv") as f:
            csv_reader = csv.DictReader(f)
            voyages = []
            for row in csv_reader:
                voyage = self.newVoyage(row, flights, employees)
                voyages.append(voyage)
        return Collection(voyages, "voyages")

    def newVoyage(self, row, flights, employees):
        # new voyage from csv row
        try:
            flightAttendsSsn = row["flightAttendants"].split(";")
            flightAttends = []
            for fas in flightAttendsSsn:
                flightAttends.append(employees.filter(("=", "ssn", fas)))
            return Voyage(flights.filter(("=", "id", row["outFlight"])),
                          flights.filter(("=", "id", row["returnFlight"])),
                          employees.filter(("=", "ssn", row["flightCaptain"])),
                          employees.filter(("=", "ssn", row["flightAssistant"])),
                          employees.filter(("=", "ssn", row["headAttendant"])),
                          flightAttends)
        except KeyError:
            return Voyage(flights.filter(("=", "id", row["outFlight"])),
                          flights.filter(("=", "id", row["returnFlight"])))


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
"""
if __name__ == "__main__":
    f = File()
    all_obj = f.read()
    fs = all_obj["flights"].all
    vs = all_obj["voyages"].all
    for i in range(len(fs)):
        vi = i//2
        if i % 2 == 0:
            vs[vi].outFlight = fs[i]
        else:
            vs[vi].returnFlight = fs[i]
    f.write("voyages",all_obj["voyages"])
"""
