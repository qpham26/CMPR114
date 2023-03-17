# Enter the monthly automobile related costs then display
# the total monthly cost and the annual cost

def main():
    # Enter the monthly costs for each expense.
    loan_payment = float(input('Enter the monthly loan payment: '))
    insurance = float(input('Enter the monthly insurance cost: '))
    gas = float(input('Enter the monthly gas cost: '))
    oil = float(input('Enter the monthly oil cost: '))
    tires = float(input('Enter the monthly tire cost: '))
    maintenance = float(input('Enter the monthly maintenance cost: '))

    # Calculate the total monthly cost
    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance

    # Calculate the total annual cost
    total_annual_cost = total_monthly_cost * 12

    # Display
    print(f'Total monthly cost: ${total_monthly_cost:,.2f}')
    print(f'Total annual cost: ${total_annual_cost:,.2f}')

# Call the main function.
main()
