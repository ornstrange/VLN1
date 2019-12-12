from curses import KEY_UP, KEY_DOWN, KEY_EXIT
from curses.ascii import ESC

from .screens import Menu, Input, List
#from screens import Menu, Input, List

class Interface:
    def __init__(self, screenHeight, screenWidth):
        self.running = True

        # setting up screens with parents and size
        main = Menu(None, 9)
        sub = Menu(main, 7)
        subVoy = Menu(main, 7)
        add = Input(sub, 18)
        addVoy = Menu(sub, 8)
        view = Menu(sub, 7)
        find = Input(sub, 18)
        edit = Input(find, 18)
        _list = List(view, screenHeight, screenWidth)
        voySelMan = List(addVoy, screenHeight, screenWidth)
        airSelVoy = List(addVoy, screenHeight, screenWidth)
        empSelVoy = List(addVoy, screenHeight, screenWidth)
        voySelCopy = List(addVoy, screenHeight, screenWidth)

        self.screens = {
            "main": main,
            "sub": sub,
            "subVoy": subVoy,
            "add": add,
            "addVoy": addVoy,
            "view": view,
            "find": find,
            "edit": edit,
            "list": _list,
            "voySelMan": voySelMan,
            "airSelVoy": airSelVoy,
            "empSelAdd": empSelVoy,
            "voySelCopy": voySelCopy
        }

        # populating menu entries
        self["main"].entries = [("Voyages", self["subVoy"]),
                                ("Destinations", self["sub"]),
                                ("Employees", self["sub"]),
                                ("Airplanes", self["sub"]),
                                ("Quit", None)]
        self["sub"].entries = [("Register new *", self["add"]),
                               ("View or edit *s", self["view"]),
                               ("Go back", None)]
        self["subVoy"].entries = [("Register new voyage", self["addVoy"]),
                               ("View or edit voyages", self["view"]),
                               ("Go back", None)]
        self["addVoy"].entries = [("Create new", self["add"]),
                                  ("Copy from previous voyage", self["find"]),
                                  ("Populate unmanned voyage", self["list"]),
                                  ("Go back", None)]
        self["view"].entries = [("View all *s", self["list"]),
                                ("Find a specific *", self["find"]),
                                ("Go back", None)]

        # centering all screens
        for key in self.screens:
            self[key].center(screenHeight, screenWidth)

        # init menu names and current window
        self.current = self["main"]

    def __getitem__(self, key):
        return self.screens[key]

    def draw(self):
        self.current.draw()

    def parseKey(self):
        keyInt = self.current.window.getch()

        if self.current.type == "menu":
            self.parseKeyMenu(keyInt)
        elif self.current.type == "input":
            self.parseKeyInput(keyInt)
        elif self.current.type == "list":
            self.parseKeyList(keyInt)

    def parseKeyMenu(self, keyInt):
        selected = self.current.selected
        if keyInt in [KEY_UP, KEY_DOWN]:
            self.traverseMenu(keyInt)
        elif keyInt == ord("\n"): # enter pressed
            if self.current.at():
                self.changeScreen(self.current.at())
            else: # go back
                self.changeScreen(self.current.parent)

    def parseKeyMainMenu(self, all_collections):
        keyInt = self.current.window.getch()
        if keyInt in [KEY_UP, KEY_DOWN]:
            self.traverseMenu(keyInt)
        elif keyInt == ord("\n"): # enter pressed
            if self.current.at():
                collectionStr = self.current.entries[self.current.selected][0]
                collection = all_collections[collectionStr.lower()]
                self.current.collection = collection
                self.changeScreen(self.current.at())
            else: # go back
                self.running = False

    def traverseMenu(self, keyInt):
        safeRange = range(len(self.current.entries))
        direction = 1 if keyInt == KEY_DOWN else -1
        if self.current.selected + direction in safeRange:
            self.current.selected += direction

    def parseKeyList(self, keyInt):
        current = self.current
        selected = current.selected
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(current.pages[current.page]))
            direction = 1 if keyInt == KEY_DOWN else -1
            if selected + direction in safeRange:
                self.current.selected += direction
            elif selected + direction == -1:
                if current.page != 0:
                    self.current.page -= 1 if current.page else 0
                    self.current.selected = len(current.pages[current.page]) - 1
            elif current.page != current.maxPage:
                self.current.page += 1
                self.current.selected = 0
        elif keyInt in [ord("e"), ord("f"), ord("s"), ord("v")]:
            self.current.tabActive = chr(keyInt)
        elif keyInt == ord("q"):
            self.changeScreen(self.current.parent)
        elif keyInt == ord("\n"): # enter pressed
            self.current.at()

    def changeScreen(self, newScreen):
        # clear current screen
        self.current.clear()
        # pass collection down to next screen
        newScreen.collection = self.current.collection
        self.current = newScreen
        if self.current.type in ["menu", "list"]:
            self.current.selected = 0
        if self.current.type == "list":
            self.current.page = 0

