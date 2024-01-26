import tkinter as tk
class HelloCore2webApp:
    def __init__(self):
# Create the main window
        self.root = tk.Tk()
        self.root.title("Hello Core2web")
        # Specify the window dimensions as a string (width x height)
        self.root.geometry("300x200")
        # Create a label to display the message
        self.label = tk.Label(self.root, text="")
        self.label.pack(pady=10)
        # Create a button that, when clicked, calls the display_message method
        self.hello_button = tk.Button(self.root, text="Click Me", command=self.display_message)
        self.hello_button.pack(pady=10)
    def display_message(self):
        self.label.config(text="Hello, Core2web!")
    def run(self):
# Run the tkinter event loop
        self.root.mainloop()
if __name__ == '__main__':
# Create an instance of the HelloCore2webApp class and run the application
    app = HelloCore2webApp()
    app.run()