
import curses
# from RPLCD import CharLCD

# print("Successfully installed {}".format("RPLCD"))
print('hi')
print('testing...1, 2, 3.')


print("Brendon wuz here")
print("Jarod was also here")
print("testing 2")

# ===============================================================
# Testing gpiozero library and Button module
# ===============================================================
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

# print("Out of loop")

# ===============================================================
# Testing GPIO library
# ===============================================================

# import RPi.GPIO as G
# from time import sleep
#
# # set numbering mode and define output pins
# G.setmode(G.BOARD)
# G.setup(11, G.IN)
# G.setup(13, G.IN)
# G.setup(15, G.IN)
# G.setup(16, G.IN)
#
# right_button = G.input(17)
# up_button = G.input(27)
# down_button = G.input(22)
# left_button = G.input(23)
#
# while True:
#     if right_button == True:
#         print("-->")
#     elif up_button == True:
#         print("^\n|")
#     elif down_button == True:
#         print("|\n*")
#     elif left_button == True:
#         print("<--")
#     sleep(10)
#     break

# ===============================================================
# Testing Thermal Sensor code
# Using: Raspberry_Pi_DS18B20_Temperature_Sensing/thermometer.py
# ===============================================================

import glob
import time
import subprocess

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '00-*')[0] # Should be "28*" as device directory but
device_file = device_folder + '/w1_slave'       # hardware is not interfacing properly

def read_temp_raw():
    # If device_file magically appears and is consistent, then use this code block
    # f = open(device_file, 'r')
    # lines = f.readlines()
    # f.close()
    # return lines

# Attempts to read DS18B20 device file, if available
	catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err = catdata.communicate()
	out_decode = out.decode('utf-8')
	lines = out_decode.split('\n')
	return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

while True:
    deg_c, deg_f = read_temp()
    print("%4f degrees F\r")
    time.sleep(1)
