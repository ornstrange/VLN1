import curses as cur

from .window import Windows

class Interface:
    def __init__(self, stdscr):
        windows = Windows(stdscr)
        windows.printLines()

