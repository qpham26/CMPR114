with open("things.txt", "w") as file:
    file.write("lion\n")
    file.write("apple\n")
    file.write("Japan\n")

# Open the file for reading
with open("things.txt", "r") as file:
    # Loop through each line in the file and print it
    for line in file:
        print(line.strip())