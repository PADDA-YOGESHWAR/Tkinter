#opening a new window
from tkinter import *

old_window=Tk()#independent window

def create_window():
    new_window=Tk()#independent window
    #new_window =Toplevel()#Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    old_window.destroy()#closes our old window 

Button(old_window,text ='create a new window',command=create_window).pack()



old_window.mainloop()