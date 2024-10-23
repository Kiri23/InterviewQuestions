"""
Problem: Find Matching Parentheses

Purpose:
Given a string containing nested parentheses and the position of an opening parenthesis,
find its matching closing parenthesis.

Method:
- Uses a stack-like array to keep track of parentheses
- When finding an opening parenthesis '(', add its position to the array
- When finding a closing parenthesis ')', remove the last opening position from array
- When array becomes empty, we've found our matching pair

Key Components:
- Input: 
  * str: String containing parentheses
  * inputIndex: Position of the opening parenthesis we want to match

- Variables:
  * parenthensis[]: Array to track positions of opening parentheses
  
Example Usage:
str = "(a(bc))"
inputIndex = 0  # First parenthesis
# Should find the matching closing parenthesis position
"""

str = "Sometimes (when i nest them (my parenthical) too much (like this (and this))) they get confusing"
str2 = "(a(bc)"
inputIndex = 0
parenthensis = [inputIndex]

for i, char in enumerate(str2):
    if i > inputIndex:
        print(f"char: {char}, index: {i}")
        if char == ")":
            parenthensis.pop()
        elif char == "(":
            parenthensis.append(i)
    if len(parenthensis) == 0:
        print(i)

if len(parenthensis) > 0:
    print(parenthensis)
