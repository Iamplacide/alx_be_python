income = int(input("Enter your monthly income : "))
expenses = int(input("Enter your total montly expenses : "))

saving = income - expenses
projected = round ((saving * 12) + (saving * 12 * 0.05))

print(f'Your monthly savings are ${saving}.')

print(f"Projected savings after one year, with interest, is: ${projected}.")
