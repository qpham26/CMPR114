#Program to create and store 10 random numbers to a txt file
import random

# Generate 10 random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for i in range(10)]

# Write the numbers to a text file
with open("random_numbers.txt", "w") as file:
    for num in random_numbers:
        file.write(str(num) + "\n")

# Read the contents of the file and display them
with open("random_numbers.txt", "r") as file:
    contents = file.read()
    print(contents)
