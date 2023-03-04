# While loop that take a number,
# multiply the number by 10,
# continue until the product is > 100

product_max = 100
product = 1
while product < 100:
    num = float(input("Enter a number: "))
    product = num * 10
    print(f'The product is: {product}')

