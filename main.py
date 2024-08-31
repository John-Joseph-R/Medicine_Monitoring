import tkinter as tk
from add_medicine import AddMedicineWindow
from view_medicine import ViewMedicineWindow
from log_intake import LogIntakeWindow
from restock_medicine import RestockMedicineWindow

class MedicineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medicine Management")

        # Main Menu Buttons
        tk.Button(root, text="Add Medicine", command=self.open_add_medicine_window).pack(fill=tk.X)
        tk.Button(root, text="View Medicine", command=self.open_view_medicine_window).pack(fill=tk.X)
        tk.Button(root, text="Log Medicine Intake", command=self.open_log_intake_window).pack(fill=tk.X)
        tk.Button(root, text="Restock", command=self.open_restock_window).pack(fill=tk.X)

    def open_add_medicine_window(self):
        AddMedicineWindow(self.root)

    def open_view_medicine_window(self):
        ViewMedicineWindow(self.root)

    def open_log_intake_window(self):
        LogIntakeWindow(self.root)

    def open_restock_window(self):
        RestockMedicineWindow(self.root)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MedicineApp(root)
    root.mainloop()
