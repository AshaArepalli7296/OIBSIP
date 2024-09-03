import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import random
import string

# Define character sets
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_+-=;:,.<>?'

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = lower_case
    if use_uppercase:
        characters += upper_case
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = []
    if use_uppercase:
        password.append(random.choice(upper_case))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_symbols:
        password.append(random.choice(symbols))

    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choice(characters) for _ in range(remaining_length))

    random.shuffle(password)
    return ''.join(password)

def on_generate():
    try:
        length = int(length_combobox.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        if length <= 0:
            raise ValueError("Password length must be greater than 0")

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    password = password_var.get()
    if password:
        head.clipboard_clear()
        head.clipboard_append(password)
        head.update()  
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
head = tk.Tk()
head.title("Password Generator")
head.geometry("1000x700") 
head.configure(bg='DarkTurquoise')  

# Title Label
tk.Label(head, text="  PASSWORD GENERATOR  ", font=("Arial Bold ", 32), bg='white', fg='Black').pack(pady=20)

# Input frame
input_frame = tk.Frame(head, bg='#e1e1e1')
input_frame.pack(pady=20)

# Password Length
tk.Label(input_frame, text="Password Length:", font=("Arial", 16), bg='#e1e1e1').pack(anchor='w', padx=20)
length_options = [str(i) for i in range(8, 21)]  # Length options from 8 to 20
length_combobox = ttk.Combobox(input_frame, values=length_options, width=15, font=("Arial", 16))
length_combobox.set('12')  # Default value
length_combobox.pack(padx=20)

# Checkbox variables
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# Checkbuttons for options
tk.Checkbutton(input_frame, text="Include Uppercase Letters", variable=uppercase_var, bg='#e1e1e1', font=("Arial", 14)).pack(anchor='w', padx=20, pady=5)
tk.Checkbutton(input_frame, text="Include Numbers", variable=numbers_var, bg='#e1e1e1', font=("Arial", 14)).pack(anchor='w', padx=20, pady=5)
tk.Checkbutton(input_frame, text="Include Symbols", variable=symbols_var, bg='#e1e1e1', font=("Arial", 14)).pack(anchor='w', padx=20, pady=5)

# Generate button
tk.Button(head, text="Generate Password", command=on_generate, bg='#4a90e2', fg='white', font=("Arial", 16)).pack(pady=20)

# Generated Password Label
tk.Label(head, text="  Generated Password  ", font=("Arial", 18), bg='#f0f0f0').pack(pady=10)
password_var = tk.StringVar()
password_entry = tk.Entry(head, textvariable=password_var, width=50, font=("Arial", 16), state='readonly')
password_entry.pack(pady=10)

# Copy to Clipboard button
tk.Button(head, text="Copy to Clipboard", command=copy_to_clipboard, bg='#4a90e2', fg='white', font=("Arial", 16)).pack(pady=20)

# Run the application
head.mainloop()







