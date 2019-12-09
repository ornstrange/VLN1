import curses

MENU_HEIGHT = 40
MENU_WIDTH  = 30

class Screen:
    def __init__(self, height, width, parent):
        self.parent = parent
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width)

class Menu(Screen):
    def __init__(self, parent,
                 entries,
                 height = MENU_HEIGHT,
                 width = MENU_WIDTH):
        super.__init__(super, height, width, parent)
        self.entries = entries
        self.selected = 0

    def draw(self):
        # draws menu with selected entry highlighted
        pass

    def go(self):
        # return the screen of the selected entry
        return self.entries[self.selected]

class Input(Screen):
    def __init__(self, parent, fields, rules, finished,
                 height = MENU_HEIGHT,
                 width = MENU_WIDTH):
        super.__init__(super, height, width, parent)
        self.fields = fields
        self.rules = rules
        self.finished = finished # screen when done

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

    def add(self, collection, new):
        # add new object to collection
        pass


class List(Screen):
    def __init__(self, parent, onSelect, entries, 
                 height = MENU_HEIGHT,
                 width = MENU_WIDTH):
        super.__init__(super, height, width, parent)
        self.onSelect = onSelect
        self.entries = entries # collection of objects
        self.selected = self.entries[0]

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
        #return self.onSelect.fields = vars(self.selected)

