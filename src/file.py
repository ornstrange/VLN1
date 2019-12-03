class File:
    def writeEmployees(self, employees):
        with open("data/employees.csv", "w+") as f:
            # header row
            f.write("name,ssn,address,landline,mobile,email,rank,role\n")
            # data rows
            for e in employees:
                f.write(f"{e.name},{e.ssn},{e.address},{e.landline},{e.mobile},{e.email},{e.rank},{e.role}\n")

    def writeAirplanes(self, airplanes):
        with open("data/airplaines.csv", "w+") as f:
            #header row
            f.write("id,type,maker,nrSeats\n")
            #data rows
            for e in airplanes:
                f.write(f"{e.id},{e.type},{e.planeInsignia},{e.model}, {e.nrSeats},{e.emptyweight},{e.maxTakeOffWeight},{e.unitThrust},{e.serviceCeiling},{e.length},{e.height},{e.wingspan}\n")

    def writeVoyages(self, voyages):
        with open("data/voyages.csv", "w+") as f:
            #header row
            f.write("seatSold,outFlight,returnFlight,flightCaptain,flightAssistant,headAttendant,flightAttendants\n")
            #data rows
            for e in voyages:
                f.write(f"{e.seatSold},{e.outFlight}, {e.returnFlight}, {e.flightCaptain}, {e.flightAssistant}, {e.headAttentant}, {e.flightAttendants}\n")

    def writeDestinations(selfself, destinations):
        with open("data/destinaiton.csv", "w+") as f:
            #header row
            f.write(f"country,airport,flightTime,distance,contactName,contactNr\n")
            #data rows
            for e in destinations:
                f.write(f"{e.country},{e.airport},{e.flightTime},{e.distance}, {e.contactName}, {e.contactNr}\n")

