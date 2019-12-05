from copy import deepcopy

class Collection:
    def __init__(self, data):
        self.all = data

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

    def filter(self, *args):
        # filters all elements using a list of
        # (key, value) tuples
        filtered = deepcopy(self.all)
        try:
            for key, val in args:
                if type(key).__name__ == "datetime":
                    begin, end = key, val
                    filtered = self.filterDate(begin, end, filtered)
                else:
                    filtered = self.filterKeyVal(key, val, filtered)
                if not filtered:
                    # No match, dont bother continuing
                    return None
            return filtered if len(filtered) > 1 else filtered[0]
        except (KeyError, ValueError):
            return None


