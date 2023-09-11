import tkinter as tk
import math

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def insert_text(text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + text)

def calculate_sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_sin():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_cos():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_tan():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create an entry widget to display and input expressions
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=6)

# Create buttons for digits and operations
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'sqrt'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20,
              command=lambda btn=button: insert_text(btn) if btn != '=' else evaluate_expression() if btn == '=' else None,
              ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Create clear button
tk.Button(root, text="Clear", padx=20, pady=20, command=clear).grid(row=5, column=0, columnspan=2)

# Start the GUI main loop
root.mainloop()
