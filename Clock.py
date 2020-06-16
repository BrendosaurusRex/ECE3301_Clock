from tkinter import *
import tkinter
import time
import calendar
from datetime import date
import glob
import os

# os.system('modprobe w1-gpio')
# os.system('modprobe w1-therm')
#
# base_dir = '/sys/bus/w1/devices/'
# device_folder = glob.glob(base_dir + '28-*')[0] # Should be "28*" as device directory but
# device_file = device_folder + '/w1_slave'       # hardware is not interfacing properly
#
# def read_temp_raw():
#     # If device_file magically appears and is consistent, then use this code block
#      f = open(device_file, 'r')
#      lines = f.readlines()
#      f.close()
#      return lines
#
# def read_temp():
#     lines = read_temp_raw()
#     while lines[0].strip()[-3:] != 'YES':
#         time.sleep(0.2)
#         lines = read_temp_raw()
#     equals_pos = lines[1].find('t=')
#     if equals_pos != -1:
#         temp_string = lines[1][equals_pos+2:]
#         temp_c = float(temp_string) / 1000.0
#         temp_f = temp_c * 9.0 / 5.0 + 32.0
#         return temp_c, temp_f


cal = calendar.month(2020, 5)
root = Tk()
frame = Frame(root)
frame.pack()

root.geometry('800x400+350+300')
root.title("python clock designing")


cframe =Frame(root, width=200, height=100, bg='green')
cframe.pack(side= LEFT)

clock=Label(cframe, padx=200, pady=100, bd=3, fg= 'white',font=('arial',20,'bold'),text=cal ,bg='light green')
clock.pack(side= LEFT )

today = date.today()

cframe3 =Frame(root, width=200, height=100, bg='green')
cframe3.pack(side=BOTTOM)

clock3=Label(cframe, padx=200, pady=100, bd=3, fg= 'white',font=('arial',20,'bold'),text=today ,bg='light green')
clock3.pack(side= BOTTOM )

timenow=''
c2frame =Frame(root, width=200, height=100)
c2frame.pack(side = LEFT)

clock2=Label(cframe,padx=200, pady=200, bd=3, fg= 'white',font=('arial',48,'bold'),text= timenow,bg='black')
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


# =============================================================================
# Old Code
# =============================================================================

# def main(stdscr):
#     curses.curs_set(0)
#     stdscr.nodelay(1)
#
#     dti = mktime(datetime.now().timetuple())
#     while 1:
#         ndti = mktime(datetime.now().timetuple())
#         if dti < ndti:
#             dti = ndti
#             stdscr.addstr(datetime.now().strftime('%b %d  %H:%M:%S\r'))
#             stdscr.refresh()
#             sleep(0.95)
#         else:
#             sleep(0.01)
#
# curses.wrapper(main)
