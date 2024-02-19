import tkinter as tk
from tkinter import ttk

class BloodBankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Bank Management System")

        # Initialize variables
        self.donors = []

        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets
        tk.Label(self.root, text="Donor Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.donor_name_entry = tk.Entry(self.root)
        self.donor_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        tk.Label(self.root, text="Blood Type:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.blood_type_entry = tk.Entry(self.root)
        self.blood_type_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Buttons
        tk.Button(self.root, text="Add Donor", command=self.add_donor).grid(row=2, column=0, columnspan=2, pady=10)

        # Treeview for displaying donors
        self.tree = ttk.Treeview(self.root, columns=('Name', 'Blood Type'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Blood Type', text='Blood Type')
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Search functionality
        tk.Label(self.root, text="Search Blood Type:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        tk.Button(self.root, text="Search", command=self.search_donor).grid(row=5, column=0, columnspan=2, pady=5)

    def add_donor(self):
        name = self.donor_name_entry.get()
        blood_type = self.blood_type_entry.get()

        if name and blood_type:
            self.donors.append((name, blood_type))
            self.update_treeview()
            self.clear_entries()

    def update_treeview(self):
        # Clear existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new donor data into the treeview
        for donor in self.donors:
            self.tree.insert('', 'end', values=donor)

    def clear_entries(self):
        # Clear entry fields after adding a donor
        self.donor_name_entry.delete(0, 'end')
        self.blood_type_entry.delete(0, 'end')

    def search_donor(self):
        search_term = self.search_entry.get().lower()
        matching_donors = [(name, blood_type) for name, blood_type in self.donors if search_term in blood_type.lower()]

        # Clear existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert matching donor data into the treeview
        for donor in matching_donors:
            self.tree.insert('', 'end', values=donor)

if __name__ == "__main__":
    root = tk.Tk()
    app = BloodBankApp(root)
    root.mainloop()
