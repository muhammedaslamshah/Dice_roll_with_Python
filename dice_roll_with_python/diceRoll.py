'''
The "Dice Roll" project is a straightforward and cleanly coded Python
program that emulates rolling a six-sided die. Users can repeatedly
roll the die with the 'Enter' key and exit the program by typing 'Q'. 
This uncomplicated script delivers an enjoyable and interactive gaming
experience.

'''

import random


def DiceRoll():
    dice_sides = 6
    rolling = True

    while rolling:
        roll_cmnd = input("Do you want to roll again the Dice?...\n Enter Enter- roll. \n Q- Quit \n\n")
        if roll_cmnd.lower() != "q":
            rolled_value = random.randint(1, dice_sides)
            rolling = True
            print("You have rolled: \n", rolled_value)
        else:
            rolling = False
    print(" \n Thanks for Playing \n")
DiceRoll()