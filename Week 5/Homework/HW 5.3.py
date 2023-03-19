#This program calculates monthly sales tax

def main():
    # Get the total sales for the month.
    total_sales = float(input('Enter the total sales for the month: $'))

    # County sales tax.
    county_tax = total_sales * 0.025

    # State sales tax.
    state_tax = total_sales * 0.05

    # Total sales tax.
    total_tax = county_tax + state_tax

    # Printing the results.

    print(f'County Sales Tax: ${county_tax:,.2f}')
    print(f'State Sales Tax: ${state_tax:,.2f}')
    print(f'Total Sales Tax: ${total_tax:,.2f}')

# Call the main function.
main()
