# Number Analysis Program
# Receive and store a series of 20 numbers in a list
# and display the lowest, highest, total, and average

# Initial variables
num_list = []
counter = 0
total = 0
length = 20

# Loop to store the numbers to a list
while counter < length:
    num = float(input(f'Enter a number: '))
    num_list.append(num)
    counter += 1
    total = total + num

# Calculate the desired outputs
average = total/len(num_list)
highest = max(num_list)
lowest = min(num_list)

# Display the outputs
print(f'The lowest number is {lowest:,.2f}')
print(f'The highest number is {highest:,.2f}')
print(f'The total of the numbers is {total:,.2f}')
print(f'The average of the numbers is {average:,.2f}')
