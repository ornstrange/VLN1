import curses


class Screen:
    def __init__(self, parent, height, width):
        self.parent = parent
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width)
        self.window.keypad(True)
        self.collection = None
        self.mainMenu = False # shitmix

    def center(self, termHeight, termWidth):
        self.window.mvwin(termHeight // 2 - self.height // 2,
                          termWidth // 2 - self.width // 2)

    def clear(self):
        self.window.clear()
        self.window.refresh()


class Menu(Screen):
    type = "menu"

    def __init__(self, parent, height, width):
        super().__init__(parent, height, width)
        self.entries = None # {"entry": screen}
        self.selected = 0

    def draw(self):
        # draws menu with selected entry highlighted
        self.window.clear()
        self.window.box()

        center = self.width // 2

        for i, entry in enumerate(self.entries):
            text = entry[0]
            if self.collection:
                text = text.replace("*", type(self.collection[0]).__name__.lower())
            if self.selected == i:
                text = "> " + text + " <"
            offset = center - (len(text) // 2)
            self.window.move(i + 2, offset)
            if self.selected == i:
                self.window.addstr(text, curses.A_BOLD)
            else:
                self.window.addstr(text)

    def go(self):
        # return the screen of the selected entry
        return self.entries[self.selected]


class Input(Screen):
    type = "input"

    def __init__(self, parent, height, width):
        super().__init__(parent, height, width)
        self.fields = None
        self.rules = None
        self.finished = None

    def draw(self):
        self.window.clear()
        self.window.box()
        self.window.addstr(5, 5, "I am input window yes")

    def check(self):
        # check if all fields are filled and correct
        pass

    def checkField(self, field, rule):
        # check if field is filled and follows rule
        pass

    def change(self, entry):
        # change existing object
        pass

    def add(self):
        # add new object to collection
        pass


class List(Screen):
    type = "list"

    def __init__(self, parent, height, width):
        super().__init__(parent, height, width)
        self.onSelect = None
        self.entries = None
        self.selected = 0

    def draw(self):
        # draws entries, with filter, sort and view options
        # and selected entry highlighted
        self.window.clear()
        self.window.box()

    def filterOptions(self):
        # get possible filter options
        pass

    def sortOptions(self):
        # get possible sort options
        pass

    def select(self):
        # returns the screen with selected object passed to it
        pass

