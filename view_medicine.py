import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from firebase_config import db

class ViewMedicineWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("List of Medicines")

        ref = db.collection('medicines')
        medicines = ref.stream()

        # Listbox with scrollbar
        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = Listbox(self.window, yscrollcommand=scrollbar.set)
        for medicine in medicines:
            data = medicine.to_dict()
            listbox.insert(tk.END, f"{medicine.id} - {data['remaining_tablets']} tablets")
        listbox.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

        # Bind the selection event
        listbox.bind('<<ListboxSelect>>', lambda event: self.show_medicine_details(event, listbox))
        
    def show_medicine_details(self, event, listbox):
        selected = listbox.get(listbox.curselection())
        medicine_name = selected.split(" - ")[0]

        ref = db.collection('medicines').document(medicine_name)
        medicine = ref.get()

        if medicine.exists:
            details = medicine.to_dict()
            messagebox.showinfo(f"{medicine_name} Details", f"Name: {medicine_name}\n"
                                                            f"Frequency: {details['frequency']}\n"
                                                            f"Before/After Food: {details['food_relation']}\n"
                                                            f"Total Tablets: {details['total_tablets']}\n"
                                                            f"Remaining Tablets: {details['remaining_tablets']}\n"
                                                            f"Last Intake Date: {details['last_intake_date']}")
        else:
            messagebox.showerror("Error", "Medicine not found!")
