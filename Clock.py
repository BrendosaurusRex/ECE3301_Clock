# import curses
# import time
#
# print("intializing screen")
# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
#
# time.sleep(10)
#
# curses.nocbreak(); screen.keypad(0); curses.echo()
# curses.endwin()
# print("screen closed")

import RPi.GPIO as GPIO
#import Adafruit_CharLCD
import curses
from subprocess import *
from time import sleep, strftime, mktime
from datetime import datetime

lcd = Adafruit_CharLCD()

lcd.begin(16,1)

#GPIO.setup(18, 0)
#GPIO.output(18, 1)

dti = mktime(datetime.now().timetuple())
while 1:
    ndti = mktime(datetime.now().timetuple())
    if dti < ndti:
        dti = ndti
        lcd.clear()
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        sleep(0.95)
    else:
        sleep(0.01)
