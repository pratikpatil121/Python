from tkinter import *

def gets():
    print(f"The Username is: {uservalue.get()}")
    print(f"The Password is: {passvalue.get()}")


window=Tk()
window.geometry("700x400")

user=Label(window,text="Username")
password=Label(window,text="Password")

#GRID
user.grid(row=0)
password.grid(row=1)

#VARIABLE CLASSES IN TKINTER
#BooleanVar, DoubleVar, IntVar, StringVar

uservalue=StringVar()
passvalue=StringVar()

#ENTRY 
userentry=Entry(window,textvariable=uservalue)
passentry=Entry(window,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

button=Button(text="Submit",command=gets)
button.grid(row=3,column=1)


window.mainloop()