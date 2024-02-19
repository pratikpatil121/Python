from tkinter import *
from PIL import Image, ImageTk
def getvals():
    print(f"Name is : {namevalue.get()}")
    print(f"Phone Number is : {phonevalue.get()}")
    print(f"Male : {male.get()}")
    print(f"Female : {female.get()}")
    print(f"Emergency Contact Number is: {emergencyvalue.get()}")
    print(f"The Mode Of Payment is : {paymentvalue.get()}")
    print(f"Pre Food Meal : {foodvalue.get()}")

    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),male.get(),female.get(),emergencyvalue.get(),paymentvalue.get(),foodvalue.get()}\n")
#main display
window=Tk()
window.geometry("400x400")
window.title("Travel Form")

#Background Color
window.configure(bg="black")
window.resizable( 0,0 )

#Background Image
bg_image=Image.open("image1.png")
bg_resize=bg_image.resize((400,400))
bg=ImageTk.PhotoImage(bg_resize)

bg_label=Label(window,image=bg)
bg_label.place(x=0,y=0)

Label(text="Welcome to Core2Web Travels",font=("comicsansms",13,"italic","bold"),bg="tomato",fg="black",pady=15,borderwidth=4,relief=RAISED).grid(row=1,column=3)

#Importing Images
photo=Image.open("logo.png")
photo_resize=photo.resize((100,100))
photo_img=ImageTk.PhotoImage(photo_resize)
photo_label=Label(image=photo_img)
photo_label.grid(row=0,column=3)

#Labeling
name=Label(window,text="Name",bg="misty rose",fg="black",borderwidth=4,relief=SUNKEN)
phoneno=Label(window,text="PhoneNo",bg="misty rose",fg="black",borderwidth=4,relief=SUNKEN)
gender=Label(window,text="Gender",bg="misty rose",fg="black",borderwidth=4,relief=SUNKEN)
emergency=Label(window,text="Emergency Number",bg="misty rose",fg="black",borderwidth=4,relief=SUNKEN)
paymentmode=Label(window,text="Payment Mode",bg="misty rose",fg="black",borderwidth=4,relief=SUNKEN)

#Packing as Grid
name.grid(row=2,column=2)
phoneno.grid(row=3,column=2)
gender.grid(row=4,column=2)
emergency.grid(row=6,column=2)
paymentmode.grid(row=7,column=2)



namevalue=StringVar()
phonevalue=StringVar()
#gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()
foodvalue=IntVar()
male=IntVar()
female=IntVar()

#Entries
nameentry=Entry(textvariable=namevalue,bg="LightCyan2",fg="black")
phoneentry=Entry(textvariable=phonevalue,bg="LightCyan2",fg="black")
#genderentry=Entry(textvariable=gendervalue,bg="LightCyan2",fg="white")
emergencyentry=Entry(textvariable=emergencyvalue,bg="LightCyan2",fg="black")
paymententry=Entry(textvariable=paymentvalue,bg="LightCyan2",fg="black")

#Entries pack
nameentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
#genderentry.grid(row=4,column=3)
emergencyentry.grid(row=6,column=3)
paymententry.grid(row=7,column=3)

#Check box
food=Checkbutton(text="Want to prebook your meal?",variable=foodvalue,bg="LightCyan2",fg="black")
food.grid(row=9,column=3)

male1=Checkbutton(text="Male",variable=male,bg="LightCyan2",fg="black",)
male1.grid(row=4,column=3)
female1=Checkbutton(text="Female",variable=female,bg="LightCyan2",fg="black")
female1.grid(row=5,column=3)
#Button
button=Button(text="Submit",command=getvals,bg="LightCyan2",fg="black")
button.grid(row=10,column=3)
button.bind('<Double-1>',quit)
window.mainloop()