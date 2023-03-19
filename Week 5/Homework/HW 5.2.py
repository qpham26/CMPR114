# This program calculates the income generated from ticket sales

def ticket():
    # Prompt the user for the number of tickets sold for each seating category
    num_a = int(input('Enter the number of Class A seats sold: '))
    num_b = int(input('Enter the number of Class B seats sold: '))
    num_c = int(input('Enter the number of Class C seats sold: '))

    # Calculate the income generated from ticket sales for each seating category
    income_a = num_a * 20
    income_b = num_b * 15
    income_c = num_c * 10

    # Calculate the total income generated from ticket sales
    total_income = income_a + income_b + income_c

    # Display the total income generated from ticket sales
    print(f'Total income generated from ticket sales: ${total_income:.2f}')

def main():
    # Call the ticket function
    ticket()

main()
