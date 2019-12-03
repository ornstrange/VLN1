import curses
from curses import panel
from .menu import Menus

class Windows:
    # call for top panels.window
    # [] access for windows
    # .panel[] access for panels
    def __init__(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.windows = {
            "main": stdscr,
            "sub": curses.newwin(h,w),
            "voyage": curses.newwin(h,w),
            "add": curses.newwin(h,w),
            "view": curses.newwin(h,w),
            "find": curses.newwin(h,w),
            "list": curses.newwin(h,w)}
        self.panel = {}
        for key in self.windows:
            self.panel[key] = panel.new_panel(self[key])

    def __getitem__(self, key):
        return self.windows[key]

    def __call__(self):
        return panel.top_panel().window()

    def front(self, key):
        # clear top window
        self().clear()
        # move selected panel to top
        self.panel[key].top()
        panel.update_panels()
        curses.doupdate()

