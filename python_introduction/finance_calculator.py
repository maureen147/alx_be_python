# finance_calculator.py
# Simple personal finance calculator (no conditional statements)

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)  # add 5% interest

# Output results (formatted to 2 decimal places)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
