import curses

class Menus:
    def __init__(self):
        self.main = ["Voyages", "Destinations", "Employees", "Airplanes", "Exit"]
        self.sub = ["Add new", "View", "Go back"]
        self.newVoyage = ["All new", "Copy existing", "Go back"]
        self.view = ["View all", "Search", "Go back"]

    def longest(self):
        return "\n".join(self.main)

