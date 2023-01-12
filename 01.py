from tkinter import *

#widgets = GIU elements : buttons,textboxes,labels,images
#windows = serves as a container to hold or contain these widges

window = Tk()#instantiate an instance of a window
window.geometry("450x420")#window size
window.title("Yogesh")#title of the window
icon = PhotoImage(file='C:/Users/USER/OneDrive/Desktop/programming/python GUI/dog.png')#converting image to icon
window.iconphoto(True,icon)#Here we make our icon display on the window by passing visibility as true and icon we want to display
window.config(background='black')#changes the background color of the window
#window.config(background='#5cfcff')#changes the background color of the window with hexadecimal values




window.mainloop()#place window on the computer screen, listen for events
