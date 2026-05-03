import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Length Converter App")  # (as required, even though it's RPS)
root.geometry("400x400")

# Function to decide winner
def play(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    )

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack(pady=20)

# Buttons
rock_btn = tk.Button(root, text="Rock", width=10, command=lambda: play("rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=10, command=lambda: play("paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run app
root.mainloop()