# frontend/calculator_gui.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.calculator import add, subtract, multiply, divide
import tkinter as tk

# Function to handle button clicks
def button_click(value):
    entry_var.set(entry_var.get() + str(value))

# Function to clear input
def clear():
    entry_var.set("")

# Function to calculate the result
def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression, {"__builtins__": None}, 
                      {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide})
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

# Create main window
root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and place buttons
for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 15), bg="lightgreen", command=calculate)
    else:
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 15), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Create clear button
clear_btn = tk.Button(root, text="C", width=10, height=2, font=("Arial", 15), bg="lightcoral", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4)

# Run application
root.mainloop()
