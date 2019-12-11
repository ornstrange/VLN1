import curses
from ui.interface import Interface
from file import File

def logo(stdscr, x, y):
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
    try:
        for i, line in enumerate(logoStrings):
            stdscr.move(i+y, x)
            stdscr.addstr(line)
        stdscr.refresh()
    except:
        pass

def art(stdscr, screenHeight, screenWidth):
    art = ["                                              __|__",
        "  -                                       ---@-(\")-@---",
        " | |\                                        !  !  !            ===================",
        "===| \______________|_______                                    |   NaN  Air  HQ  |",
        "  \|  O ooooo-=====-|ooo O n\__              . . . .            |      _____      |",
        "    -|=|--o-----||--|---|=||---'   _o’    o     .        o o    | $$  |  |  |  $$ |",
        "_____|=|__|\\n___oo______|=|o________|_____|\\n   |     ___|\|\\n__|_____|  |  |_____|"
    ]

    stdscr.hline(screenHeight-1,0,"_",screenWidth)
    for i, line in enumerate(art):
        stdscr.move((screenHeight - 7) + i, screenWidth//2 - (len(art[-1])//2))
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
    logo(stdscr, (screenWidth//6)-14, (screenHeight//2)-4) # draw logo
    logo(stdscr, ((screenWidth*5)//6)-14, (screenHeight//2)-4) # draw logo
    art(stdscr, screenHeight, screenWidth)

    interface = Interface(screenHeight, screenWidth) # init interface
    while interface.running:
        interface.draw()
        if interface.current.name == "main menu":
            interface.parseKeyMainMenu(all_collections)
        else:
            interface.parseKey()


if __name__ == "__main__":
    curses.wrapper(main)

