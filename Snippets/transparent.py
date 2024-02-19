import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

# Create a frame
frame = tk.Frame(root, bg="transparent")
frame.grid(row=0, column=0)

# Create a label
label = tk.Label(frame, text="Hello, world!", bg="transparent")
label.grid(row=0, column=0)

# Set the transparency of the frame
frame.wm_attributes("-transparentcolor", "transparent")

# Start the mainloop
root.mainloop()