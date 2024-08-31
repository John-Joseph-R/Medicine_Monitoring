import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from firebase_config import db
import datetime

class LogIntakeWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Log Medicine Intake")

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
        listbox.bind('<<ListboxSelect>>', lambda event: self.log_intake(event, listbox))

    def log_intake(self, event, listbox):
        selected = listbox.get(listbox.curselection())
        medicine_name = selected.split(" - ")[0]

        ref = db.collection('medicines').document(medicine_name)
        medicine = ref.get()

        if medicine.exists:
            details = medicine.to_dict()
            remaining_tablets = details['remaining_tablets'] - 1

            ref.update({
                'remaining_tablets': remaining_tablets,
                'last_intake_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

            if remaining_tablets < 10:
                daily_tablets = int(details['frequency'])
                if remaining_tablets < daily_tablets * 3:
                    messagebox.showwarning("Warning", f"Warning: {medicine_name} won't last for 3 more days! Only {remaining_tablets} tablets remaining.")
                else:
                    messagebox.showinfo("Info", f"{medicine_name} has enough tablets for 3 more days.")
            else:
                messagebox.showinfo("Logged", f"{medicine_name} intake logged. {remaining_tablets} tablets remaining.")
        else:
            messagebox.showerror("Error", "Medicine not found!")
