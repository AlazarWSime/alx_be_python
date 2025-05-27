monthly_income = input("Enter your monthly income: " )
total_monthly_expenses = input("Enter your total monthly expenses: ")


monthly_savings = float(monthly_income) - float(total_monthly_expenses)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Projected davings after one year, with interest, is: ${projected_savings} ")
