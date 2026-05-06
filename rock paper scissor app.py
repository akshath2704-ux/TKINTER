import tkinter as tk
import random
from tkinter import font
root = tk.Tk()
root.title("Length Converter App")  
root.geometry("400x400")  
root.resizable(False, False)
root.configure(bg="white")

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice):
    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result = "It's a tie!"
        result_label.config(fg="orange")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        result_label.config(fg="green")
    else:
        result = "Computer wins!"
        result_label.config(fg="red")
    
    result_label.config(text=result)


title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=11)
title_label = tk.Label(root, text="Rock Paper Scissors", font=title_font, bg="white")
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)
rock_btn = tk.Button(button_frame, text="Rock ", font=button_font, width=10, 
                     command=lambda: determine_winner("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper ", font=button_font, width=10, 
                      command=lambda: determine_winner("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors ", font=button_font, width=10, 
                         command=lambda: determine_winner("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)
user_choice_label = tk.Label(root, text="Your choice: ", font=label_font, bg="white")
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=label_font, bg="white")
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Click a button to play!", font=title_font, bg="white")
result_label.pack(pady=20)
reset_btn = tk.Button(root, text="Play Again", font=button_font, 
                      command=lambda: [user_choice_label.config(text="Your choice: "),
                                      computer_choice_label.config(text="Computer's choice: "),
                                      result_label.config(text="Click a button to play!", fg="black")])
reset_btn.pack()
root.mainloop()