import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# ...existing code...

button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

for choice in choices:
    btn = tk.Button(button_frame, text=choice, width=10, font=("Arial", 12),
                    command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=5)

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}") # type: ignore

root = tk.Tk()
root.title("Rock Paper Scissors")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack()

result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()