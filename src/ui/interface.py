import curses as cur

from .screens import Top, Sub, View, Add, Search, List

class Interface:
    def __init__(self, stdscr):
        self.current = Top(stdscr)

