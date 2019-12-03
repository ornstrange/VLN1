class Airplane:
    #def __init__(self, id, type, model,nrSeats,emptyWeight, maxTakeOffWeight, unitThrust, serviceCeiling, length, height, wingspan):
    def __init__(self, id, type, model, maker, nrSeats):
        self.id = id
        self.type = type
        self.model = model
        self.maker = maker
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
        airplaneDict = vars(self)
        valuesStr = [str(x) for x in airplaneDict.values()]
        return ",".join(valuesStr)

    def __repr__(self):
        # debug repr
        output = "Airplane: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"

