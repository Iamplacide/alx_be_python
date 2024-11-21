income = input("Enter your monthly income: ")
expenses = input("Enter your total montly expenses: ")

saving = float(income) - float(expenses)
projected = round ((saving * 12) + (saving * 12 * 0.05))

print(f'Your monthly savings are ${saving}.')

print(f"Projected savings after one year, with interest, is: ${projected}.")
