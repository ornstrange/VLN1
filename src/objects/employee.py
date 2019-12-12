class Employee:
    name = "employee"

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

    def header(self):
        return ",".join(vars(self))

    def fieldsRules(self):
        return [
            ("name",
             "Name (ex. Paul Johnson)",
             "([A-Z][a-z]+\s[A-Z][a-z]+)"),
            ("ssn",
             "Social Security Number (ex. 1910952789)",
             "\d{10}"),
            ("address",
             "Address (ex. Midgard 5)",
             "([A-Z][a-z]+\s\d+)"),
            ("mobile",
             "Mobile number (ex. 8689243)",
             "\d{7}"),
            ("email",
             "Email address (ex. not@real.com)",
             "([a-z]+@[a-z]+\.[a-z]+)"),
            ("rank",
             "Rank (ex. Captain / Pilot / Service Manager)",
             "[a-zA-Z]+"),
            ("license",
             "Airplane license (ex. 737Max), not for flight attendants",
             "[a-ZA-Z]*")
        ]
