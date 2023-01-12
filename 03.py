from tkinter import *
#button = does some action when u click on it

window = Tk()

img = PhotoImage(file="C:/Users/USER/OneDrive/Desktop/programming/python GUI/dog.png")
count = 0
def click():
    global count
    count = count +1
    print("You clicked the button")
    print(count)
    
button = Button(window,
                text='click',
                command =click,
                font=("Comic Sans",30),
                fg='#00FF00',
                bg="black",
                activeforeground="Blue",
                activebackground="Yellow",
                state = ACTIVE,
                image = img,
                compound='bottom')
button.pack()






window.mainloop()
