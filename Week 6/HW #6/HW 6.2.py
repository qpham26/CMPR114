# Open the file in read mode
file = open("things.txt", "r")

# Read all lines from the file into a list
lines = file.readlines()

# Close the file
file.close()

# Print the lines from the list
for line in lines:
    print(line.strip())
