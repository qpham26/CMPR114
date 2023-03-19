#Property Tax calculator program

def main():
    # Prompt the user to enter the actual value of the property.
    actual_value = float(input('Enter the actual value of the property: '))

    # Calculate the assessment value at 60%.
    assessment_value = actual_value * 0.6

    # Calculate the property tax
    property_tax = assessment_value / 100 * 0.72

    # Display the final answers
    print("The assessment value of the property is: $", format(assessment_value, ',.2f'))
    print("The property tax for the property is: $", format(property_tax, ',.2f'))

# Call the main function to start the program.
main()
