import random
import tkinter as tk

# Predefined list of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.word = random.choice(words)
        self.word_length = len(self.word)
        self.display = ["_"] * self.word_length
        self.incorrect_guesses = 0
        self.guessed_letters = []

        # Create GUI elements
        self.word_label = tk.Label(master, text=" ".join(self.display), font=("Arial", 24))
        self.word_label.pack()

        self.guesses_label = tk.Label(master, text="Incorrect guesses remaining: 6", font=("Arial", 18))
        self.guesses_label.pack()

        self.guessed_letters_label = tk.Label(master, text="Guessed letters:", font=("Arial", 18))
        self.guessed_letters_label.pack()

        self.guessed_letters_text = tk.Text(master, height=5, width=20, font=("Arial", 12))
        self.guessed_letters_text.pack()

        self.guess_entry = tk.Entry(master, width=20, font=("Arial", 18))
        self.guess_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.word:
            for i in range(self.word_length):
                if self.word[i] == guess:
                    self.display[i] = guess
        else:
            self.incorrect_guesses += 1
            self.guessed_letters.append(guess)

        self.word_label.config(text=" ".join(self.display))
        self.guesses_label.config(text=f"Incorrect guesses remaining: {6 - self.incorrect_guesses}")
        self.guessed_letters_text.insert(tk.END, guess + "\n")

        if "_" not in self.display:
            self.word_label.config(text="Congratulations, you won!")
            self.guess_button.config(state="disabled")
        elif self.incorrect_guesses == 6:
            self.word_label.config(text=f"Game over! The word was {self.word}.")
            self.guess_button.config(state="disabled")

root = tk.Tk()
root.title("Hangman Challenge")
game = HangmanGame(root)
root.mainloop()