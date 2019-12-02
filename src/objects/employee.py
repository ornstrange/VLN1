class Employee:
    def __init__(self, name, ssn, address, landline, mobile, email, rank, role):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.landline = landline 
        self.mobile = mobile
        self.email = email
        self.rank = rank
        self.role = role
        

class Pilot(Employee):
    def __init__(self, name, ssn, address, landline, mobile, email, rank, role, license):
        super().__init__(name, ssn, address, landline, mobile, email, rank, role)
        self.license = license

