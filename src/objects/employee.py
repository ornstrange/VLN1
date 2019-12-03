class Employee:
    def __init__(self, name, ssn, address, landline, mobile, email, rank, License):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.email = email
        self.rank = rank
        self.license = License

    def __str__(self):
        # csv representation
        output = ""
        empDict = vars(self)
        for val in empDict.values():
            output += f"{val},"
        return output[:-1] # strip last comma

