"""
File: 04_user_input.py
Author: Kole Bauer
Date: 12 August 2025
Description: Demonstrates the use of the input() function to get user input in Python.
"""

# The input() function pauses the program execution and waits for the user to type something.
# Whatever the user types is returned as a string.


# -------------------------------------------------------
# Example 1: Basic input
# -------------------------------------------------------
name = input("Enter your name: ")
print()
print(f"Hello, {name}!")
print()


# -------------------------------------------------------
# Example 2: Input is always a string
# -------------------------------------------------------
# Even if the user types a number, input() still returns it as a string.
age_input = input("Enter your age: ")
print()
print(f"You said your age is {age_input}.")
print()
print(f"Type of age_input: {type(age_input)}.")
print()


# -------------------------------------------------------
# Example 3: Converting input to a number
# -------------------------------------------------------
# If you need to do math with input, convert it using int() or float()
age = int(age_input)
years_until_30 = 30 - age
print(f"You will be 30 in {years_until_30} years.\n \n \n \n")