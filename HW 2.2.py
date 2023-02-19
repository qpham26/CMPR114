#User input information
num_people = int(input("Enter the number of people: "))
num_hotdog = int(input("Enter the number of hot dog per person: "))
total = num_people * num_hotdog
#Given data for the number of hot dogs and buns per pack
num_hotdogs_perpack = 10
num_buns_perpack = 8

#Calculate the remainders
hotdogs_rem = total%num_hotdogs_perpack
buns_rem = total%num_buns_perpack

#Calculcate the un-rounded number of packages
total_hotdogpacks = float(total/num_hotdogs_perpack)
total_bunspacks = float(total/num_buns_perpack)

#Logic to round-up the number of packages
if hotdogs_rem > 0:
    if float(round(total_hotdogpacks)) > float(total_hotdogpacks):
        total_hotdogpacks = round(total_hotdogpacks)
        print("The minimum number of packages of hot dogs required: " + str(total_hotdogpacks))
    else:
        total_hotdogpacks = round(float(total_hotdogpacks)) + 1
        print("The minimum number of packages of hot dogs required: " + str(total_hotdogpacks))
else:
    print("The minimum number of packages of hot dogs required: " + str(total_hotdogpacks))

if buns_rem > 0:
    if float(round(total_bunspacks)) > float(total_bunspacks):
        total_bunspacks = round(total_bunspacks)
        print("The minimum number of packages of buns required: " + str(total_bunspacks))
    else:
        total_bunspacks = round(float(total_bunspacks)) + 1
        print("The minimum number of packages of buns required: " + str(total_bunspacks))
else:
    print("The minimum number of packages of buns required: " + str(total_bunspacks))

left_over_dogs = total_hotdogpacks * float(num_hotdogs_perpack) - total
left_over_buns = total_bunspacks * float(num_buns_perpack) - total
print("The minimum number of left over hot dogs: " + str(left_over_dogs))
print("The minimum number of left over buns: " + str(left_over_buns))