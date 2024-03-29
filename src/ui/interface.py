from curses import KEY_UP, KEY_DOWN, KEY_EXIT, curs_set
from curses.ascii import ESC

from objects.collection import Collection
from .screens import Menu, Input, List, Select, SelEmp

class Interface:
    def __init__(self, collections, screenHeight, screenWidth):
        self.running = True
        self.collections = collections

        # setting up screens with parents, children and size
        main = Menu(None, 9)
        sub = Menu(main, 7)
        subVoy = Menu(main, 7)
        add = Input(sub, finished=sub)
        addVoyMenu = Menu(sub, 8)
        #view = Menu(sub, 7)
        _list = List(sub, screenHeight, screenWidth)
        #find = Input(sub, finished=_list)
        edit = Input(_list, finished=sub)
        empSelVoy = Select(addVoyMenu, screenHeight, screenWidth)
        manVoy = SelEmp(empSelVoy, finished=addVoyMenu)
        voySelMan = Select(addVoyMenu, screenHeight, screenWidth, manVoy)
        desSelVoy = Select(addVoyMenu, screenHeight, screenWidth)
        airSelVoy = Select(desSelVoy, screenHeight, screenWidth)
        addVoy = Input(airSelVoy, finished=addVoyMenu)
        voySelCopy = Select(addVoyMenu, screenHeight, screenWidth, addVoy)

        # endpoints
        _list.onSelect = edit
        desSelVoy.onSelect = airSelVoy
        airSelVoy.onSelect = addVoy
        empSelVoy.onSelect = manVoy

        self.screens = {
            "main": main,
            "sub": sub,
            "subVoy": subVoy,
            "add": add,
            "addVoy": addVoy,
            "addVoyMenu": addVoyMenu,
            #"view": view,
            #"find": find,
            "edit": edit,
            "list": _list,
            "manVoy": manVoy,
            "voySelMan": voySelMan,
            "airSelVoy": airSelVoy,
            "empSelVoy": empSelVoy,
            "voySelCopy": voySelCopy,
            "desSelVoy": desSelVoy
        }

        # populating menu entries
        self["main"].entries = [("Voyages", self["subVoy"]),
                                ("Destinations", self["sub"]),
                                ("Employees", self["sub"]),
                                ("Airplanes", self["sub"]),
                                ("Quit", None)]
        self["sub"].entries = [("Register new *", self["add"]),
                               ("View or edit *s", self["list"]),
                               ("Go back", None)]
        self["subVoy"].entries = [("Register new voyage", self["addVoyMenu"]),
                               ("View or edit voyages", self["list"]),
                               ("Go back", None)]
        self["addVoyMenu"].entries = [("Create new", self["desSelVoy"]),
                                  ("Copy from previous voyage", self["voySelCopy"]),
                                  ("Populate unmanned voyage", self["voySelMan"]),
                                  ("Go back", None)]
        #self["view"].entries = [("View all *s", self["list"]),
        #                        ("Find a specific *", self["find"]),
        #                        ("Go back", None)]

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
        # select correct type
        if self.current.type == "menu":
            self.parseKeyMenu(keyInt)
        elif self.current.type == "input":
            self.parseKeyInput(keyInt)
        elif self.current.type == "list":
            self.parseKeyList(keyInt)
        elif self.current.type == "select":
            self.parseKeySelect(keyInt)
        elif self.current.type == "selEmp":
            self.parseKeySelEmp(keyInt)

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

    def traverseMenu(self, keyInt):
        safeRange = range(len(self.current.entries))
        direction = 1 if keyInt == KEY_DOWN else -1
        if self.current.selected + direction in safeRange:
            self.current.selected += direction

    def parseKeyList(self, keyInt):
        current = self.current
        if current.tabActive == "s":
            self.parseKeySort(keyInt)
            return
        if current.tabActive == "f":
            self.parseKeyFilter(keyInt)
            return
        elif keyInt in [KEY_UP, KEY_DOWN]:
            self.traverseList(keyInt)
        elif keyInt in [ord("e"), ord("s"), ord("f"), ord("v")]:
            self.current.tabActive = chr(keyInt)
        elif keyInt == ord("q"):
            self.changeScreen(self.current.parent)
        elif keyInt == ord("\n"): # enter pressed
            #self.current.setValue()
            self.changeScreen(self.current.onSelect)

    def parseKeySelect(self, keyInt):
        current = self.current
        if current.tabActive == "s":
            self.parseKeySort(keyInt)
            return
        if current.tabActive == "f":
            self.parseKeyFilter(keyInt)
            return
        elif keyInt in [KEY_UP, KEY_DOWN]:
            self.traverseList(keyInt)
        elif keyInt in [ord("e"), ord("s"), ord("f"), ord("v")]:
            self.current.tabActive = chr(keyInt)
        elif keyInt == ord("q"):
            self.changeScreen(self.current.parent)
        elif keyInt == ord("\n"): # enter pressed
            self.current.addValue()
            self.changeScreen(self.current.onSelect)

    def parseKeySort(self, keyInt):
        current = self.current
        selected = current.selSort
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(current.fields))
            direction = 1 if keyInt == KEY_DOWN else -1
            if selected + direction in safeRange:
                self.current.selSort += direction
        elif keyInt == ord("\n"): # enter pressed
            curField = self.current.currentSortField()
            sortedCollection = current.collection.sort(curField)
            self.current.collection = sortedCollection
            self.current.tabActive = "e"
        elif keyInt == ord("e"): # e pressed
            self.current.tabActive = "e"

    def parseKeyFilter(self, keyInt):
        current = self.current
        selected = self.current.selFilt
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(self.current.fields)+1)
            direction = 1 if keyInt == KEY_DOWN else -1
            if selected + direction in safeRange:
                self.current.selFilt += direction
        elif keyInt == ord("\n"):
            if selected != len(self.current.fields):
                self.current.editCurrentTextbox()
                return
            else:
                for key, test in current.fieldValues.items():
                    if test != "":
                        if " " in test:
                            test = test.split()
                            mytuple = ("d", key, test)
                            result = self.current.collection.filter(mytuple)
                            if result:
                                if type(result).__name__ != "Collection":
                                    name = type(result).__name__.lower() + "s"
                                    self.current.collection = Collection([result], name)
                                else:
                                    self.current.collection = result
                        else:
                            mytuple = ("?", key, test)
                            result = self.current.collection.filter(mytuple)
                            if result:
                                if type(result).__name__ != "Collection":
                                    name = type(result).__name__.lower() + "s"
                                    self.current.collection = Collection([result], name)
                                else:
                                    self.current.collection = result
                self.current.tabActive = "e"
        elif keyInt == ord("e"): # e pressed
            self.current.tabActive = "e"

    def traverseList(self, keyInt):
        current = self.current
        selected = current.selected
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
                if self.current.checkAllFields():
                    if self.current in [self["add"], self["addVoy"]]:
                        self.current.add()
                    self.changeScreen(self.current.finished)

    def parseKeySelEmp(self, keyInt):
        selected = self.current.selected
        if keyInt == ord("\n"):
            if selected != len(self.current.fields):
                self.changeScreen(self["empSelVoy"])
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
                if self.current.checkAllFields():
                    self.current.edit()
                    self.changeScreen(self.current.finished)

    def changeScreen(self, newScreen):
        # exit if newScreen is None
        if not newScreen:
            exit()
        # at main menu
        if self.current == self["main"]:
            collectionStr = self.current.entries[self.current.selected][0]
            self.current.collection = self.collections[collectionStr.lower()]
        # clear current screen
        self.current.clear()
        # pass collection down to next screen
        newScreen = self.passCollection(newScreen)
        # special cases
        newScreen = self.specialCases(newScreen)
        # change screen
        self.current = newScreen
        # init stuff
        self.current.selected = 0
        if self.current.type in ["list", "select"]:
            self.current.page = 0
            self.current.tabActive = "e"
            self.current.selSort = 0
            self.current.selFilt = 0
        if self.current.type == "list":
            self.current.fields = None
        elif self.current.type == "select":
            self.current.entry = None
        elif self.current.type == "input":
            self.current.setupFields()
        elif self.current == self["edit"]:
            newScreen.setValues()

    def passCollection(self, newScreen):
        # pass collection down to next screen
        if self.current.type == "select":
            if newScreen.type == "select":
                newScreen.saveCollection = self.current.saveCollection
            else:
                newScreen.collection = self.current.saveCollection
        else:
            if newScreen.type == "select":
                newScreen.saveCollection = self.current.collection
            else:
                newScreen.collection = self.current.collection
        return newScreen

    def specialCases(self, newScreen):
        # set collections
        if newScreen == self["desSelVoy"]:
            newScreen.collection = self.collections["destinations"]
        elif newScreen == self["airSelVoy"]:
            newScreen.value += self.current.value
            newScreen.collection = self.collections["airplanes"]
        elif newScreen == self["voySelMan"]:
            newScreen.collection = self.collections["voyages"]
        elif newScreen == self["empSelVoy"]:
            if self.current == self["manVoy"]:
                newScreen.currentField = self.current.currentField()
            newScreen.collection = self.collections["employees"]
        elif newScreen == self["addVoy"]:
            newScreen.fieldValues["destination"] = self.current.value[0]
            newScreen.fieldValues["airplane"] = self.current.value[1]
        elif newScreen == self["manVoy"]:
            if self.current == self["empSelVoy"]:
                newScreen.fieldValues[self.current.currentField] = self.current.getEntry()
            else:
                newScreen.setupFields()
                newScreen.entry = self.current.getEntry()
        elif newScreen == self["edit"]:
            newScreen.entry = self.current.getEntry()
        return newScreen

