from tkinter import *

window=Tk()
window.title("Main Window")
window.geometry("400x300")

#Important Labels Options
'''
text --> adds text
bg --> background
fg --> foreground
font --> sets the font
padx --> padding
pady --> padding
relief --> styling the border --> SUNKEN, RAISED , GROOVE, RIDGE
'''

title_label=Label(text="TKInter Project Pratice",bg="red",padx="40",pady="30")
title_label.pack()

title_label2=Label(text="Detailing The Styling",bg="black",padx="40",pady="30",font=("comicsansm",19,"bold"),borderwidth=4,relief=SUNKEN)
title_label2.pack()
window.mainloop()