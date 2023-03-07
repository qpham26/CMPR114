#Program takes a range of sales, and shows the commission
#and add the commission to the salary
sales = float(input("Enter your sale: "))

if 50000 <= sales < 70000:
    salary = 70000.00 * 1.1
    print(f'Your total sale is ${sales:,.2f}')
    print(f'Your salary is ${salary:,.2f}')
elif 70000 <= sales < 90000:
    salary = 80000.00 * 1.2
    print(f'Your total sale is ${sales:,.2f}')
    print(f'Your salary is ${salary:,.2f}')
elif 90000 <= sales:
    salary = sales * 1.3
    print(f'Your total sale is ${sales:,.2f}')
    print(f'Your salary is ${salary:,.2f}')
else:
    print(f'Your total sale is ${sales}')
    print("Value of sales if not listed in the provided table")





