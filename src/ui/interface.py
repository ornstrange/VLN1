from curses import KEY_UP, KEY_DOWN

from .screens import Menu, Input, List

MENUWIDTH = 37
EDITWIDTH = 40

class Interface:
    def __init__(self, screenHeight, screenWidth):
        self.running = True

        # setting up screens with parents
        self.main = Menu(None, 9, MENUWIDTH)
        self.sub = Menu(self.main, 7, MENUWIDTH)
        self.add = Input(self.sub, 18, EDITWIDTH)
        self.addVoyage = Menu(self.sub, 8, MENUWIDTH)
        self.view = Menu(self.sub, 7, MENUWIDTH)
        self.find = Input(self.sub, 18, EDITWIDTH)
        self.list = List(self.view, screenHeight, screenWidth)

        # populating menu entries
        self.main.entries = [("Voyages", self.sub),
                             ("Destinations", self.sub),
                             ("Employees", self.sub),
                             ("Airplanes", self.sub),
                             ("Quit", None)]
        self.sub.entries = [("Register new *", self.add),
                            ("View or edit *s", self.view),
                            ("Go back", None)]
        self.addVoyage.entries = [("Create new", self.add),
                                  ("Copy from previous voyage", self.find),
                                  ("Populate unmanned voyage", self.list),
                                  ("Go back", None)]
        self.view.entries = [("View all *s", self.list),
                             ("Find a specific *", self.find),
                             ("Go back", None)]

        # centering all screens
        self.main.center(screenHeight, screenWidth)
        self.sub.center(screenHeight, screenWidth)
        self.add.center(screenHeight, screenWidth)
        self.addVoyage.center(screenHeight, screenWidth)
        self.view.center(screenHeight, screenWidth)
        self.find.center(screenHeight, screenWidth)
        self.list.center(screenHeight, screenWidth)

        # init menu names and current window
        self.main.name = "main menu"
        self.sub.name = "sub menu"
        self.add.name = "add"
        self.current = self.main

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
            safeRange = range(len(self.current.entries))
            direction = 1 if keyInt == KEY_DOWN else -1
            if selected + direction in safeRange:
                self.current.selected += direction
        elif keyInt == ord("\n"): # enter pressed
            if self.current.entries[selected][1]:
                name = self.current.entries[selected][1].name
                colType = self.current.collection.name
                if name == "add" and colType == "voyages":
                    self.changeScreen(self.addVoyage)
                else:
                    self.changeScreen(self.current.go())
            else: # go back
                self.changeScreen(self.current.parent)

    def parseKeyMainMenu(self, all_collections):
        keyInt = self.current.window.getch()
        if keyInt in [KEY_UP, KEY_DOWN]:
            safeRange = range(len(self.current.entries))
            direction = 1 if keyInt == KEY_DOWN else -1
            if self.current.selected + direction in safeRange:
                self.current.selected += direction
        elif keyInt == ord("\n"): # enter pressed
            if self.current.go():
                collectionStr = self.current.entries[self.current.selected][0]
                collection = all_collections[collectionStr.lower()]
                self.current.collection = collection
                self.changeScreen(self.current.go())
            else: # go back
                self.running = False

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

        elif keyInt == ord("\n"): # enter pressed
            pass

    def changeScreen(self, newScreen):
        # clear current screen
        self.current.clear()
        # pass collection down to next screen
        newScreen.collection = self.current.collection
        self.current = newScreen
        if self.current.type == "menu":
            self.current.selected = 0

