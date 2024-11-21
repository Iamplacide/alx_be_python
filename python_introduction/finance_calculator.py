monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total montly expenses: ")

monthly_savings = (float(monthly_income) - float(monthy_expenses)
projected = round ((monthly_savings * 12) + (monthly_savings * 12 * 0.05))

print(f'Your monthly savings are ${monthly_savings}.')

print(f"Projected savings after one year, with interest, is: ${projected}.")
