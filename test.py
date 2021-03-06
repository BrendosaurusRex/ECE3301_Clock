
# import curses
# # from RPLCD import CharLCD
#
# # print("Successfully installed {}".format("RPLCD"))
# print('hi')
# print('testing...1, 2, 3.')
#
#
# print("Brendon wuz here")
# print("Jarod was also here")
# print("testing 2")

# ===============================================================
# Brendon: Testing gpiozero library and Button module
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
# Brendon: Testing GPIO library
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
# Jarod: Testing GPIO library
# ===============================================================
# this method is  is waiting for a rising edge from a button Press
# try this Out
# also reference this link: https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
#to download the library, im note sure if your other attempts downloaded it the same way
#if it works it can then be adjusted to fit our needs
import RPi.GPIO as GPIO

def button_callback(channel):
	print("button was pushed")

GPIO.setwarnings(False) # ignore warnings lol
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)

message = input("press enter to quit\n\n")
GPIO.cleanup()
# ===============================================================
# Jarod: Testing clock GUI
# ===============================================================
from tkinter import *
import tkinter
import time
import calendar
from datetime import date

cal = calendar.month(2020, 5)
root = Tk()
frame = Frame(root)
frame.pack()

root.geometry('600x300+350+300')
root.title("python clock designing")


cframe =Frame(root, width=15, height=15, bg='black')
cframe.pack(side= LEFT)
 
clock=Label(cframe, padx=15, pady=15, bd=3, fg= 'white',font=('arial',20,'bold'),text=cal ,bg='black')
clock.pack(side= LEFT )




deg_c,deg_f=read_temp()

cframe4 =Frame(root, width=200, height=31, bg='black')
cframe4.pack(side=BOTTOM)
 
clock4=Label(cframe, padx=200, pady=31, bd=3, fg= 'white',font=('arial',20,'bold'),text=(temp_f,"F�","/",temp_c,"C�") ,bg='black')
clock4.pack(side= BOTTOM )


today = date.today()

cframe3 =Frame(root, width=200, height=25, bg='black')
cframe3.pack(side=BOTTOM)
 
clock3=Label(cframe, padx=200, pady=25, bd=3, fg= 'white',font=('arial',20,'bold'),text=today ,bg='black')
clock3.pack(side= BOTTOM )

timenow=''
c2frame =Frame(root, width=200, height=35,bg='black')
c2frame.pack(side = LEFT)
 
clock2=Label(cframe,padx=200, pady=35, bd=3, fg= 'white',font=('arial',20,'bold'),text= timenow,bg='black')
clock2.pack(side = LEFT)
 



def timer():
    global timenow
    newtime = time.strftime('%H: %M: %S %p')
    if newtime != timenow:
        timenow= newtime
        clock2.config(text= timenow)
    clock2.after(200, timer)
timer()

 
 
mainloop()


# ===============================================================
# Brendon: Testing Thermal Sensor code
# Using: Raspberry_Pi_DS18B20_Temperature_Sensing/thermometer.py
# ===============================================================

import glob
import time
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-*')[0] # Should be "28*" as device directory but
device_file = device_folder + '/w1_slave'       # hardware is not interfacing properly

def read_temp_raw():
    # If device_file magically appears and is consistent, then use this code block
     f = open(device_file, 'r')
     lines = f.readlines()
     f.close()
     return lines

# Attempts to read DS18B20 device file, if available
	#catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#out,err = catdata.communicate()
	#out_decode = out.decode('utf-8')
	#lines = out_decode.split('\n')
	#return lines

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

# while True:
    #deg_c, deg_f = read_temp()
    print(read_temp())
    time.sleep(1)
 