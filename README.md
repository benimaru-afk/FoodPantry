# 🥫 NMT Pantry Food Tracker

A simple desktop application built in Python using Tkinter and SQLite to help manage and track food inventory at the **New Mexico Tech Pantry**. This tool allows pantry volunteers to quickly add, view, and remove food items while keeping track of expiration dates with a color-coded system for food safety.

---

## 🎯 Project Goal

The goal of this application is to:

- **Improve food inventory management** at the NMT Pantry.
- **Reduce waste** by alerting users before food expires.
- **Maintain food safety** standards by ensuring expired items are removed automatically.
- **Provide a user-friendly interface** for volunteers with minimal technical knowledge.

STUDENT SYSTEM: open webapp (to be built soon...)
---

ADMIN SYSTEM: running an exe
---

## 🧰 Features

- **Add Items**  
  Input the food name, entry date, and expiration date.

- **View Items**  
  View all current items with a color-coded expiration system:
  - 🟩 Green: More than 2 weeks left
  - 🟨 Yellow: Between 1–2 weeks
  - 🟥 Red: Less than 1 week
  - ⚠️ Auto-removal of expired items with a warning popup

- **Delete Items**  
  Manually remove a food item by name.

---

## 🗃️ How It Works

1. Launch the app.
2. Click `Add Item` to log new pantry stock.
3. Click `View Items` to check current food and time left before expiration.
4. Click `Delete Item` to manually remove items.
5. Expired items are **automatically removed** with a user alert.

All data is stored locally in a **SQLite database** (`food_items.db`).

---

## 🖥️ Requirements

- Python 3.x
- Tkinter (included with standard Python)
- SQLite3 (standard Python module)

---

## 📦 Setup Instructions

1. Clone this repository or download the `.py` file.
2. Run the Python file:
   ```bash
   python food_tracker.py

## EXE Creation

1. In terminal/powershell, install 'pyinstaller' with 'pip install pyinstaller'
2. run the command:
```bash
'pyinstaller --onefile -w 'filename.py' '
