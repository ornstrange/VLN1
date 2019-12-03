import csv
from objects/airplane import Airplane
from objects/employee import Employee
from objects/destination import Destination
from objects/flight import Flight
from objects/voyage import Voyage

class File:
    def write(self,f, arr):
        # header row
        header = vars(arr[0])
        f.write(",".join(list(header.keys())))
        # data rows
        for object in arr:
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

    def writeFlight(self, flight):
        with open("data/flight.csv","w+") as f:
            self.write(f,destinations)
        
    def readAirplane(self):
        with open("data/airplanes.csv", "r") as f:
            csv_reader = csv.DictReader(f,delimiter=",")
            planes = []
            for row in csv_reader:
                plane = Airplane(row[0],row[1],row[2],row[3],row[4])
                planes.append(plane)
        return planes
    
    def readEmployee(self):
        with open("data/employees.csv") as f:
            csv_reader = csv.DictReader(f,delimiter=",")
            employees = []
            for row in csv_reader:
                employee = Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                employees.append(empl)
        return employees
    
    def readDestination(self):
        with open("data/destinations.csv") as f:
            csv_reader = csv.DictReader(f,delimiter=",")
            destinations = []
            for row in csv_reader:
                destination = Destination(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                destinations.append(destination)
        return destinations
            
    def readFlight(self):
        with open("data/flight.csv") as f:
            csv_reader = csv.DictReader(f,delimiter=",")
            flights = []
            for row in csv_reader:
                flight = Flight(row[0],row[1],row[2],row[3],row[4])
                flights.append(flight)
        return flights

    def readVoyage(self):
        with open("data/voyage.csv") as f:
            csv_reader = csv.DictReader(f,delimiter=",")
            voyages = []
            for row in csv_reader:
                voyage = Voyage(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                voyages.append(voyage)
        return voyages




