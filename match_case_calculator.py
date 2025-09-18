# File: alx_be_python/control-flow/match_case_calculator.py
"""Simple Calculator using match-case."""

def main():
    # Ask for first and second numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Ask for operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Match-case block
    match operation:
        case "+":
            print(f"The result is {num1 + num2}")
        case "-":
            print(f"The result is {num1 - num2}")
        case "*":
            print(f"The result is {num1 * num2}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"The result is {num1 / num2}")
        case _:
            print("Invalid operation. Please choose +, -, *, /.")

if __name__ == "__main__":
    main()
