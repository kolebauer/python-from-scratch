"""
File: 02_03_escape_sequences.py
Author: Kole Bauer
Date: 16 August 2025
Description: Introduces common escape sequences for special characters in strings (\n, \t, \\, \", \') and explains when to use them.
"""

# Escape sequences let you include characters in a string that would otherwise be hard to type or read. The backslash \ starts a special code like \n for a newline or \t for a tab. Use them to control layout or to print quotes/backslashes.

# -------------------------------------------------------
# Example 1: Newlines with \n
# -------------------------------------------------------
# WHY: Format multi-line output without many print() calls.
# TODO: show a short poem/menu printed with \n
# print("Line 1\nLine 2\nLine 3")

# -------------------------------------------------------
# Example 2: Tabs with \t
# -------------------------------------------------------
# WHY: Make quick-and-dirty columns in console output.
# TODO: show a 3-column table header and a couple rows using \t
# print("Item\tQty\tPrice")

# -------------------------------------------------------
# Example 3: Printing backslashes with \\
# -------------------------------------------------------
# WHY: Windows file paths; escaping the escape character itself.
# TODO: show C:\Users\Kole\repo printed exactly
# print("C:\\Users\\Kole\\repo")

# -------------------------------------------------------
# Example 4: Quotes inside strings (\" and \')
# -------------------------------------------------------
# WHY: Print quoted dialogue or strings containing quotes without syntax errors.
# TODO: show: He said, "Hi!"
# print("He said, \"Hi!\"")

# -------------------------------------------------------
# Example 5: When NOT to use escapes: triple-quoted strings
# -------------------------------------------------------
# WHY: Long, readable blocks (banners/menus) are easier with triple quotes.
# TODO: demonstrate """...""" and note how to avoid a leading blank line.

# -------------------------------------------------------
# Common pitfalls
# -------------------------------------------------------
# - Forgetting that backslash starts an escape: "C:\new\test" breaks (\n, \t).
# - Overusing \n when a multi-line string would be clearer.
# - Mixing quote types poorly: prefer '...' with " inside, or "..." with \' or \" as needed.

# -------------------------------------------------------
# Micro-quiz
# -------------------------------------------------------
# 1) Print exactly: C:\Projects\python
# 2) Print: The file is called "report.txt"
# 3) Print a 2-row table using \t with headers Name,Score and one row: Kole,98

# -------------------------------------------------------
# Practice (filled by Kole later)
# -------------------------------------------------------
# 1) Print a small 3-line banner using \n.
# 2) Print a tabbed "receipt" with two items and prices.
# 3) Print the sentence: It\'s called "Escape Art".
# 4) Reprint your favorite Windows-style path (from Example 3) but using a raw string (we’ll introduce raw strings later; for now just leave a TODO placeholder).