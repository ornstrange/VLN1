class Employee:
    def __init__(self, name, ssn, address, mobile, email, rank, license = False):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.mobile = mobile
        self.email = email
        self.rank = rank
        self.license = license


    def __str__(self):
        # csv representation
        employeeDict = vars(self)
        valuesStr = [str(x) for x in employeeDict.values()]
        return ",".join(valuesStr)

    def __repr__(self):
        # debug repr
        output = "Employee: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"