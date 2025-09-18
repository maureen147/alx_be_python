#!/usr/bin/env python3

# Prompt user for input - MUST use exact wording
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match-case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    case _:
        result = "Invalid operation"

# Output result - MUST use exact wording
print(f"The result is {result}")
