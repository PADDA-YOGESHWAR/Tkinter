from tkinter import *
#entry widget = textbox that creates a single line of user input

window =Tk()
def submit():
    info = entry.get()
    print("The entered text is "+info)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
    
def back():
    entry.delete(len(entry.get())-1,END)
    
entry = Entry(window,
              font=("Arial",30),
              fg="#00FF00",
              bg='black',
              show='*')

#entry.insert(0,"Demo Entry")


entry.pack(side=LEFT)
submit=Button(window,text = "Submit",command = submit)
submit.pack(side = RIGHT)
delete=Button(window,text = "Delete",command = delete)
delete.pack(side = RIGHT)
backspace=Button(window,text = "<=",command = back)
backspace.pack(side = RIGHT)

window.mainloop()