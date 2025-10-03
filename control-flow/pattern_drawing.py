#!/usr/bin/env python3
"""
pattern_drawing.py
Prompt for a positive integer (variable name `size`) and draw a square
pattern of asterisks using a while loop and a nested for loop.
"""

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1

