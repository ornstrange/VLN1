import curses
from curses import A_BOLD, A_REVERSE, A_NORMAL, A_DIM
from curses.textpad import Textbox

MENUWIDTH = 37
EDITWIDTH = 64
EDITHEIGHT = 37

class Screen:
    def __init__(self, parent, height, width):
        self.parent = parent
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width)
        self.window.keypad(True)
        self.collection = None

    def center(self, termHeight, termWidth):
        self.y = termHeight // 2 - self.height // 2
        self.x = termWidth // 2 - self.width // 2
        self.window.mvwin(self.y, self.x)

    def clear(self):
        self.window.clear()
        self.window.refresh()

class Menu(Screen):
    type = "menu"

    def __init__(self, parent, height, width=MENUWIDTH):
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

    def at(self):
        # return the screen of the selected entry
        return self.entries[self.selected][1]


class Input(Screen):
    type = "input"

    def __init__(self, parent, height=EDITHEIGHT, width=EDITWIDTH, finished=None):
        super().__init__(parent, height, width)
        self.fields = None
        self.rules = None
        self.finished = finished
        self.textBoxes = {}
        self.selected = 7

    def draw(self):
        self.window.clear()
        self.window.box()
        self.window.refresh()

        # draw textboxes
        for key in self.textBoxes:
            box, win = self.textBoxes[key]
            win.box()
            win.refresh()
        # descriptions
        for i, field in enumerate(self.fields):
            desc = field[1]
            currentY = self.y + (i * 4)
            self.window.move(currentY, 3)
            self.window.addstr(desc)

        # confirm button
        attr = A_NORMAL
        output = "Confirm"
        if self.selected == len(self.fields):
            attr = A_BOLD | A_REVERSE
            output = "> Confirm <"
        self.window.addstr(self.y + self.height - 8,
                           self.width//2 - len(output)//2,
                           output, attr)

        # quit instructions
        self.window.addstr(self.y + self.height - 5,
                           3,
                           "(q) go back / cancel")

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

    def createTextbox(self):
        currentY = self.y + 3 + (len(self.textBoxes) * 4)
        _tempWin = curses.newwin(3, self.width - 4, currentY, self.x + 2)
        _tempWin.box()
        _tempWin.refresh()
        return (Textbox(_tempWin), _tempWin)

    def setupFields(self):
        # returns a list of fields to use in header
        self.textBoxes = {}
        firstObject = self.collection[0]
        self.fields = firstObject.fieldsRules()
        for name, desc, rule in self.fields:
            self.textBoxes[name] = self.createTextbox()


class List(Screen):
    type = "list"

    def __init__(self, parent, height, width, onSelect = None):
        super().__init__(parent, height, width)
        self.onSelect = onSelect
        self.selected = 0
        self.selSort = 0
        self.page = 0
        self.pages = []
        self.maxPage = 0
        self.tabs = {"e": "(e) Entries",
                     "f": "(f) Filter",
                     "s": "(s) Sort",
                     "v": "(v) View Options",
                     "q": "(q) Go back "}
        self.tabActive = "e"
        self.sortWin = curses.newwin(20, 50, 10, 63)



    def draw(self):
        # draws entries, with filter, sort and view options
        # and selected entry highlighted
        self.window.clear()
        self.drawHeader()
        self.drawEntries()
        self.drawTabs()
        self.window.box()
        self.window.refresh()
        if self.tabActive == "s":
            self.drawSort()
    
    def drawSort(self):
        self.sortWin.clear()
        self.sortWin.box()
        self.sortWin.addstr(16, 15, "(e) Entries / cancel")
        for i,field in enumerate(self.fields()):
            text = field
            if i == self.selSort:
                text = "> " + text + " <"
            offset = (49 - (len(text))) // 2
            self.sortWin.move(i + 5, offset)
            if self.selSort == i:
                self.sortWin.addstr(text, A_BOLD)
            else:
                self.sortWin.addstr(text)
        self.sortWin.refresh()

    def drawHeader(self):
        fields = self.fields()
        fieldWidth = (self.width - 2) // len(fields)
        for i, key in enumerate(fields):
            self.window.move(1, (fieldWidth*i) + 1)
            self.window.addstr(f"{key:^{fieldWidth}}")
            if i != 0:
                self.window.move(1, (fieldWidth*i) + 1)
            self.window.addch(curses.ACS_VLINE)
        self.window.hline(2,1,curses.ACS_HLINE,self.width - 2)

    def drawEntries(self):
        self.splitPages()
        for i, entry in enumerate(self.pages[self.page]):
            attr = A_BOLD | A_REVERSE if self.selected == i else A_NORMAL
            self.window.move((i*2)+3, 1)
            self.tabulate(i, entry, attr)
            self.window.hline((i*2)+4, 1,curses.ACS_HLINE,self.width - 2)

    def drawTabs(self):
        self.window.hline(self.height-3, 1,curses.ACS_HLINE,self.width - 2)
        tabWidth = (self.width-2)//len(self.tabs)
        for i, tab in enumerate(self.tabs.values()):
            offset = (tabWidth//2) - (len(tab)//2)
            self.window.move(self.height-2, i*tabWidth + offset)
            self.window.addstr(tab)

    def splitPages(self):
        # split collection to pages
        self.pages = []
        for i in range(0, len(self.collection.all), (self.height - 4) // 2):
            self.pages.append(self.collection[i:i+(self.height - 4)//2])
        self.maxPage = len(self.pages) - 1

    def tabulate(self, i, entry, attr):
        # outputs all entries, beautiful
        baseHeight = (i*2) + 3
        items = vars(entry).items()
        fieldWidth = (self.width - 2) // len(items)
        for i, item in enumerate(items):
            key, val = item
            output = str(val)
            if type(val).__name__ == "Employee":
                output = val.name
            elif type(val).__name__ == "Flight":
                output = str(val.departure)
            elif type(val).__name__ == "list":
                output = ", ".join([x.name.split()[1] for x in val])

            self.window.move(baseHeight, (fieldWidth*i) + 1)
            self.window.addstr(f"{output:^{fieldWidth}}", attr)
            if i != 0:
                self.window.move(baseHeight, (fieldWidth*i) + 1)
            self.window.addch(curses.ACS_VLINE, attr)

    def filterOptions(self):
        # get possible filter options
        pass

    def select(self):
        # returns the screen with selected object passed to it
        pass

    def fields(self):
        # returns a list of fields to use in header
        return list(vars(self.collection[0]).keys())

