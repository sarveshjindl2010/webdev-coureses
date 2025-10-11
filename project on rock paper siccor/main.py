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

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}") # type: ignore

root = tk.Tk()
root.title("Rock Paper Scissors")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()
frame.place(x=50, y=60)
title_label = tk.Label(frame, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack()
title_label.place(x=80, y=10)
result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.pack()
result_label.place(x=70, y=200)
root.mainloop()