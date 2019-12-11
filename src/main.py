import curses
from ui.interface import Interface
from file import File

def logo(stdscr, screenWidth):
    logoStrings = [
        "   /-/| /-/ /-----/ /-/| /-/",
        "  / / |/ / / /=/ / / / |/ /",
        " / /| / / / __  / / /| / /",
        "/_/ |/_/ /_/ /_/ /_/ |/_/",
        "",
        "    /-----/ /-/ /-----/",
        "   / /=/ / / / / /=/ /",
        "  / __  / / / / _  _/",
        " /_/ /_/ /_/ /_/ \_\\"
    ]
    for i, line in enumerate(logoStrings):
        stdscr.move(i+3, (screenWidth // 2) - 14)
        stdscr.addstr(line)
    stdscr.refresh()

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
    logo(stdscr, screenWidth) # draw logo

    interface = Interface(screenHeight, screenWidth) # init interface
    while interface.running:
        interface.draw()
        if interface.current.name == "main menu":
            interface.parseKeyMainMenu(all_collections)
        else:
            interface.parseKey()


if __name__ == "__main__":
    curses.wrapper(main)

