class File:
    def writeEmployees(self, employees):
        with open("data/employees.csv", "w+") as f:
            # header row
            f.write("name,ssn,address,landline,mobile,email\n")
            # data rows
            for e in employees:
                f.write(f"{e.name},{e.ssn},{e.address},{e.landline},{e.mobile},{e.email}\n")

