#Grade data program
#ask user for full name and exam grades
name = input("Enter your full name: ")
try:
    midterm = float(input("Enter your midterm grade: "))
    final = float(input("Enter your final exam grade: "))
except ValueError:
    print("Error: Invalid input. Please enter a number for the grades.")
else:
    # calculate average grade and determine letter grade
    average = (midterm + final) / 2
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # write results to file
    with open("grades.txt", "a") as file:
        file.write(f"{name}: {average:.2f} ({letter_grade})\n")

    # read results from file and display to user
    with open("grades.txt", "r") as file:
        print(file.read())
