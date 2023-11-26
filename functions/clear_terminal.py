# a function that clears the terminal on all the operating systems , (you can use it to hide some infos or inputs after the user types in a special caractere)
import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
