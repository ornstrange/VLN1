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
            return sorted(arr, key=lambda x: vars(x)[key])
        except KeyError:
            return arr

    def filterKeyVal(self, key, val, arr):
        # filters a list using key, value
        try:
            return list(filter(lambda x: vars(x)[key] == val, arr))
        except (KeyError, ValueError):
            return None

    def filterDate(self, begin, end, arr):
        # filters a list using a begin and end date
        try:
            return list(filter(lambda x: begin <= x.departure <= end, arr))
        except (ValueError, KeyError):
            return None

    def filterRegex(self, key, reg, arr):
        # filters a list using a key, bla
        try:
            return list(filter(lambda x: vars(x)re.compile(reg).search == key, arr))
        except:
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
                    filtered = self.filterRegex(key, val, filtered)
                elif op == "=":
                    filtered = self.filterKeyVal(key, val, filtered)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            return filtered if len(filtered) > 1 else filtered[0]
        except (KeyError, ValueError):
            return None

