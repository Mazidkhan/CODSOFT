import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry.get())
    
    if length < 1:
        messagebox.showerror("Invalid Length", "Password length must be at least 1.")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x400")
root.resizable(False,False)

# Create label and entry for password length
label = tk.Label(root, text="Enter Password Length:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# Create button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create label to display generated password
password_label = tk.Label(root, text="")
password_label.pack(pady=10)

# Start the main event loop
root.mainloop()
