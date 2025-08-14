"""
File: 02_01_print_parameters.py
Author: Kole Bauer
Date: 14 August 2025
Description: Demonstrates the use of print() parameters such as sep and end to
produce cleaner, more intentional console output.
"""

# The print() function can display multiple pieces of information at once.
# By default, Python separates these pieces with a space and ends the output with a newline.
# The sep (separator) parameter controls what appears between multiple arguments, and the end parameter controls what is printed at the very end.
# Customizing these parameters allows you to format console output for clarity, create clean single-line status updates, or build simple tables without extra code.

# -------------------------------------------------------
# Example 1: Default behavior vs. custom separators (sep)
# -------------------------------------------------------
# The sep (separator) parameter controls what appears between multiple arguments.
# Default: a single space.
print("Python", "is", "fun")  # Default separator: space

# Custom separators help create compact or styled output.
print("Python", "is", "fun", sep="-")
print("2025", "08", "14", sep="/")   # Date-style formatting
print("A", "B", "C", sep=" | ")      # Visually distinct columns


# -------------------------------------------------------
# Example 2: Controlling the line ending (end)
# -------------------------------------------------------
# By default, print() ends with a newline "\n".
# The end parameter lets you change or remove that newline.
print("Loading", end="...")  # No newline yet; next print continues the line
print("done!")               # Appears on the same line: Loading...done!

# You can also end with a custom marker + newline.
print("Step 1 complete", end=" ✔\n")
print("Step 2 complete", end=" ✔\n")


# -------------------------------------------------------
# Example 3: Building a line progressively
# -------------------------------------------------------
# Printing small pieces on one line can improve readability for status messages.
print("Task:", end=" ")
print("Download", end=" -> ")
print("Validate", end=" -> ")
print("Save")

# Be careful: forgetting a final newline can cause the next output to butt up
# against this line. Ending with print() (no args) inserts a newline.
print()  # Insert a clean blank line


# -------------------------------------------------------
# Example 4: Using sep and end together intentionally
# -------------------------------------------------------
# Combine sep for inner spacing and end to control trailing characters.
print("Item", "Qty", "Price", sep=" | ", end="\n---------------------------\n")
print("Notebook", 2, "$3.50", sep=" | ")
print("Pen", 1, "$1.20", sep=" | ")
print("---------------------------")

# Another pattern: print a label and value on one line without extra spaces.
print("Total:", end=" ")  # No trailing newline yet
print("$8.20")


# -------------------------------------------------------
# Example 5: Common pitfalls (and fixes)
# -------------------------------------------------------
# 1) Unwanted spaces when mixing strings and numbers:
#    Multiple arguments already insert the separator (default space). Avoid manual spaces
#    inside strings unless you need them.
print("Count:", 3)           # Clean
print("Count: ", 3)          # Works, but adds an extra space after ':'

# 2) Run-on lines from reusing end without a newline later:
print("Processing", end="...")  # No newline yet
# print("Next message starts here")  # Would run on the same line if uncommented
print()  # Fix: add a newline before the next unrelated output
print("Ready for next step.")


# -------------------------------------------------------
# Practice (optional): Try these on your own
# -------------------------------------------------------
# 1) Print the words Monday, Tuesday, Wednesday on one line separated by commas (", ").
# 2) Print "Ready", "Set", "Go!" on one line with arrows between them (e.g., "Ready -> Set -> Go!").
# 3) Print "Start:" and "Finish." so that both appear on the same line with a space between.
# 4) Create a tiny two-row "table" header with a custom sep for alignment hints.
# (Type your attempts below this comment to keep the examples above runnable as-is.)