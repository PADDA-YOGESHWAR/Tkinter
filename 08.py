#listbox is a listing a selectable text items within it's own container
from tkinter import *
window = Tk()

def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print('You have ordered ')
    for index in food:
        print(index)
    
    #print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())
    
def Del():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

listbox=Listbox(window,
                bg='#f7ffde',
                font=('Constantia',35),
                width =12,
                selectmode=MULTIPLE
                
                )
listbox.pack()


listbox.insert(1,'Pizza')
listbox.insert(2,'Burgur')
listbox.insert(3,'softdrink')
listbox.insert(4,'garlic bread')
listbox.insert(5,'pasta')

listbox.config(height=listbox.size())#dynamically changes the size of a listbox

entry = Entry(window)
entry.pack()

submitbutton = Button(window,text='submit',command = submit)
submitbutton.pack()

addbutton = Button(window,text='ADD',command = add)
addbutton.pack()

delbutton = Button(window,text='DELETE',command = Del)
delbutton.pack()

window.mainloop()