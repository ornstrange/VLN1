class Airplane:
    name = "airplane"

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

    def fieldsRules(self):
        return [
            ("id",
             "Identification Number (TF-***)",
             "TF-[A-Z]{3}"),
            ("type",
             "Type of airplane (ex. 737Max)",
             ".+"),
            ("model",
             "Airplane model (ex. 737)",
             ".+"),
            ("maker",
             "Manufacturer (ex. Boeing)",
             ".+"),
            ("nrSeats",
             "Number of seats (ex. 55)",
             "\d+")
        ]

