import tkinter as tk
from tkinter import ttk
import random

# Function to roll dice
def roll_dice():
    num_dice = int(dice_count_var.get())  # Get number of dice from dropdown
    rolls = [random.randint(1, 6) for _ in range(num_dice)]  # Roll dice
    result_label.config(text=f"🎲 Rolls: {', '.join(map(str, rolls))}")  # Update UI

# Create main window
root = tk.Tk()
root.title("Dice Roller 🎲")
root.geometry("300x200")

# Title Label
title_label = tk.Label(root, text="Roll the Dice!", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Dropdown for number of dice
dice_count_var = tk.StringVar(value="1")  # Default to 1 dice
dice_options = [str(i) for i in range(1, 7)]  # Options: 1 to 6 dice
dice_dropdown = ttk.Combobox(root, textvariable=dice_count_var, values=dice_options, state="readonly")
dice_dropdown.pack(pady=5)

# Roll Button
roll_button = tk.Button(root, text="Roll 🎲", font=("Arial", 12, "bold"), command=roll_dice)
roll_button.pack(pady=10)

# Label to Display Result
result_label = tk.Label(root, text="🎲 Rolls: ", font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI Loop
root.mainloop()
