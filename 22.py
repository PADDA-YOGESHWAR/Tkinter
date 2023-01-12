#mouse events
from tkinter import *
def dosomething(event):
    print("The Mouse was placed in the area : "+str(event.x)+","+str(event.y))
    

window=Tk()


#window.bind("<Button-1>",dosomething)#left click of mouse 
#window.bind("<Button-2>",dosomething)#scroll wheel of mouse 
#window.bind("<Button-3>",dosomething)#right click of mouse 
#window.bind("<ButtonRelease>",dosomething)
#window.bind("<Enter>",dosomething)#Enters The window
#window.bind("<Leave>",dosomething)#Leave The window
#window.bind("<Motion>",dosomething)#For every small motion of change

 
window.mainloop()