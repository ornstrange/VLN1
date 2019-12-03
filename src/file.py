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

