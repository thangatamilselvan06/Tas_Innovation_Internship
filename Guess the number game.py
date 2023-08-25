import tkinter as tk
import random

def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    info_label.config(text="New game started! Guess a number between 1 and 100.")
    guess_entry.delete(0, "end")

def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < secret_number:
            info_label.config(text="Try a higher number.")
        elif guess > secret_number:
            info_label.config(text="Try a lower number.")
        else:
            info_label.config(text=f"Congratulations! You guessed the number {secret_number}.")
    except ValueError:
        info_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Guess the Number Game")

info_label = tk.Label(root, text="Welcome to Guess the Number! Click 'Start New Game' to begin.")
info_label.pack()

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack()

new_game_button = tk.Button(root, text="Start New Game", command=new_game)
new_game_button.pack()

new_game()

root.mainloop()
