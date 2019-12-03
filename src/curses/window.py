import curses as cur
from curses import panel

from menu import Menus

class Windows:
    # call for top panels.window
    # [] access for windows
    # .panel[] access for panels

    def __init__(self, stdscr):
        h, w = stdscr.getmaxyx()
        self.windows = {
            "main": stdscr,
            "sub": cur.newwin(h,w),
            "voyage": cur.newwin(h,w),
            "add": cur.newwin(h,w),
            "view": cur.newwin(h,w),
            "find": cur.newwin(h,w),
            "list": cur.newwin(h,w)}
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
        cur.doupdate()

if __name__ == "__main__":
    stdscr = cur.initscr()
    cur.noecho()
    cur.cbreak()
    stdscr.keypad(True)

    windows = Windows(stdscr)

    windows.front("main")
    windows().addstr("i am main")
    windows().getch()

    cur.nocbreak()
    stdscr.keypad(False)
    cur.echo()
    cur.endwin()

