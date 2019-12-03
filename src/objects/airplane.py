class Airplane:
    #def __init__(self, id, type, model,nrSeats,emptyWeight, maxTakeOffWeight, unitThrust, serviceCeiling, length, height, wingspan):
    def __init__(self, id, type, model, nrSeats):
        self.id = id
        self.type = type
        self.model = model
        self.nrSeats = nrSeats
        #self.emptyWeight = emptyWeight
        #self.maxTakeOffWeight = maxTakeOffWeight
        #self.unitThrust = unitThrust
        #self.serviceCeiling = serviceCeiling
        #self.length = length
        #self.height = height
        #self.wingspan = wingspan

    def __str__(self):
        # csv representation
        output = ""
        airplaneDict = vars(self)
        for val in airplaneDict.values():
            output += f"{val},"
        return output[:-1] # strip last comma

    def __repr__(self):
        # debug repr
        output = "Airplane: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"

