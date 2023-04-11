# Midterm question 3: add codes to write to the coffee text file.
# User to enter their favorite coffee brand, prod num and price

# Open and get user input in append mode
with open("coffee.txt", "a") as file:
    brand = input("Enter your favorite coffee brand: ")
    prod_num = input("Enter the product number: ")
    price = input("Enter the price: ")

    # write the new coffee entry to the file
    file.write(f"\n{brand},{prod_num},{price}")

print("New entry added to coffee.txt!")

