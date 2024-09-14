monthly_income = float(input("Enter yur monthly income: "))
monthly_expense = float(input("Enter yur montly expenses: "))

monthly_saving = monthly_income - monthly_expense
projected_saving = monthly_saving * 12 + (monthly_saving * 12*0.05)

print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")
