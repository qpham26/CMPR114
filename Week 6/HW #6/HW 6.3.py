# Open the file in write mode
with open("number_list.txt", "w") as file:
    # Loop through the numbers 1 to 100 and write each one to a line in the file
    for number in range(1, 101):
        file.write(str(number) + "\n")
