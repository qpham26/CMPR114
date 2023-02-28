month = float(input("Enter the current month: "))

if 0 < month <= 3:
    print("The month is in the first quarter.")
elif 3 < month <= 6:
    print("The month is in the second quarter.")
elif 6 < month <= 9:
    print("The month is in the third quarter.")
elif 9 < month <= 12:
    print("The month is in the forth quarter.")
else:
    print("Invalid input. Please enter a valid month between 1 and 12.")