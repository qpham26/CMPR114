# Enter a distance in kilometers, then converts that distance to miles.

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    miles = kilometers_to_miles(kilometers)
    print(f'{kilometers:,.2f} kilometers is equal to {miles:,.2f} miles.')

def kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

# Call the main function.
main()