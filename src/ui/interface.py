from curses import KEY_UP, KEY_DOWN, KEY_EXIT, curs_set
from curses.ascii import ESC

from .screens import Menu, Input, List
#from screens import Menu, Input, List

class Interface:
    def __init__(self, screenHeight, screenWidth):
        self.running = True

        # setting up screens with parents, children and size
        main = Menu(None, 9)
        sub = Menu(main, 7)
        subVoy = Menu(main, 7)
        add = Input(sub, finished=sub)
        addVoyMenu = Menu(sub, 8)
        view = Menu(sub, 7)
        _list = List(view, screenHeight, screenWidth, view)
        find = Input(sub, finished=_list)
        edit = Input(find, finished=view)
        empSelVoy = List(addVoyMenu, screenHeight, screenWidth)
        manVoy = Input(empSelVoy, finished=addVoyMenu)
        empSelVoy.onSelect = manVoy
        voySelMan = List(addVoyMenu, screenHeight, screenWidth, manVoy)
        addVoy = Input(addVoyMenu)
        airSelVoy = List(addVoy, screenHeight, screenWidth, addVoyMenu)
        addVoy.finished = airSelVoy
        voySelCopy = List(addVoyMenu, screenHeight, screenWidth, addVoy)

        self.screens = {
            "main": main,
            "sub": sub,
            "subVoy": subVoy,
            "add": add,
            "addVoy": addVoy,
            "addVoyMenu": addVoyMenu,
            "view": view,
            "find": find,
            "edit": edit,
            "list": _list,
            "manVoy": manVoy,
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
        self["subVoy"].entries = [("Register new voyage", self["addVoyMenu"]),
                               ("View or edit voyages", self["view"]),
                               ("Go back", None)]
        self["addVoyMenu"].entries = [("Create new", self["addVoy"]),
                                  ("Copy from previous voyage", self["voySelCopy"]),
                                  ("Populate unmanned voyage", self["voySelMan"]),
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
        nextScreen = self.current.at()
        collection = self.current.collection
        if keyInt in [KEY_UP, KEY_DOWN]:
            self.traverseMenu(keyInt)
        elif keyInt == ord("\n"): # enter pressed
            if nextScreen:
                self.changeScreen(nextScreen)
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
    
    def parseKeyFilter(self, keyInt):
        current = self.current
        selected = current.selFilt
        if keyInt == ord("e"): # e pressed
            self.current.tabActive = "e"

    def parseKeySort(self, keyInt):
        current = self.current
        selected = current.selSort
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(current.fields()))
            direction = 1 if keyInt == KEY_DOWN else -1
            if selected + direction in safeRange:
                self.current.selSort += direction
        elif keyInt == ord("\n"): # enter pressed
            self.current.collection =self.current.collection.sort(self.current.fields()[self.current.selSort])
            self.current.tabActive = "e"
        elif keyInt == ord("e"): # e pressed
            self.current.tabActive = "e"

    def parseKeyList(self, keyInt):
        current = self.current
        selected = current.selected
        if current.tabActive == "s":
            self.parseKeySort(keyInt)
            return
        if current.tabActive == "f":
            self.parseKeyFilter(keyInt)
            return
        elif keyInt in [KEY_UP, KEY_DOWN]:
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
        elif keyInt in [ord("e"), ord("s"), ord("f"), ord("v")]:
            self.current.tabActive = chr(keyInt)
        elif keyInt == ord("q"):
            self.changeScreen(self.current.parent)
        elif keyInt == ord("\n"): # enter pressed
            self.current.at()

    def parseKeyInput(self, keyInt):
        selected = self.current.selected
        if keyInt == ord("\n"):
            if selected != len(self.current.fields):
                self.current.editCurrentTextbox()
                return
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(self.current.fields) + 1)
            direction = 1 if keyInt == KEY_DOWN else -1
            if selected + direction in safeRange:
                self.current.selected += direction
        elif keyInt == ord("q"):
            self.changeScreen(self.current.parent)
        elif keyInt == ord("\n"):
            if selected == len(self.current.fields):
                if self.current == self["add"]:
                    self.current.add()
                self.changeScreen(self.current.finished)
            else:
                self.current.editCurrentTextbox()

    def changeScreen(self, newScreen):
        # clear current screen
        self.current.clear()
        # pass collection down to next screen
        newScreen.collection = self.current.collection
        self.current = newScreen
        self.current.selected = 0
        if self.current.type == "list":
            self.current.page = 0
            self.current.tabActive = "e"
            self.current.selSort = 0
            self.current.selFilt = 0
        elif self.current.type == "input":
            self.current.setupFields()

