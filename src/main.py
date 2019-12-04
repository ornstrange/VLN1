from curses import wrapper
from ui.interface import Interface
from file import File

def main(stdscr):
    ui = Interface(stdscr)

if __name__ == "__main__":
    wrapper(main)

