from tkinter import *
window = Tk()

hot = PhotoImage(file="C:/Users/USER/OneDrive/Desktop/programming/python GUI/dog.png")
hotLabel=Label(image=hot)
hotLabel.pack()

def submit():
    print('The temp is ',scale.get())
scale = Scale(window,
              from_=100,
              to=0,
              length = 400,
              orient=VERTICAL,#This is orientation that tells weather the scale must ve vertial or horizontal
              font = ('Consolas',10),
              tickinterval = 10,#adds a numeric indecators for the values
              showvalue=0,#this will hide the current value
              resolution=5,#increments the value to a fixed number
              troughcolor='#00ff00',
              fg='red',
              bg='black'
              )
scale.set(((scale['from']-scale['to'])/2))#default scale value 
scale.pack()
cold = PhotoImage(file="C:/Users/USER/OneDrive/Desktop/programming/python GUI/cold.png")
coldLabel=Label(image=cold)
coldLabel.pack()

button = Button(window,
                text='submit',
                command=submit,
                )
button.pack()

window.mainloop()