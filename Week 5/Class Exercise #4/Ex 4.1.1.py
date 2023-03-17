# This program demonstrates two functions that
# have local variables with the same name.
def main():
    # Call the texas function.
    texas()
    # Call the california function.
    california()


# Definition of the texas function. It creates
# a local variable named birds.
def texas():
    birds = float(input('Enter the number of birds in Texas: '))
    print(f'texas has {birds} birds.')


# Definition of the california function. It also
# creates a local variable named birds.
def california():
    birds = float(input('Enter the number of birds in California: '))
    print(f'california has {birds} birds.')


# Call the main function.
main()