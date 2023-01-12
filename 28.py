from tkinter import *
from time import *

window = Tk()


def update():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    
    date_string=strftime("%B %d, %Y || %H:%M:%S")
    date_label.config(text=date_string)
    
    day_string=strftime("%A")
    day_label.config(text=day_string)
    
    #time_label.after(1000,update)
    window.after(1000,update)


time_label = Label(window,font=('Arial',50),fg='#00ff00',bg='black')
time_label.pack()

date_label = Label(window,font=('Times New Roman',30),fg='black',bg='Yellow')
date_label.pack()

day_label = Label(window,font=('Ink Free',25),fg='black',bg='white')
day_label.pack()

update()


window.mainloop()