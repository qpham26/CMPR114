num = float(input("Enter the number of packages: "))
price = 99
if 10 <= num <= 19:
    discount = 0.1
elif 20 <= num <= 49:
    discount = 0.2
elif 50 <= num <= 99:
    discount = 0.3
elif num >= 100:
    discount = 0.4
else:
    discount = 0

total_discount = discount*price*num
total = num*99-total_discount
print("Your amount of discount is: $" + str(total_discount))
print("Your total is: $" + str(total))