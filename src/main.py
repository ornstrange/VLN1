from curses import wrapper
from ui.interface import Interface
from file import File

def main(stdscr):
    ui = Interface(stdscr)

    stdscr.clear()
    for i in range(0, 9):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
        stdscr.getkey()
    stdscr.refresh()

if __name__ == "__main__":
    wrapper(main)

