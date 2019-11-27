class Employee:
    def __init__(self, name, ssn, address, landline, mobile, email):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.email = email


class Pilot(Employee):
    def __init__(self, name, ssn, address, landline, mobile, email, license):
        super.__init__(name, ssn, address, landline, mobile, email)
        self.license = license


class FlightAttendant(Employee):
    def __init__(self, name, ssn, address, landline, mobile, email, rank):
        super.__init__(name, ssn, address, landline, mobile, email)
        self.rank = rank
