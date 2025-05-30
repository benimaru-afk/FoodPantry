import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from datetime import datetime, timedelta

# Database setup
conn = sqlite3.connect("food_items.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS food (
        name TEXT,
        entry_date TEXT,
        expire_date TEXT
    )
''')
conn.commit()

# Main Application
class FoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Tracker")
        self.root.geometry("400x300")  # Set the window size

        tk.Button(root, text="View Items", width=20, command=self.view_items).pack(pady=10)
        tk.Button(root, text="Add Item", width=20, command=self.add_item).pack(pady=10)
        tk.Button(root, text="Delete Item", width=20, command=self.delete_item).pack(pady=10)

    def add_item(self):
        name = simpledialog.askstring("Food Name", "Enter food name:")
        if not name:
            return
        entry_date = simpledialog.askstring("Entry Date", "Enter entry date (YYYY-MM-DD):")
        expire_date = simpledialog.askstring("Expire Date", "Enter expire date (YYYY-MM-DD):")

        try:
            datetime.strptime(entry_date, "%Y-%m-%d")
            datetime.strptime(expire_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Date Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        cursor.execute("INSERT INTO food VALUES (?, ?, ?)", (name, entry_date, expire_date))
        conn.commit()
        messagebox.showinfo("Success", f"{name} added.")

    def delete_item(self):
        name = simpledialog.askstring("Food Name", "Enter name of food to delete:")
        if not name:
            return
        cursor.execute("DELETE FROM food WHERE name = ?", (name,))
        conn.commit()
        messagebox.showinfo("Deleted", f"{name} removed (if it existed).")

    def view_items(self):
        window = tk.Toplevel(self.root)
        window.title("Food Items")

        now = datetime.now().date()
        cursor.execute("SELECT rowid, name, entry_date, expire_date FROM food")
        items = cursor.fetchall()

        row = 0
        for rowid, name, entry_date, expire_date in items:
            try:
                expire = datetime.strptime(expire_date, "%Y-%m-%d").date()
            except ValueError:
                continue

            days_left = (expire - now).days
            if days_left < 0:
                cursor.execute("DELETE FROM food WHERE rowid = ?", (rowid,))
                conn.commit()
                messagebox.showwarning("Expired", f"{name} has expired and was removed.")
                continue

            frame = tk.Frame(window, width=400)
            frame.grid(row=row, column=0, sticky="w", pady=5, padx=10)

            if days_left > 14:
                bg_color = "lightgreen"
            elif days_left >= 7:
                bg_color = "yellow"
            else:
                bg_color = "red"

            tk.Label(frame, text=f"{name} - Expires in {days_left} days", bg=bg_color, width=40).pack()
            row += 1

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FoodApp(root)
    root.mainloop()
