import tkinter as tk
from tkinter import ttk

def check_strength():
    password = password_entry.get()
    length = len(password)
    
    if length == 0:
        strength = "Enter a password"
        color = "gray"
    elif length < 6:
        strength = "Very Weak"
        color = "red"
    elif length < 8:
        strength = "Weak" 
        color = "orange"
    elif length < 12:
        strength = "Medium"
        color = "yellow"
    elif length < 16:
        strength = "Strong"
        color = "green"
    else:
        strength = "Very Strong"
        color = "blue"
    
    result_label.config(text=f"Strength: {strength}", foreground=color)
    progress_bar['value'] = min(length * 6.25, 100) 
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

title_label = ttk.Label(main_frame, text="Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=(0, 15))

ttk.Label(main_frame, text="Enter Password:").pack(anchor="w")

password_entry = ttk.Entry(main_frame, show="*", width=30, font=("Arial", 11))
password_entry.pack(pady=5, fill="x")
password_entry.bind("<KeyRelease>", lambda e: check_strength()) 

progress_bar = ttk.Progressbar(main_frame, length=300, mode='determinate')
progress_bar.pack(pady=10, fill="x")

result_label = ttk.Label(main_frame, text="Strength: Enter a password", font=("Arial", 11))
result_label.pack(pady=5)

check_strength()

root.mainloop()