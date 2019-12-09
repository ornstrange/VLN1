import curses as cur

from .screens import Screen

class Interface:
    def __init__(self, stdscr):
        self.main = stdscr
        self.main = Screen()
        self.sub = Screen()

