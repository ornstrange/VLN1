from curses import KEY_UP, KEY_DOWN

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

        # init main menu and current window
        self.main.mainMenu = True
        self.current = self.main

    def __call__(self):
        # idno
        return self.current

    def draw(self):
        self().draw()

    def parseKey(self):
        keyInt = self().window.getch()

        if self().type == "menu":
            self.parseKeyMenu(keyInt)
        elif self().type == "input":
            self.parseKeyInput(keyInt)
        elif self().type == "list":
            self.parseKeyList(keyInt)

    def parseKeyMenu(self, keyInt):
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(self().entries))
            direction = 1 if keyInt == KEY_DOWN else -1
            if self().selected + direction in safeRange:
                self().selected += direction
        elif keyInt == ord("\n"): # enter pressed
            if self.current.entries[self().selected][1]:
                self.changeScreen(self().entries[self().selected])
            else: # go back
                self.current = self().parent

    def parseKeyMain(self, all_collections):
        keyInt = self().window.getch()
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(self().entries))
            direction = 1 if keyInt == KEY_DOWN else -1
            if self().selected + direction in safeRange:
                self().selected += direction
        elif keyInt == ord("\n"): # enter pressed
            if self().entries[self().selected][1]:
                curCollectionStr = self().entries[self().selected][0]
                curCollection = all_collections[curCollectionStr.lower()]
                self().collection = curCollection
                self.changeScreen(self().entries[self().selected])
            else: # go back
                exit()

    def changeScreen(self, newScreen):
        # later element of tuple is the screen
        newScreen = newScreen[1]
        # clear current screen
        self.current.clear()
        # pass collection down to next screen
        newScreen.collection = self.current.collection
        self.current = newScreen
        self.current.selected = 0
        self.current.window.keypad(True)

