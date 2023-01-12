from tkinter import *

#label is an area widget thar holds text/image within a window
window = Tk()
photo = PhotoImage(file='C:/Users/USER/OneDrive/Desktop/programming/python GUI/dog.png')

label =Label(window,
             text="This is puppy",
             font=("Arial",40,'bold'),
             fg='#00FF00',
             bg='black',
             relief=RAISED,
             bd=10,
             padx=20,
             pady=10,
             image =photo,
             compound='top')#defining a label widget
label.pack()#packing a label widget means adding label to window
#label.place(x=0,y=0)#place funtion gives us the aditional options like where we want to place the label


window.mainloop()
