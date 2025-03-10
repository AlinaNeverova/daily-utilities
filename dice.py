"""
Dice Rolling Simulator
This simple program simulates rolling a six-sided dice. 
"""

import numpy as np

while True:                                                  # The option to roll the dice again will be offered again after each attempt
    user_input = input("Roll the dice: ")
    if user_input == "":                                     # To roll a die, just press Enter
        np.random.randint(1,7)
        print("There's a number: ", np.random.randint(1,7))
    else:
        print("The end")                                     # The game will be interrupted if you enter any character
        break