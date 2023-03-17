# Define global variables.
num1 = 0
num2 = 0
num3 = 0
total = 0
average = 0

def main():
    global num1, num2, num3
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    calc()

#Function to calculate sum and ave
def calc():
    global total, average
    total = num1 + num2 + num3
    average = total / 3
    result()

def result():
    print(f'The sum of {num1}, {num2}, and {num3} is {total}.')
    print(f'The average of {num1}, {num2}, and {num3} is {average}.')

# Call the main function.
main()

