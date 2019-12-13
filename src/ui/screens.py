import curses
from curses import A_BOLD, A_REVERSE, A_NORMAL, A_DIM, A_UNDERLINE
from curses.textpad import Textbox

from re import match

from file import File

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
        self.desc = None
        self.fieldValues = None
        self.finished = finished
        self.textBoxes = {}
        self.selected = 7

    def draw(self):
        self.window.clear()
        self.window.box()
        self.window.refresh()

        # draw textboxes
        for key in self.textBoxes:
            self.textBoxes[key][1].box()
            self.textBoxes[key][1].refresh()
            self.textBoxes[key][2].clear()
            self.textBoxes[key][2].addstr(self.fieldValues[key])
            self.textBoxes[key][2].refresh()

        # descriptions
        for i, field in enumerate(self.desc):
            attr = A_NORMAL
            if self.selected == i:
                attr = A_BOLD | A_UNDERLINE
            currentY = self.y + (i * 4)
            self.window.move(currentY, 3)
            self.window.addstr(self.desc[field], attr)

        # confirm button
        attr = A_NORMAL
        output = "Confirm"
        if self.selected == len(self.fields):
            curses.curs_set(0)
            attr = A_BOLD | A_REVERSE
            output = "> Confirm <"
        self.window.addstr(self.y + self.height - 8,
                           self.width//2 - len(output)//2,
                           output, attr)

        # quit instructions
        self.window.addstr(self.y + self.height - 5,
                           3,
                           "(q) go back / cancel")

    def change(self, entry):
        # change existing object
        pass

    def add(self):
        # add new object to collection
        if self.collection.name == "airplanes":
            newAirplane = File.newAirplane(File, self.fieldValues)
            self.collection.all.append(newAirplane)
            File.write(File, self.collection.name, self.collection)
        elif self.collection.name == "destinations":
            newDestination = File.newDestination(File, self.fieldValues)
            self.collection.all.append(newDestination)
            File.write(File, self.collection.name, self.collection)
        elif self.collection.name == "employees":
            newEmployee = File.newEmployee(File, self.fieldValues)
            self.collection.all.append(newEmployee)
            File.write(File, self.collection.name, self.collection)
        elif self.collection.name == "voyages":
            self.newVoyage()

    def newVoyage():
        newVoyage = File.newVoyage(File, self.fieldValues)

    def currentField(self):
        return self.fields[self.selected]

    def currentTextbox(self):
        return self.textBoxes[self.currentField()]

    def editCurrentTextbox(self):
        curses.curs_set(1)
        curses.ungetch(1)
        self.fieldValues[self.currentField()] = self.currentTextbox()[0].edit()
        if not self.checkCurrentField():
            self.fieldValues[self.currentField()] = ""
        curses.curs_set(0)

    def checkCurrentField(self):
        # check if field follows rule
        curField = self.currentField()
        curFieldText = self.fieldValues[curField]
        curRule = self.rules[curField]
        return match(curRule, curFieldText) != None

    def createTextbox(self):
        currentY = 3 + (len(self.textBoxes) * 4)
        boxWin = self.window.derwin(3, self.width - 4, currentY, 2)
        textWin = self.window.derwin(1, self.width - 6, currentY + 1, 3)
        return (Textbox(textWin), boxWin, textWin)

    def setupFields(self):
        # returns a list of fields to use in header
        self.textBoxes = {}
        firstObject = self.collection[0]
        fieldsRules = firstObject.fieldsRules()
        self.fields = [x[0] for x in fieldsRules]
        self.desc = {x[0]: x[1] for x in fieldsRules}
        self.rules = {x[0]: x[2] for x in fieldsRules}
        self.fieldValues = {x[0]: "" for x in fieldsRules}
        for name in self.fields:
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
        self.sortWin = self.window.derwin(20, 50,
                                          self.height//2 - 10,
                                          self.width//2 - 25)
        self.filterWin = self.window.derwin(20, 50,
                                          self.height//2 - 10,
                                          self.width//2 - 25)

    def draw(self):
        # draws entries, with filter, sort and view options
        # and selected entry highlighted
        if self.tabActive == "s":
            self.drawSort()
            return
        if self.tabActive == "f":
            self.drawFilter()
            return
        self.window.clear()
        self.drawHeader()
        self.drawEntries()
        self.drawTabs()
        self.window.box()
        self.window.refresh()
    
    def drawFilter(self):
        self.sortWin.clear()
        self.sortWin.box()        
        self.sortWin.addstr(16, 15, "(e) Entries / cancel")
        self.sortWin.refresh()

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

