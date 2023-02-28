#Break condition and variables
count = 0
total = float(0)

#While loop to take 4 inputs
while count < 4:
    #sales and commission rate input
    sales = float (input("Enter the amount of sales: "))
    comm_rate = float (input("Enter the commission rate: "))
    #calculate commission
    commission = sales * comm_rate
    total = total + sales + commission
    count += 1

#Printing the final sum
print("The total sales with commission: $" + str(total))
