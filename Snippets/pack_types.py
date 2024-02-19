from tkinter import *

window=Tk()
window.title("Main Window")
window.geometry("400x300")

#Important Pack Options
#anchor = nw --> Nort West Directions
#side =top, bottom, left, right
#fill -->X,Y moves w// resize wi ndow
#padx
#pady



title_label=Label(text="Hey! It's Me Pratik",bg="black")
title_label.pack(side=BOTTOM,anchor="ne",fill=X,padx=50,pady=50)


window.mainloop()