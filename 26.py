from tkinter import *
import time
window = Tk()

WIDTH =500
HEIGHT = 500
xVelocity = 2
yVelocity = 3

canvas = Canvas(window,width = WIDTH,height = HEIGHT)
canvas.pack()

photo=PhotoImage(file="C:/Users/USER/OneDrive/Desktop/programming/python GUI/dog.png")
my_image=canvas.create_image(0,0,image=photo,anchor=NW)


image_width = photo.width()
image_height = photo.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0]>=(WIDTH - image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if (coordinates[1]>=(HEIGHT - image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
    



window.mainloop()