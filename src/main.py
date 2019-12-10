import curses
from ui.interface import Interface
from file import File

def main(stdscr):
    f = File()
    all_collections = f.read()
    try:
        curses.curs_set(0)
    except:
        pass
    screenHeight, screenWidth = stdscr.getmaxyx()
    interface = Interface(stdscr)
    current = interface.view
    current.collection = all_collections["voyages"]
    currentWin = current.window
    currentWin.mvwin(screenHeight // 2 - current.height // 2,
                     screenWidth // 2 - current.width // 2)
    current.draw()
    currentWin.getch()


if __name__ == "__main__":
    curses.wrapper(main)

