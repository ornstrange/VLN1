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
    try:
        stdscr.hline(screenHeight-1,0,"_",screenWidth)
        for i, line in enumerate(art):
            stdscr.move((screenHeight - 7) + i, screenWidth//2 - (len(art[-1])//2))
            stdscr.addstr(line)
        stdscr.refresh()
    except:
        pass

def main(stdscr):
    # create collections from file
    f = File()
    all_collections = f.read()

    # hide the cursor
    curses.curs_set(0)

    # init interface
    screenHeight, screenWidth = stdscr.getmaxyx()
    interface = Interface(all_collections, screenHeight, screenWidth)
    while interface.running:
        if interface.current.type == "menu":
            # draw logo and art
            logo(stdscr, (screenWidth//6)-14, (screenHeight//3)-4)
            logo(stdscr, ((screenWidth*5)//6)-14, (screenHeight//3)-4)
            art(stdscr, screenHeight, screenWidth)
        # draw current window and parse input
        interface.draw()
        interface.parseKey()

if __name__ == "__main__":
    curses.wrapper(main)

