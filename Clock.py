import curses
import time

print("intializing screen")
screen = curses.initscr()
curses.noecho()
curses.cbreak()

time.sleep(10)

curses.nocbreak(); screen.keypad(0); curses.echo()
curses.endwin()
print("screen closed")
