class Airplane:
    def __init__(self, id, type, model, maker, nrSeats):
        self.id = id
        self.type = type
        self.model = model
        self.maker = maker
        self.nrSeats = nrSeats

    def __str__(self):
        # csv representation
        airplaneDict = vars(self)
        valuesStr = [str(x) for x in airplaneDict.values()]
        return ",".join(valuesStr)

    def header(self):
        return ",".join(vars(self))

    def __repr__(self):
        # debug repr
        output = "Airplane: ["
        items = vars(self)
        for key in items:
            output += f"{key}: {items[key]}, "
        return output.strip() + "]"

