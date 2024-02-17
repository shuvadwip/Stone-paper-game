import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choose: Rock, Paper, or Scissors")
        self.label.pack(pady=10)

        self.choices = ["Rock", "Paper", "Scissors"]

        for choice in self.choices:
            button = tk.Button(self.master, text=choice, command=lambda c=choice: self.play_game(c))
            button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.master, text="Score: User - 0 | Computer - 0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play_game(self, user_choice):
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        result_text = f"User: {user_choice} | Computer: {computer_choice}\nResult: {result}"

        self.result_label.config(text=result_text)

        self.update_score(result)

        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Scissors" and computer_choice == "Paper")
            or (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if "You win" in result:
            self.user_score += 1
        elif "Computer wins" in result:
            self.computer_score += 1

    def update_score_label(self):
        score_text = f"Score: User - {self.user_score} | Computer - {self.computer_score}"
        self.score_label.config(text=score_text)

    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.update_score_label()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
