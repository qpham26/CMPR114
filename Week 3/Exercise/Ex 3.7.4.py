# This program will ask for the week sales to get the total and store them in a list
def main():
    days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    week_sales = []

    print('Enter the sales for the week.\n')

    index = 0
    for i in days_in_week:
        sale = float(input(f'Enter the sales for {i}: '))
        week_sales.append(sale)
        index += 1
    total_sales = total(week_sales)
    print(f'The total sales of the week is ${total_sales:,.2f} ')

    write('week_sales.txt', week_sales, total_sales)


def total(numbers):
    sum = 0
    for value in numbers:
        sum += int(value or 0)
    return sum


def write(name, sales, total):
    output = open(name, 'w')
    for money in sales:
        output.writelines(str(money) + '\n')
    output.writelines(f'Total sales: ${total: .2f}')

main()
