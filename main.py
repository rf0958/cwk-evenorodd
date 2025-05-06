# Is It Even Or Odd? - Coding With Kids Level 4
# Made by @Rf0958 (Riker) on Github.
# https://github.com/rf0958
# Last Changes Saved on 5.5.2025

import sys

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    print("Welcome to Is it Even Or Odd!")
    print() # Blank Line
    get_number = int(input("Please Enter A Number: "))
    print(even_or_odd(get_number)) # Based on my knowledge with functions in Python, this should work???

if __name__ == "__main__":
    while True:
        main()
        choice = input("Do you want to enter another number?: ")
        if not choice.lower().startswith("y"):
            sys.exit() # It could be break but I like sys.exit more.


