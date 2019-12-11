import curses
from ui.interface import Interface
from file import File

def main(stdscr):
    # create collections from file
    f = File()
    all_collections = f.read()

    # hide the cursor
    try:
        curses.curs_set(0)
    except:
        pass

    screenHeight, screenWidth = stdscr.getmaxyx()
    interface = Interface(stdscr) # init interface
    interface().window.keypad(True)
    while True:
        interface().center(screenHeight, screenWidth)
        interface.draw()
        if interface().mainMenu:
            interface.parseKeyMain(all_collections)
        else:
            interface.parseKey()


if __name__ == "__main__":
    curses.wrapper(main)

