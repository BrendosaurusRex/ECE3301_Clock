
import curses
from curses import textpad
from subprocess import *
from time import sleep, strftime, mktime
from datetime import datetime

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    dti = mktime(datetime.now().timetuple())
    while 1:
        ndti = mktime(datetime.now().timetuple())
        if dti < ndti:
            dti = ndti
            stdscr.addstr(datetime.now().strftime('%b %d  %H:%M:%S\n'))
            stdscr.refresh()
            sleep(0.95)
        else:
            sleep(0.01)

curses.wrapper(main)
