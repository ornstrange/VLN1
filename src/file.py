class File:
    def write(self, arr):
        # header row
        header = vars(arr[0])
        f.write(",".join(list(header.keys())))
        # data rows
        for e in employees:
            f.write(str(e))

    def writeEmployees(self, employees):
        with open("data/employees.csv", "w+") as f:
            self.write(employees)

    def writeAirplanes(self, airplanes):
        with open("data/airplaines.csv", "w+") as f:
            self.write(airplanes)

    def writeVoyages(self, voyages):
        with open("data/voyages.csv", "w+") as f:
            self.write(voyages)

    def writeDestinations(self, destinations):
        with open("data/destinations.csv", "w+") as f:
            self.write(destinations)

