import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from firebase_config import db

class RestockMedicineWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Restock Medicine")

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
        listbox.bind('<<ListboxSelect>>', lambda event: self.restock_medicine(event, listbox))

    def restock_medicine(self, event, listbox):
        selected = listbox.get(listbox.curselection())
        medicine_name = selected.split(" - ")[0]

        restock_window = tk.Toplevel(self.window)
        restock_window.title(f"Restock {medicine_name}")

        tk.Label(restock_window, text="Number of Strips to Restock").grid(row=0, column=0)
        strips_entry = tk.Entry(restock_window)
        strips_entry.grid(row=0, column=1)

        tk.Button(restock_window, text="Restock", command=lambda: self.update_stock(medicine_name, strips_entry.get(), restock_window)).grid(row=1, column=0, columnspan=2)

    def update_stock(self, medicine_name, strips, window):
        strips = int(strips)
        ref = db.collection('medicines').document(medicine_name)
        medicine = ref.get()

        if medicine.exists:
            details = medicine.to_dict()
            tablets_per_strip = details['total_tablets'] // (details['remaining_tablets'] // strips)
            new_tablets = strips * tablets_per_strip

            ref.update({
                'remaining_tablets': details['remaining_tablets'] + new_tablets,
                'total_tablets': details['total_tablets'] + new_tablets
            })

            messagebox.showinfo("Success", f"{medicine_name} restocked successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Medicine not found!")
