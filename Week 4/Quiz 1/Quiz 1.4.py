#Program takes a range of sales and shows the commission
sales = float(input("Enter your sale: "))

if 50000 <= sales <= 60000:
    print(f'Your total sale is ${sales:,.2f}')
    sales = sales * .1
    print(f'Your commission of 10% is ${sales:,.2f}')
elif 70000 <= sales <= 80000:
    print(f'Your total sale is ${sales:,.2f}')
    sales = sales * .2
    print(f'Your commission of 20% is ${sales:,.2f}')
elif 90000 <= sales <= 100000:
    print(f'Your total sale is ${sales:,.2f}')
    sales = sales * .3
    print(f'Your commission of 30% is ${sales:,.2f}')
elif sales > 100000: #Assume 30% commission for sales over 100K
    print(f'Your total sale is ${sales:,.2f}')
    sales = sales * .3
    print(f'Your commission of 30% is ${sales:,.2f}')
else:
    print(f'Your total sale is ${sales}')
    print("You are not eligible for a commission")

