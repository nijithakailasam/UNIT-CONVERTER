import tkinter as tk
from tkinter import ttk

# Conversion rates relative to meters
conversion_rates = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Miles": 0.000621371,
    "Feet": 3.28084
}

def convert():
    try:
        value = float(entry.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        # Convert to meters first
        value_in_meters = value / conversion_rates[from_unit]
        result = value_in_meters * conversion_rates[to_unit]
        
        label_result.config(text=f"{value} {from_unit} = {round(result, 4)} {to_unit}")
    except ValueError:
        label_result.config(text="Enter a valid number!")

# Main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x250")

# Input
tk.Label(root, text="Enter value:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

# From unit
tk.Label(root, text="From:", font=("Arial", 12)).pack()
combo_from = ttk.Combobox(root, values=list(conversion_rates.keys()), state="readonly")
combo_from.set("Meters")
combo_from.pack(pady=5)

# To unit
tk.Label(root, text="To:", font=("Arial", 12)).pack()
combo_to = ttk.Combobox(root, values=list(conversion_rates.keys()), state="readonly")
combo_to.set("Kilometers")
combo_to.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert).pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14), fg="blue")
label_result.pack(pady=10)

root.mainloop()
