from tkinter import *

window=Tk()
window.geometry("400x300")

frame1=Frame(window,bg="grey",borderwidth=6,relief=SUNKEN)
frame1.pack(side=LEFT,fill=X)

frame2=Frame(window,borderwidth=8,bg="grey",relief=SUNKEN)
frame2.pack(side=BOTTOM,fill=X)

frame3=Frame(window,borderwidth=8,bg="orange",relief=SUNKEN)
frame3.pack(side=LEFT,fill=X)

text_label=Label(frame1,text="Project TKInter")
text_label.pack(side=LEFT,fill=Y)

text2_label=Label(frame2,text="Details of tkinter",font=("Helvetica",20,"bold"),fg="red")
text2_label.pack(side=BOTTOM,fill=X)

text3_label=Label(frame3,text="Hello World",fg="yellow")
text3_label.pack(side=LEFT,fill=Y)

window.mainloop()