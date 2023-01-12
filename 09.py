from tkinter import *
from tkinter import messagebox
window =Tk()

def click():
    #messagebox.showinfo(title = "message box",message="Hey.. How are you")
    '''while(True):
        messagebox.showwarning(title = "WARNING",message="I will kill you")'''
    #messagebox.showerror(title = "Error",message="Somting when wrong")
    '''if messagebox.askokcancel(title='ok or cancel',message = 'Do you like coding?'):
        print("OK let's do it")
    else:
        print("OK then try somthing which you are interested in")'''
    '''if messagebox.askretrycancel(title='ok or cancel',message = 'Do you want to retry coding?'):
        print("OK let's do it")
    else:
        print("OK then try somthing which you are interested in")'''
    '''if messagebox.askyesno(title='YES or NO',message = 'Do you want to code'):
        print("Come with me then..! let's code")
    else:
        print("Why don't you try it once?")'''
    '''answer = messagebox.askquestion(title="question",message="Do you like python?")
    if answer == "yes":
        print("I like python too")
    else:
        print(" Y do you not like python")'''
    ans = messagebox.askyesnocancel(title = 'YES NO CANCLE',message = "Press any one of the following",icon= 'warning')
    if ans == True:
        print("YOU PRESSED YES")
    elif ans == False:
        print("YOU PRESSED NO")
    else :
        print("YOU PRESSED CANCEL")    



button = Button(window,
               command = click,
               text = 'send')

button.pack()




window.mainloop()