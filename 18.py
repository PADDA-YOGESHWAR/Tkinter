#grid geometry manager
#grid() =geometry manager that organizes widgets in a table - like structure in a parent
from tkinter import *
window=Tk()

Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNamelabel=Label(window,text = "First Name : ",width=20,bg='red').grid(row=1,column=0)
firstNameEntry=Entry(window).grid(row=1,column=1)

lastNamelabel=Label(window,text = "Last Name : ",bg='green').grid(row=2,column=0)
lastNameEntry=Entry(window).grid(row=2,column=1)

gmaillabel=Label(window,text = "GMail : ",bg='blue',width =30).grid(row=3,column=0)
gmailEntry=Entry(window).grid(row=3,column=1)

Button(window,text="submit").grid(row=4,column =0,columnspan=2)


window.mainloop()