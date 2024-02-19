from tkinter import *

def hello():
    print("Hello")
    
def name():
    print("My Name Is Pratik")

def college():
    print("NBN College Of Engineering")

def year():
    print("BE:Last Year")

window=Tk()
window.geometry("400x300")

frame=Frame(window,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="red",text="Click me",command=hello)
b1.pack(side=LEFT,padx=10)

b2=Button(frame,fg="red",text="Your name",command=name)
b2.pack(side=LEFT,padx=10)

b3=Button(frame,fg="red",text="College",command=college)
b3.pack(side=LEFT,padx=10)

b4=Button(frame,fg="red",text="Which year",command=year)
b4.pack(side=LEFT,padx=10)

window.mainloop()