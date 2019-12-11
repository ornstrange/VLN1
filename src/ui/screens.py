import curses
from curses import A_BOLD, A_REVERSE, A_NORMAL, A_DIM


class Screen:
    def __init__(self, parent, height, width):
        self.parent = parent
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width)
        self.window.keypad(True)
        self.collection = None
        self.name = None

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
        self.clear()
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
                self.window.addstr(text, A_BOLD)
            else:
                self.window.addstr(text)
        self.window.refresh()

    def go(self):
        # return the screen of the selected entry
        return self.entries[self.selected][1]


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
        self.window.refresh()

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
        self.selected = 0
        self.page = 0
        self.pages = []
        self.maxPage = 0

    def draw(self):
        # draws entries, with filter, sort and view options
        # and selected entry highlighted
        self.window.clear()
        self.window.box()

        fields = self.fields()
        fieldWidth = (self.width - 2) // len(fields)

        for i, key in enumerate(fields):
            self.window.move(1, (fieldWidth*i) + 1)
            self.window.addstr(f"{key:^{fieldWidth}}")
            self.window.move(1, (fieldWidth*i))
            self.window.addch(curses.ACS_VLINE)
        self.window.hline(2,1,curses.ACS_HLINE,self.width - 2)

        self.splitPages()
        for i, entry in enumerate(self.pages[self.page]):
            attr = A_BOLD | A_REVERSE if self.selected == i else A_DIM
            self.window.move((i*2)+3, 1)
            self.window.addstr(str(entry), attr)
            self.window.hline((i*2)+4, 1,curses.ACS_HLINE,self.width - 2)
        self.window.refresh()

    def splitPages(self):
        # split collection to pages
        self.pages = []
        for i in range(0, len(self.collection.all), (self.height - 4) // 2):
            self.pages.append(self.collection[i:i+(self.height - 4)//2])
        self.maxPage = len(self.pages) - 1

    def filterOptions(self):
        # get possible filter options
        pass

    def sortOptions(self):
        # get possible sort options
        pass

    def select(self):
        # returns the screen with selected object passed to it
        pass

    def fields(self):
        # returns a list of fields to use in header
        return list(vars(self.collection[0]).keys())

