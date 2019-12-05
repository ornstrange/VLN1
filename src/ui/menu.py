import curses

class Menus:
    main = ["Voyages", "Destinations", "Employees", "Airplanes", "Exit"]
    sub = ["Add new", "View", "Go back"]
    newVoyage = ["All new", "Use existing", "Go back"]
    view = ["View all", "Search", "Go back"]

    def __init__(self):
        self.tl = bytes(curses.ACS_ULCORNER).decode("utf-8")
        self.tr = bytes(curses.ACS_URCORNER).decode("utf-8")
        self.bl = bytes(curses.ACS_LLCORNER).decode("utf-8")
        self.br = bytes(curses.ACS_LRCORNER).decode("utf-8")
        self.hl = bytes(curses.ACS_HLINE).decode("utf-8")
        self.vl = bytes(curses.ACS_VLINE).decode("utf-8")
        self.tt = bytes(curses.ACS_TTEE).decode("utf-8")
        self.lt = bytes(curses.ACS_LTEE).decode("utf-8")
        self.rt = bytes(curses.ACS_RTEE).decode("utf-8")
        self.ct = bytes(curses.ACS_PLUS).decode("utf-8")
        self.bt = bytes(curses.ACS_BTEE).decode("utf-8")

    def topLine(self, size):
        return self.tl + self.hl * (size-2) + self.tr

    def botLine(self, size):
        return self.bl + self.hl * (size-2) + self.br

