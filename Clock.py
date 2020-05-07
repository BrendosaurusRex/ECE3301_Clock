from tkinter import *
import tkinter
import time
import calendar
from datetime import date
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

# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# redbutton = Button(frame, text=cal, fg="red")
# redbutton.pack( side =  RIGHT)
#
# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
#
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)

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
