def sales():
    salary = float(input("Enter your salary: "))
    num_days = int(input("Enter the days of sales: "))
    total_sales = 0
    sales_file = open('sales.txt', 'a')

    for count in range(1, num_days +1):
        sales = float(input('Enter the sales for day #' + str(count) + ": "))
        sales_file.write(str(sales) + '\n')
        total_sales += sales

    if total_sales > 1000:
        commission = total_sales * 0.1
        salary += commission

    sales_file.write("Salary with commission: " + str(salary) + '\n')
    sales_file.close()
    print('Sales recorded')

def ReadSales():
    sales_file = open ('sales.txt', 'r')
    line = sales_file.readline()
    while line !='':
        print(line.strip())
        line = sales_file.readline()
    sales_file.close()

sales()
ReadSales()
