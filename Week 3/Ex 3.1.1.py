#Setup variables
max_temp = 102.5
count = 0
sum_temp = 0

#Prompt the user to enter the set of 4 temperatures in the while loop
while count <4:
    temp = float(input("Enter the temperature for today: "))
    #break condition when temp is over 102.5
    if temp >= max_temp:
        print("A temperature over 102.5 is detected. Computing total and average")
        break
    sum_temp += temp
    count += 1

#logic to calculate average only when 4 input is received, else stop the program
if count == 4:
    average = sum_temp/4
    print("Total = " + str(sum_temp))
    print("Average = " + str(average))
else:
    print("Not enough valid input. Need 4 inputs to compute.")

