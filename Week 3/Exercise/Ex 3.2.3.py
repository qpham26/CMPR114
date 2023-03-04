#Program to collect data (nums of bugs) for 5 days
day_max = 5
sum = 0

for x in range(day_max):
    x += 1 #counter
    bugs = float(input("Enter the number of bugs for day #" + str(x) + ": "))
    sum = sum + bugs #calculate the sum

#return the total
print(f'The total bugs collected after 5 days: {sum}')

