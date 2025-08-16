"""
File: 02_02_string_methods.py
Author: Kole Bauer
Date: 16 August 2025
Description: Demonstrates common string methods for formatting and analyzing text.
"""


# Strings in Python have many built-in "methods" that allow you to change their appearance or analyze their content.
# A method is like a small tool that belongs to an object, in this case a string variable.
# You "call" or use a method by using "dot notation," like: variable.method()


# -------------------------------------------------------
# Example 1: Capitalization methods
# -------------------------------------------------------
# .capitalize(), .title(), .upper(), .lower()

words = "sally SELLS SEASHELLS on The seashORE."

# .capitalize() makes only the first character uppercase, and the rest lowercase.
print(words.capitalize(), "\n")     # "\n or newline to clean up the output: "Sally sells seashells on the seashore."

# .title() capitalizes the first letter in each word, which is called "Title Case"
print(words.title(), "\n")      # Sally Sells Seashells On The Seashore.""

# .upper() makes every letter in the string uppercase.
print(words.upper(), "\n")      # "SALLY SELLS SEASHELLS ON THE SEASHORE."

# .lower() behaves the same as .upper(), but makes all letters in the string lowercase.
print(words.lower(), "\n")      # "sally sells seashells on the seashore."


# -------------------------------------------------------
# Example 2: Counting substrings and chaining methods.
# -------------------------------------------------------
# .count() counts how many times a substring (like a letter, a space, or a word) appears.
print(words.count("s"))     # 3 (counts only instances of lowercase "s")

# Combine or "chain" two or more string methods like .lower() and .count() to count "s" regardless of case.
print(words.lower().count("s"), "\n")     # 8 (each capital "S" was converted to lowercase "s" and then all "s" were counted.)

# Why this matters:
# Counting is helpful when analyzing text, like checking how often a keyword appears in a document or validating user input.


# -------------------------------------------------------
# Example 3: Stripping whitespace
# -------------------------------------------------------
#.strip() removes spaces from the beginning and end of a string.
messy = "       Python ROCKS!    "
print(messy, "\n")
print(messy.strip(), "\n")

# Chaining methods again, we can take the value stored in the "messy", remove whitespace, and lowercase the result.
print(messy.strip().lower(), "\n")

# Why this matters:
# User in can and will be messy. It may have extra spaces, or inconsistent capitalization.
# Cleaning text before saving or comparing makes your program more reliable.


# -------------------------------------------------------
# Practice Section (filled by Kole) *in progress*
# -------------------------------------------------------