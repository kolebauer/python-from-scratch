"""
File: 01_05_mini_project.py
Author: Kole Bauer
Date: 12 August 2025
Description: Mini project for Module 01 - Getting Started with Python.
Creates a personalized day plan using basic input, variables, type conversion, and f-strings.
Project prompt and structure collaboratively developed with OpenAI's GPT-5 model.
"""

# -------------------------------------------------------
# 1. Title & Introduction
# -------------------------------------------------------
# Print a welcome message for the planner.
# Add a blank line for readability.
welcome_message = "Hello, and welcome to Py Project Planner!"
print()
print(welcome_message)
print()


# -------------------------------------------------------
# 2. Gather Information
# -------------------------------------------------------
# Prompt the user for:
# - Their name
# - The current day of the week
# - The number of hours they have free today
# - Their favorite activity or hobby
name = input("Please enter your first name: ")
print()
current_day = input("Please enter the current day of the week: ")
print()
free_time_hours = input("Please enter the number of hours you have free today: ")
print()
favorite_activity = input("Please enter your favorite activity or hobby: ")
print()


# -------------------------------------------------------
# 3. Data Handling
# -------------------------------------------------------
# Store inputs in variables.
# Convert numeric inputs to integers or floats as needed.
float_free_time_hours = float(free_time_hours)


# -------------------------------------------------------
# 4. Basic Calculations
# -------------------------------------------------------
# - Calculate hours spent on favorite activity (half of free time)
# - Calculate hours remaining for other tasks
free_time_activity_hours = float_free_time_hours / 2
other_tasks_hours = free_time_activity_hours


# -------------------------------------------------------
# 5. Formatted Output
# -------------------------------------------------------
# Use f-strings to display:
# - Name
# - Day of the week
# - Hours for favorite activity
# - Remaining hours
# Include at least one uppercase and one lowercase f in your f-strings.
print(f"Thanks {name}!") 
print()
print(F"Based on my calculations, this {current_day}, you have {free_time_activity_hours} hours to enjoy {favorite_activity}, and {other_tasks_hours} hours to work on any other tasks.")


# -------------------------------------------------------
# 6. Visual Formatting
# -------------------------------------------------------
# Add blank lines for readability.
print()
print("")


# -------------------------------------------------------
# Stretch Goals
# -------------------------------------------------------
# There are no stretch goals for Module 01.
# In future modules, stretch goals will provide optional challenges that expand on the concepts covered in that module.