from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir = "C:/Users/USER/OneDrive/Desktop/programming/python GUI/",
                                          title = "OPEN FILE",
                                          filetype=(("textfile", "*.txt"),('all files',"*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()
window = Tk()
button = Button(text='open',command = openfile)
button.pack()


window.mainloop()


