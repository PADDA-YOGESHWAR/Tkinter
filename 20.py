#canvas = widget that is used to draw graphs,plots,images in a window
from tkinter import *

window = Tk()
canvas = Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500,fill='red',width = 5)
canvas.create_line(0,500,500,0,fill='blue',width = 5)
canvas.create_rectangle(50,50,250,250,fill="purple",width=2)
canvas.create_polygon(10,10,50,40,100,50,width=2,fill="yellow",outline='black')
points=[10,10,50,30,150,80]
canvas.create_polygon(points,width=2,fill="yellow",outline='black')

canvas.create_arc(0,0,500,500,fill='green',style=CHORD)
canvas.create_arc(0,0,500,500,style=PIESLICE,start=270)

canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10)
canvas.create_arc(0,0,500,500,fill='white',extent=180,width=10,start =180)

canvas.create_oval(190,190,310,310,fill='white',width =10)

canvas.pack()



window.mainloop()