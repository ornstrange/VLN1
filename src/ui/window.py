import curses
from .menu import Menus

class Windows:
    # [] access for windows
    def __init__(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.windows = {
            "main": stdscr,
            "sub": curses.newwin(1,1),
            "voyage": curses.newwin(1,1),
            "add": curses.newwin(1,1),
            "view": curses.newwin(1,1),
            "find": curses.newwin(1,1),
            "list": curses.newwin(1,1)}
        self.menus = Menus()

    def __getitem__(self, key):
        return self.windows[key]

