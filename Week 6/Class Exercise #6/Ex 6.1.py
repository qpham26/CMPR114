# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Write to file
file = open("user_info.txt", "w")
file.write(f"{first_name} {last_name}, {age}")
file.close()

# Read from file
file = open("user_info.txt", "r")
content = file.read()
file.close()

# Display the content
print(content)
