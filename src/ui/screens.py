import curses

class Screen:
    def __init__(self, parent, height, width):
        self.parent = parent
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width)
        self.collection = None

class Menu(Screen):
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
            offset = center - (len(text) // 2)
            self.window.move(i + 2, offset)
            if self.selected == i:
                self.window.addstr(text, curses.A_NORMAL)
            else:
                self.window.addstr(text, curses.A_DIM)

    def go(self):
        # return the screen of the selected entry
        return self.entries[self.selected]

class Input(Screen):
    def __init__(self, parent, height, width):
        super().__init__(parent, height, width)
        self.fields = None
        self.rules = None
        self.finished = None

    def draw(self):
        # draws input fields, with data if there is any
        pass

    def check(self):
        # check if all fields are filled and correct
        pass

    def checkField(self, field, rule):
        # check if field is filled and follows rule
        pass

    def change(self, entry):
        # change existing object
        pass

    def add(self, collection):
        # add new object to collection
        pass


class List(Screen):
    def __init__(self, parent, height, width):
        super().__init__(parent, height, width)
        self.onSelect = None
        self.entries = None
        self.selected = 0

    def draw(self):
        # draws entries, with filter, sort and view options
        # and selected entry highlighted
        pass

    def filterOptions(self):
        # get possible filter options
        pass

    def sortOptions(self):
        # get possible sort options
        pass

    def select(self):
        # returns the screen with selected object passed to it
        pass

