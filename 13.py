from tkinter import *
from tkinter import filedialog
window = Tk()

def save():
    file = filedialog.asksaveasfile(initialdir="C:/Users/USER/OneDrive/Desktop/programming/python GUI",defaultextension='.txt',
                                    filetypes = [
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All files",".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text : ")
    file.write(filetext)
    file.close()
    
    
button = Button(text = 'SAVE',command = save)
button.pack()

text = Text(window)
text.pack()




window.mainloop()