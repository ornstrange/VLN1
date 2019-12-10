import curses as cur

from .screens import Menu, Input, List

MENUWIDTH = 37
EDITWIDTH = 40

class Interface:
    def __init__(self, stdscr):
        self.base = stdscr
        terH, terW = self.base.getmaxyx()

        # setting up screens with parents
        self.main = Menu(None, 9, MENUWIDTH)
        self.sub = Menu(self.main, 7, MENUWIDTH)
        self.add = Input(self.sub, 18, EDITWIDTH)
        self.addVoyage = Menu(self.sub, 7, MENUWIDTH)
        self.view = Menu(self.sub, 7, MENUWIDTH)
        self.find = Input(self.sub, 18, EDITWIDTH)
        self.list = List(self.view, terH, terW)

        # populating menu entries
        self.main.entries = [("Voyages", self.sub),
                             ("Destinations", self.sub),
                             ("Employees", self.sub),
                             ("Airplanes", self.sub),
                             ("Quit", None)]
        self.sub.entries = [("Register new *", self.add),
                            ("View or edit *s", self.view),
                            ("Go back", None)]
        self.addVoyage.entries = [("Copy from previous voyage", self.find),
                                  ("Create new", self.add),
                                  ("Go back", None)]
        self.view.entries = [("View all *s", self.list),
                             ("Find a specific *", self.find),
                             ("Go back", None)]

