from tkinter import *
from ball import *
import time

window = Tk()


WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
volley_ball = ball(canvas,0,0,100,1,1,"white")
tennis_ball = ball(canvas,0,0,30,4,3,'yellow')
cricket_ball = ball(canvas,0,0,50,5,2,'red')
basket_ball = ball(canvas,0,0,80,8,6,'orange')

while True:
    volley_ball.move()
    tennis_ball.move()
    cricket_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()