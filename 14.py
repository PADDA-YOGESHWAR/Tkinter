#menubar
from tkinter import *

window = Tk()

def openfile():
    print("file has been opened")

def savefile():
    print("file has been saved")
    
def cut():
    print("Something has been cut")

def copy():
    print("Something has been copied")

def paste():
    print("Something has been pasted")    
#menu bar
menubar = Menu(window)
window.config(menu=menubar)

#filemenu
filemenu = Menu(menubar,tearoff=0,font=('MV Boli',10))
menubar.add_cascade(label='File',menu = filemenu)


filemenu.add_command(label='Open',command = openfile)
filemenu.add_command(label='Save',command = savefile)
filemenu.add_separator()
filemenu.add_command(label='Exit',command =quit)

#editmenu
editmenu = Menu(menubar,tearoff=0,font=('MV Boli',10))
menubar.add_cascade(label='Edit',menu = editmenu)
editmenu.add_command(label='Cut',command = cut)
editmenu.add_command(label='Copy',command = copy)
editmenu.add_command(label='Paste',command =paste)


window.mainloop()