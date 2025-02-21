# Financial Management Script for Nabiha
month = input("Enter the month you are recording salary for: ")
salary = float(input("Enter your total salary for this month ($): "))

savings_percentage = float(input("Enter the percentage of salary to allocate to savings: "))
rent_percentage = float(input("Enter the percentage of salary to allocate to rent: "))
electricity_percentage = float(input("Enter the percentage of salary to allocate to electricity: "))

savings = (savings_percentage / 100) * salary
rent = (rent_percentage / 100) * salary
electricity = (electricity_percentage / 100) * salary

total_expenses = savings + rent + electricity
remaining_salary = salary - total_expenses

yearly_rent = rent * 12
yearly_electricity = electricity * 12

salary_squared = salary ** 2

extra_savings = 50
leftover_after_extra_savings = extra_savings / savings if savings != 0 else "N/A"

print("\n====================== Financial Summary ======================")
print(f"Month: {month}")
print(f"Total Salary: ${salary:.2f}")
print("---------------------------------------------------------------")
print(f"Savings: ${savings:.2f} ({savings_percentage}%)")
print(f"Rent: ${rent:.2f} ({rent_percentage}%)")
print(f"Electricity: ${electricity:.2f} ({electricity_percentage}%)")
print("---------------------------------------------------------------")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Salary After Expenses: ${remaining_salary:.2f}")
print("---------------------------------------------------------------")
print(f"Estimated Yearly Rent: ${yearly_rent:.2f}")
print(f"Estimated Yearly Electricity: ${yearly_electricity:.2f}")
print("---------------------------------------------------------------")
print(f"Fun Calculation - Your Salary Squared: ${salary_squared:.2f}")
print(f"Extra Savings of $50 divided by savings: {leftover_after_extra_savings}")
print("===============================================================")
print("Financial summary completed. Have a great month ahead! 😊")
