import curses
from ui.interface import Interface
from file import File

def main(stdscr):
    inp = "s"
    top = ["Voyages", "Airplanes", "Employees", "Destinations", "Exit"]
    longest = 0
    sel = 0
    for s in top:
        longest = len(s) if len(s) > longest else longest

    curses.curs_set(0)
    bruh = curses.newwin(len(top)+2,longest+4)
    bruh.keypad(True)

    while inp.lower() != "q":
        bruh.box()
        for i in range(len(top)):
            attr = curses.A_REVERSE if sel == i else curses.A_NORMAL
            bruh.move(1+(i),2)
            bruh.addstr(top[i], attr)

        inp = bruh.getkey()

        if inp == "KEY_DOWN":
            sel += 1 if sel < len(s) else 0
        elif inp == "KEY_UP":
            sel -= 1 if sel > 0 else 0
        elif inp == "\n":
            bruh.clear()
            bruh.getch()

    # interface = Interface(stdscr)



if __name__ == "__main__":
    curses.wrapper(main)

