from tkinter import *
from PIL import Image,ImageTk

def userinfo():
    username=name_entry.get()
    password=pass_entry.get() 

    name_label=Label(text=username)
    pass_label=Label(text=password)

    name_label.pack()
    pass_label.pack()

window=Tk()
window.title("Main Window")
window.geometry("400x300")

name_label=Label(text="Enter Name: ")
name_label.pack()

name_entry=Entry()
name_entry.pack()

pass_label=Label(text="Enter Password: ")
pass_label.pack()

pass_entry=Entry()
pass_entry.pack()

submit_button=Button(text="Submit",command=userinfo)
submit_button.pack()

#for png images
photo=PhotoImage(file="shashi_sir.png")
photo_label=Label(image=photo)
photo_label.pack()


#for jpg images
#image=Image.open("Passport.jpg")
photo=ImageTk.PhotoImage(file="Passport.jpg")
image_label=Label(image=photo)
image_label.pack()

window.mainloop()