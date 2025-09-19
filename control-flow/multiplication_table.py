#!/usr/bin/env python3
"""multiplication_table.py
Prompt user for a number (variable name `number`) and print its multiplication
table from 1 to 10 in format: "X * Y = Z".
"""

def _fmt(x):
    # Show whole floats without trailing .0
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

def main():
    s = input("Enter a number to see its multiplication table: ")
    try:
        # prefer int when possible so table shows "5" not "5.0"
        number = int(s)
    except ValueError:
        try:
            number = float(s)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

    for i in range(1, 11):
        product = number * i
        print(f"{_fmt(number)} * {i} = {_fmt(product)}")

if __name__ == "__main__":
    main()

