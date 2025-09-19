#!/usr/bin/env python3
"""
multiplication_table.py
Prompt user for a number (variable name `number`) and print its multiplication
table from 1 to 10 in format: "X * Y = Z".
"""

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")


