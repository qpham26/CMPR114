# Midterm question 4: Expense report program

# Prompt user for expenses and write to text file
with open("expenses.txt", "w") as file:
    categories = ["Rent", "Gas", "Food", "Clothing", "Car payment"]
    for category in categories:
        expense = input(f"Enter your expense for {category}: ")
        file.write(f"{category}: {expense}\n")

# Read and print contents of text file
with open("expenses.txt", "r") as file:
    contents = file.read()
    print(contents)
