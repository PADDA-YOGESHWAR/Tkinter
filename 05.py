from tkinter import *
window = Tk()

def check():
    if(x.get()==1):
        print("You agreed")
    else:
        print("You don't agree")
x = IntVar()
img = PhotoImage(file="C:/Users/USER/OneDrive/Desktop/programming/python GUI/dog.png")
checkbutton=Checkbutton(window,
                        text = "Yes, I agree",
                        variable = x,
                        onvalue=1,#True/YES
                        offvalue=0,#False/NO
                        command = check,
                        font=("Arial",20),
                        fg="#00ff00",
                        bg="black",
                        activebackground="yellow",
                        activeforeground="red",
                        padx=25,
                        pady=20,
                        image = img,
                        compound = "left")
checkbutton.pack()

window.mainloop()