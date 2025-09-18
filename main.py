import tkinter as tk
from tkinter import messagebox
import datetime
import random

# Simulated RFID cards
rfid_cards = {
    "123ABC": "Alice",
    "456DEF": "Bob",
    "789GHI": "Charlie"
}

# Attendance log
attendance_log = []

# Function to simulate scanning a card
def scan_card():
    card = random.choice(list(rfid_cards.keys()))
    name = rfid_cards[card]
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attendance_log.append((name, now))
    update_log()
    messagebox.showinfo("Card Scanned", f"{name} scanned at {now}")

# Update the Tkinter listbox with attendance log
def update_log():
    log_listbox.delete(0, tk.END)
    for entry in attendance_log:
        log_listbox.insert(tk.END, f"{entry[0]} - {entry[1]}")

# Create main window
root = tk.Tk()
root.title("IoT Attendance System Simulator")
root.geometry("400x400")

# Scan button
scan_button = tk.Button(root, text="Scan Card", command=scan_card, font=("Arial", 14))
scan_button.pack(pady=20)

# Attendance log listbox
log_listbox = tk.Listbox(root, width=50)
log_listbox.pack(pady=10)

root.mainloop()
