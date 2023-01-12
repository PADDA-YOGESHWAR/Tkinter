from tkinter import *
from tkinter import colorchooser

window = Tk()
def click():
    window.config(bg=colorchooser.askcolor()[1])

window.geometry("300x300")
button= Button(window,text='click here',command = click)
button.pack()








window.mainloop()