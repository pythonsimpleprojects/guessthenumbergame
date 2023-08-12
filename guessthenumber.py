import random
import tkinter as tk

class GuessTheNumberGUI:
    def __init__(self, master):
        # Initialize the GUI window
        self.master = master
        master.title("Guess The Number")

        # Generate a random number between 1 and 100
        self.number = random.randint(1, 100)

        # Initialize the guess variable to 0
        self.guess = 0

        # Create the guess label and entry box
        self.guess_label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.guess_label.pack()
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        # Create the guess button
        self.guess_button = tk.Button(master, text="Guess", command=self.submit)
        self.guess_button.pack()

        # Create the result label
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def submit(self):
        # Get the guess from the entry box and convert it to an integer
        self.guess = int(self.guess_entry.get())

        # Compare the guess to the random number and update the result label
        if self.guess > self.number:
            self.result_label.config(text="Try to guess lower")
        elif self.guess < self.number:
            self.result_label.config(text="Try to guess higher")
        else:
            self.result_label.config(text="You won!")

# Create the main window
root = tk.Tk()

# Create the GuessTheNumberGUI object
my_gui = GuessTheNumberGUI(root)

# Start the main loop
root.mainloop()