#This program take a gross salary input and add 10%

base_salary = float(input("Enter your base salary: "))
bonus = 0.1
total_comp = base_salary * (1+bonus)
total_comp = "{:,.2f}".format(total_comp)
print(f"Your total compensation is ${total_comp}")
