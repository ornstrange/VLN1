class Airplane:
    def __init__(self, id, type, maker, nrSeats):
        self.id = id
        self.type = type
        self.maker = maker
        self.nrSeats = nrSeats

    def __str__(self):
        return f"AIRPLANE: [{self.id}, {self.type}, {self.maker}, {self.nrSeats}]"

    def __repr__(self):
        return self.__str__()
