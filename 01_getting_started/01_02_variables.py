"""
File: 02_variables.py
Author: Kole Bauer
Date: 11 August 2025
Description: Demonstrates the basic function of variables in Python
"""

# Variables act as containers that store values in memory.
# The value inside can change (unless defined as a constant by convention).
# Variables can hold different data types such as strings, integers, and floats.

# -------------------------------------------------------
# Example 1: Naming variables
# -------------------------------------------------------
# Good variable names make code easier to read and maintain.
# Bad naming slows you down when revisiting old code and when documenting your code.

a = 20.5   # Example of a poor, unclear name
average_fuel_economy_mpg = 20.5   # Example of a descriptive name


# -------------------------------------------------------
# Example 2: Basic data types
# -------------------------------------------------------

# Strings are sequences of text characters. 
# They are enclosed in either double quotes (" ") or single quotes (' ').
# Both work the same in Python, but you should be consistent in your code style.
name = "Kole"
nickname = 'KB'

# Integers are whole numbers without a decimal point.
age = 24

# Floats are numbers that contain a decimal point.
height_in_feet = 6.02

# Booleans represent one of two values: True or False.
is_student = True

# Check the type of each variable
print(type(name))
print(type(age))
print(type(height_in_feet))
print(type(is_student))


# -------------------------------------------------------
# Example 3: Basic arithmetic with numbers
# -------------------------------------------------------

# Arithmetic operators in Python:
# + (addition), - (subtraction), * (multiplication), / (division)

# Let's work with some numeric variables:
x = 10
y = 4

# Addition
print(x + y)   # 14

# Subtraction
print(x - y)   # 6

# Multiplication
print(x * y)   # 40

# Division (returns a float, even if numbers divide evenly)
print(x / y)   # 2.5

# Integer (floor) division - discards any remainder
print(x // y)  # 2

# Modulus -  gives the remainder after division
print(x % y)   # 2

# Note: Arithmetic with strings
# -------------------------------------------------------
# If a number is wrapped in quotes, Python treats it as a string, not a number.
# Adding strings together will concatenate (join) them end-to-end instead of performing math.

num1 = "10"
num2 = "4"

print(num1 + num2)  # "104" - concatenation, NOT addition

# To perform math with these, you must store them as numbers (int or float) instead of strings.


# -------------------------------------------------------
# Example 4: Type conversion
# -------------------------------------------------------
# Sometimes you'll need to change a value from one data type to another.
# This is called "type conversion" or "casting."

# Converting a string to an integer
num_str = "10"
num_int = int(num_str)   # int() converts to an integer
print(num_int + 5)       # 15

# Converting a string to a float
price_str = "19.99"
price_float = float(price_str)   # float() converts to a decimal number
print(price_float + 5)           # 24.99

# Converting a number to a string
age = 24
age_str = str(age)   # str() converts to a string
print("I am " + age_str + " years old.")  # Works because both are strings now

# You can also check a variable's type using type()
print(type(num_str))   # <class 'str'>
print(type(num_int))   # <class 'int'>