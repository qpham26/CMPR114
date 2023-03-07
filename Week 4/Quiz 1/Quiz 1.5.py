#Program takes a range of sales, and shows the commission
#and add the commission to the salary
sales = float(input("Enter your sale: "))

if 50000 <= sales <= 70000:
    print(f'Your total sale is ${sales:,.2f}')
    salary = 70000.00*
    print(f'Your commission of 10% is ${sales:,.2f}')
elif 70000 <= sales <= 80000:
    print(f'Your total sale is ${sales:,.2f}')
    sales = sales * .2
    print(f'Your commission of 20% is ${sales:,.2f}')
elif 90000 <= sales:
    print(f'Your total sale is ${sales:,.2f}')
    sales = sales * .3
    print(f'Your commission of 30% is ${sales:,.2f}')
else:
    print(f'Your total sale is ${sales}')
    print("Value of sales if not listed in the provided table")

