from copy import deepcopy
import re

class Collection:
    def __init__(self, data, name):
        self.all = data
        self.name = name

    def __getitem__(self, index):
        return self.all[index]

    def sort(self, key):
        # sorts a list using key
        try:
            self.all = sorted(self.all, key=lambda x: vars(x)[key])
            return self
        except KeyError:
            return self

    def filterKeyVal(self, key, val, arr):
        # filters a list using key, value
        try:
            return list(filter(lambda x: vars(x)[key] == val, arr))
        except (KeyError, ValueError):
            return None

    def filterDate(self, begin, end, arr):
        # filters a list using a begin and end date
        try:
            return list(filter(lambda x: begin <= x.outflight.departure <= end, arr))
        except (ValueError, KeyError):
            return None

    def filterRegex(self, key, reg, arr):
        # filters a list using a key, bla
        try:
            return list(filter(lambda x: re.search(reg, vars(x)[key]),arr))
        except (KeyError, ValueError):
            return None
    def filter(self, *args):
        # filters all elements using a list of
        # (key, value) tuples
        filtered = deepcopy(self.all)
        try:
            for op, key, val in args:
                if op == "d":
                    begin, end = key, val
                    filtered = self.filterDate(begin, end, filtered)
                elif op == "?":
                    reg = val
                    filtered = self.filterRegex(key, reg, filtered)
                elif op == "=":
                    filtered = self.filterKeyVal(key, val, filtered)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            if len(filtered) == 1:
                return filtered[0]
            else:
                return Collection(filtered, self.name)
        except (KeyError, ValueError):
            return None

