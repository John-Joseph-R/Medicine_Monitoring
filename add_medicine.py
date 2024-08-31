import tkinter as tk
from tkinter import messagebox
from firebase_config import db

class AddMedicineWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Add Medicine")

        # Name
        tk.Label(self.window, text="Medicine Name").grid(row=0, column=0)
        self.medicine_name = tk.Entry(self.window)
        self.medicine_name.grid(row=0, column=1)

        # Frequency
        tk.Label(self.window, text="Frequency of Consumption").grid(row=1, column=0)
        self.frequency = tk.Entry(self.window)
        self.frequency.grid(row=1, column=1)

        # Food Relation
        tk.Label(self.window, text="Before/After Food").grid(row=2, column=0)
        self.food_relation = tk.Entry(self.window)
        self.food_relation.grid(row=2, column=1)

        # Strips
        tk.Label(self.window, text="Number of Strips").grid(row=3, column=0)
        self.strips = tk.Entry(self.window)
        self.strips.grid(row=3, column=1)

        # Tablets per Strip
        tk.Label(self.window, text="Tablets per Strip").grid(row=4, column=0)
        self.tablets_per_strip = tk.Entry(self.window)
        self.tablets_per_strip.grid(row=4, column=1)

        # Add Medicine Button
        tk.Button(self.window, text="Add Medicine", command=self.add_medicine).grid(row=5, column=0, columnspan=2)

    def add_medicine(self):
        name = self.medicine_name.get()
        frequency = self.frequency.get()
        strips = int(self.strips.get())
        tablets_per_strip = int(self.tablets_per_strip.get())
        food_relation = self.food_relation.get()

        total_tablets = strips * tablets_per_strip

        ref = db.collection('medicines')
        ref.document(name).set({
            'frequency': frequency,
            'food_relation': food_relation,
            'total_tablets': total_tablets,
            'remaining_tablets': total_tablets,
            'last_intake_date': None
        })

        messagebox.showinfo("Success", f"Medicine {name} added successfully!")
        self.window.destroy()
