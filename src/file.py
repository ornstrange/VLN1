import csv
from objects.airplane import Airplane
from objects.employee import Employee
from objects.destination import Destination
from objects.flight import Flight
from objects.voyage import Voyage
from objects.collection import Collection

class File:
    def write(self,f, arr):
        # writes a list of objects to a
        # csv file
        header = vars(arr[0]) # header row
        f.write(",".join(list(header.keys())))
        for object in arr: # data rows
            f.write(str(object))
    
    def writeEmployees(self, employees):
        with open("data/employees.csv", "w+") as f:
            self.write(f,employees)

    def writeAirplanes(self, airplanes):
        with open("data/airplaines.csv", "w+") as f:
            self.write(f,airplanes)

    def writeVoyages(self, voyages):
        with open("data/voyages.csv", "w+") as f:
            self.write(f,voyages)

    def writeDestinations(self, destinations):
        with open("data/destinations.csv", "w+") as f:
            self.write(f,destinations)

    def writeFlight(self, flights):
        with open("data/flight.csv","w+") as f:
            self.write(f,flights)

    def readAirplane(self):
        with open("data/aircraft.csv", "r") as f:
            csv_reader = csv.DictReader(f)
            planes = []
            for row in csv_reader:
                plane = Airplane(
                    row["id"],
                    row["type"],
                    row["model"],
                    row["maker"],
                    row["nrseats"])
                planes.append(plane)
        return Collection(planes)

    def readEmployee(self):
        with open("data/employees.csv") as f:
            csv_reader = csv.DictReader(f)
            employees = []
            for row in csv_reader:
                employee = Employee(
                    row["name"],
                    row["ssn"],
                    row["address"],
                    row["mobile"],
                    row["email"],
                    row["ranl"],
                    row["license"])
                employees.append(employee)
        return Collection(employees)

    def readDestination(self):
        with open("data/destinations.csv") as f:
            csv_reader = csv.DictReader(f)
            destinations = []
            for row in csv_reader:
                destination = Destination(
                    row["airportID"],
                    row["country"],
                    row["airport"],
                    row["flightTime"],
                    row["distance"],
                    row["contactName"],
                    row["contactNr"])
                destinations.append(destination)
        return Collection(destinations)

    def readFlight(self):
        with open("data/flight.csv") as f:
            csv_reader = csv.DictReader(f)
            flights = []
            for row in csv_reader:
                flight = Flight(
                    row["airplane"],
                    row["destination"],
                    row["departure"],
                    row["flightNr"])
                flights.append(flight)
        return Collection(flights)

    def readVoyage(self):
        with open("data/voyage.csv") as f:
            csv_reader = csv.DictReader(f)
            voyages = []
            for row in csv_reader:
                voyage = Voyage(
                    row["seatSold"],
                    row["outFlight"],
                    row["returnFlight"],
                    row["flightCaptain"],
                    row["flightAssistant"],
                    row["headAttendant"],
                    row["flightAttendants"])
                voyages.append(voyage)
        return Collection(voyages)

    def read(self):
        #runs every read function in the right order
        #returns a dictionary of the collections
        return {"airplanes": self.readAirplane(),
            "employees": self.readEmployee(),
            "destinations": self.readDestination(),
            "flights": self.readFlight(),
            "voyages": self.readVoyage()}