# This program calculates the sum of a series
# of numbers entered by the user.

MAX = 5 # The maximum number

# Initialize an accumulator variable
total = 0.0

# Explain what we are doing.
print('This program calculates the sum and average of')
print(f'{MAX} numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number
# Display the total and average of the numbers.
average = total/MAX
print(f'The total is {total}.')
print(f'The average is {average}.')