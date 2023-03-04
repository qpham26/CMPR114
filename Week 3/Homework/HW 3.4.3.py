#This program will add all positive numbers,
# and end when a negative number is entered

#Initialize Variables
sum = 0
num = 0

#Loop to calculate sum:
while num >= 0:
    sum += num
    num = float(input('Input a positive number: '))

#Display the result
print(f'The sum of all the numbers is: {sum}')
