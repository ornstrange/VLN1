# test purposes
from airplane import Airplane


class Collection:
    def __init__(self, data):
        self.all = data

    def sort(self, key):
        try:
            return sorted(self.all, key=lambda x: vars(x)[key])
        except KeyError:
            return self.all

    def filterKeyVal(self, arr, key, val):
        # filters a list using key, value
        try:
            return list(filter(lambda x: vars(x)[key] == val, arr))
        except (KeyError, ValueError):
            return None

    def filter(self, *args):
        # filters all elements using a list of
        # (key, value) tuples
        filtered = self.all
        try:
            for key, val in args:
                filtered = self.filterKeyVal(filtered, key, val)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            return filtered
        except (KeyError, ValueError):
            return None

# Tests
planes = Collection([
    Airplane(5,"a","b",10),
    Airplane(1,"c","d",20),
    Airplane(10,"p","b",50)])

print(planes.all)
print(planes.sort("id"))
print(planes.sort("type"))
print(planes.filter(("id",5)))
print(planes.filter(("model","b")))

