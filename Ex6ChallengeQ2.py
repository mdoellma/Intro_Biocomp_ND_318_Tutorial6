# Using control structures in Python

import numpy as np


computer_number = np.random.randint(101)
user_number = -10
while user_number != computer_number50:  
    user_number = int(raw_input("Guess a number between 1 and 100: "))
    if user_number > computer_number:
        print("TOO HIGH NERD")
    elif user_number < computer_number:
        print("That's way too low.")
        
print("You won the game!")