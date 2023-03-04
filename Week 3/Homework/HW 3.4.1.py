# This program calculates distance travel for each hour

# Initialize variables
speed = float(input('What is the speed of the vehicle in mph? '))
hours = float(input('How many hours has it traveled? '))
print('Hour         Distance Traveled')

distance = 0.0
counter = 1.0
#For loop to create the values
while counter <= hours:
    #calculate the distance travel each hour
    distance = distance + speed
    #Display the hour vs distance
    print(f'{counter}                 {distance}')
    counter += 1