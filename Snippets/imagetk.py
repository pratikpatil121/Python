from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("Main Window")
window.geometry("400x300")

#for png images
photo=PhotoImage(file="shashi_sir.png")
photo_label=Label(image=photo)
photo_label.pack()

'''
#for jpg images
#image=Image.open("Passport.jpg")
photo=ImageTk.PhotoImage(file="Passport.jpg")
image_label=Label(image=photo)
image_label.pack()
'''

window.mainloop()