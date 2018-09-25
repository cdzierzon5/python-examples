#Cody Dzierzon
#9/21/18
# Clock

from tkinter import*
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar

def current_time(): 
 
   total_seconds=calendar.timegm(time.gmtime())
   current_second = total_seconds%60

   total_minutes = total_seconds//60
   current_minute = total_minutes%60

   total_hours = total_minutes//60
   current_hour = total_hours%24
#set the time zone
   current_hour = current_hour-6

   if current_hour>=12:
      tag="PM"
   else:
      tag="AM"
   a=str(h)+":"+str(m)+":"str(s)+t
   timex=str(current_hour)+":"+str(current_minute)+":"+str(current_second)+tag
   if timex== a:
      beep()

   return timex

def beep():
   winsound.Beep(540,8000)
def quit(*args):
   root.destroy()
def show_time():
   global h
   global m
   global s
   global t
   time=current_time(h,m,s,t)
   txt.set(time)
   root.after(1000,show_time)

root=Tk()
root.attributes("-fullscreen",True)
root.configure(background='Black')
root.bind("x", quit)
root.bind("a",get_alarm
root.after(1000,show_time)
fnt=font.Font(family='Helvetica',size=230,weight='bold')
txt= StringVar()
lbl=ttk.Label(root, textvariable=txt, font=fnt,foreground="Teal", background="Black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()






