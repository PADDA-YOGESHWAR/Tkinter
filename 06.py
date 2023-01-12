from tkinter import *
#radio buttons are similar to ckeckbox but you can only select one from a group
window=Tk()
food=['pizza','burger','hotdog']
x =IntVar()
def order():
    if (x.get()==0):
        print("You ordered pizza")
    elif (x.get()==1):
        print("you ordered burger")
    elif (x.get()==2):
        print("you ordered a hotdog")
    else:
        print("Huh..?")

#pizzaimg =PhotoImage(file="pizza.jpg")
#burgerimg =PhotoImage(file="burgur.jpg")
#hotdogimg =PhotoImage(file="hotdog.jpg")
#foodimages=[pizzaimg,burgerimg,hotdogimg]
for index in range(len(food)):
    radio=Radiobutton(window,
                      text=food[index],#adds text to radio button
                      variable =x,#groups radiobutton if they share the same variable
                      value = index,#assaigns each radiobutton a different value
                      padx =25,#This adds padding on x-axis
                      pady=20,#This adds padding on y-axis
                      font = ("Arial",20),
                      #image = foodimages[index] adds images to radio buttons
                      compound='left',#addsimages and text
                      indicatoron=0 ,#eleminates the circle indicators and makes as pushbuttons
                      width = 40,#this sets width of radio buttons
                      command = order#this sets command of radio buttons to function
                      )
    radio.pack(anchor=W)




window.mainloop()