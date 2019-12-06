import curses

MENU_HEIGHT = 40
MENU_WIDTH  = 30

class Screen:
    def __init__(self):
        self.parent = None
        self.selected = 0
        self.children = {}
        self.h = MENU_HEIGHT
        self.w = MENU_WIDTH
        self.window = curses.newwin(self.h, self.w)

    def draw(self):
        self.window.box()
        for i, entry in children:
            if self.selected == i:
                attr = curses.A_REVERSE
            else:
                attr = curses.A_NORMAL
            self.window.move(self.h)

