import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def estimate_body_fat(bmi):
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obese (Class 1)"
    elif 35 <= bmi < 39.9:
        return "Obese (Class 2)"
    else:
        return "Severely obese (Class 3)"

def calculate_and_display():
    try:
        weight_input = float(weight_entry.get())
        height_input = float(height_entry.get())
        weight_unit = weight_var.get()
        height_unit = height_var.get()

        if weight_unit == 2:
            weight_input = pounds_to_kg(weight_input)

        if height_unit == 2:
            feet = int(height_entry_feet.get())
            inches = int(height_entry_inches.get())
            height_input = feet_inches_to_meters(feet, inches)

        bmi = calculate_bmi(weight_input, height_input)
        body_fat = estimate_body_fat(bmi)

        result_label.config(text=f"Your BMI: {bmi:.2f}\nBody Fat Category: {body_fat}")

        # Store history
        history.append((weight_input, height_input, bmi, body_fat))
        update_history_listbox()

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid values.")

def update_history_listbox():
    history_listbox.delete(0, tk.END)
    for entry in history:
        history_listbox.insert(tk.END, f"Weight: {entry[0]} kg, Height: {entry[1]} m, BMI: {entry[2]:.2f}, Category: {entry[3]}")

# Conversion functions

def pounds_to_kg(pounds):
    return pounds * 0.453592

def feet_inches_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 0.0254

# Create GUI
root = tk.Tk()
root.title("BMI Calculator")

weight_var = tk.IntVar()
height_var = tk.IntVar()

history = []

weight_label = tk.Label(root, text="Weight:")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

weight_units_frame = tk.Frame(root)
weight_units_frame.pack()

kg_radio = tk.Radiobutton(weight_units_frame, text="kg", variable=weight_var, value=1)
kg_radio.pack(side=tk.LEFT)

lb_radio = tk.Radiobutton(weight_units_frame, text="lb", variable=weight_var, value=2)
lb_radio.pack(side=tk.LEFT)

height_label = tk.Label(root, text="Height:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

height_units_frame = tk.Frame(root)
height_units_frame.pack()

meters_radio = tk.Radiobutton(height_units_frame, text="m", variable=height_var, value=1)
meters_radio.pack(side=tk.LEFT)

feet_radio = tk.Radiobutton(height_units_frame, text="ft", variable=height_var, value=2)
feet_radio.pack(side=tk.LEFT)

height_entry_feet_label = tk.Label(root, text="Feet:")
height_entry_feet_label.pack()

height_entry_feet = tk.Entry(root)
height_entry_feet.pack()

height_entry_inches_label = tk.Label(root, text="Inches:")
height_entry_inches_label.pack()

height_entry_inches = tk.Entry(root)
height_entry_inches.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

history_label = tk.Label(root, text="History:")
history_label.pack()

history_listbox = tk.Listbox(root, width=50)
history_listbox.pack()

update_history_listbox()

root.mainloop()
