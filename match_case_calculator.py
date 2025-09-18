#!/usr/bin/env python3

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

print(f"The result is {result}")
