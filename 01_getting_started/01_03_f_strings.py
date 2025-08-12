"""
File: 03_f_strings.py
Author: Kole Bauer
Date: 12 August 2025
Description: Demonstrates the use of f-strings (formatted string literals) in Python
"""

# f-strings allow you to insert the values of variables directly into a string.
# This is called "string interpolation" - the placeholders inside the string are replaced with actual values at runtime.
# f-strings are created by placing an "f" or "F" before the opening quote of the string.


# -------------------------------------------------------
# Example 1: Old way - string concatenation
# -------------------------------------------------------
# Concatenation combines strings using the + operator.

name = "Kole"
age = 24
print("My name is " + name + " and I am " + str(age) + " years old.")

print() # Note: an empty print statement will print a new line.

# While this works, it can become messy and requires explicit type conversion (str(age)) for non-string values.


# -------------------------------------------------------
# Example 2: New way - f-strings
# -------------------------------------------------------
# With f-strings, variables can be inserted directly into the string without explicit conversion or arithmetic operators.

print(f"My name is {name} and I am {age} years old.")

print("") # A print statement with empty quotes will also print a new line

print(F"My name is {name} and I am {age} years old.")

# As shown above, both a lowercase "f" and an uppercase "F" work to initialize an f-string.
