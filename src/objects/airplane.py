class Airplane:
    def __init__(self, id, type, planeInsignia, model,nrSeats,emptyWeight, maxTakeOffWeight, unitThrust, serviceCeiling, length, height, wingspan):
        self.id = id
        self.type = type
        self.planeInsignia = planeInsignia
        self.model = model
        self.nrSeats = nrSeats
        self.emptyWeight = emptyWeight
        self.maxTakeOffWeight = maxTakeOffWeight
        self.unitThrust = unitThrust
        self.serviceCeiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan

    def __str__(self):
        return f"AIRPLANE: [{self.id}, {self.type}, {self.planeInsignia},{self.model},{self.nrSeats},{self.emptyWeight},{self.maxTakeOffWeight},{self.unitThrust},{self.serviceCeiling},{self.length},{self.height},{self.wingspan}]"

    def __repr__(self):
        return self.__str__()

