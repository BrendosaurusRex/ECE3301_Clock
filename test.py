
import curses
# from RPLCD import CharLCD

# print("Successfully installed {}".format("RPLCD"))
print('hi')
print('testing...1, 2, 3.')


print("Brendon wuz here")
print("Jarod was also here")
print("testing 2")

# ================================================================
# Testing gpiozero library and Button module
# ================================================================
# from gpiozero import Button
# from time import sleep
#
# right_button = Button(17)
# up_button = Button(27)
# down_button = Button(22)
# left_button = Button(23)
#
# # up_button.wait_for_press()
# # print("Press received")
#
# while True:
#     if right_button.is_pressed == True:
#         print("-->")
#     elif up_button.is_pressed == True:
#         print("^\n|")
#     elif down_button.is_pressed == True:
#         print("|\n*")
#     elif left_button.is_pressed == True:
#         print("<--")
#     sleep(5)
#     break

print("Out of loop")

# ================================================================
# Testing GPIO library
# ================================================================

import RPi.GPIO as G
from time import sleep

# set numbering mode and define output pins
G.setmode(G.BOARD)
G.setup(11, G.IN)
G.setup(13, G.IN)
G.setup(15, G.IN)
G.setup(16, G.IN)

right_button = G.input(17)
up_button = G.input(27)
down_button = G.input(22)
left_button = G.input(23)

while True:
    if right_button == True:
        print("-->")
    elif up_button == True:
        print("^\n|")
    elif down_button == True:
        print("|\n*")
    elif left_button == True:
        print("<--")
    sleep(10)
    break
