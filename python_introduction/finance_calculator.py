monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total montly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)
projected_saving = monthly_savings * 12 + (monthly_savings * 12*0.05)

print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving:.0f}.")
