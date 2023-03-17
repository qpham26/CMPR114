#This program receives the hours worked and the hourly rate
#then calculate the gross pay

def calculate_gross_pay(hours_worked, hourly_pay):
    gross_pay = hours_worked * hourly_pay
    return gross_pay

def main():
    hours_worked = float(input('Enter the hours worked: '))
    hourly_pay = float(input('Enter the hourly pay: '))
    gross_pay = calculate_gross_pay(hours_worked, hourly_pay)
    print(f'The gross pay is ${gross_pay:,.2f}.')

# Call the main function.
main()



