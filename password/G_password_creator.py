import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return
        
        letters = string.ascii_letters
        nums = string.digits
        sings = string.punctuation
        stuffs = letters + nums + sings

        # Ensure the password includes at least one letter, digit, and symbol
        password = (
            random.choice(letters) +
            random.choice(nums) +
            random.choice(sings) +
            "".join(random.choices(stuffs, k=length - 3))
        )
        password = "".join(random.sample(password, len(password)))

        # Display the generated password
        label_result.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create widgets
label_instruction = tk.Label(root, text="Enter the length of your password:", font=("Arial", 12))
label_instruction.pack(pady=10)

entry_length = tk.Entry(root, width=10, font=("Arial", 12))
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
button_generate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=10)

# Run the application
root.mainloop()
