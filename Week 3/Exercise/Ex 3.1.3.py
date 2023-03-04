#Return even and odd numbers
#List of numbers
num_list = [1,2,3,4,5,6,7,8,9,10]

#Find and return all odd numbers
for x in range(len(num_list)):
    if num_list[x] % 2 != 0:
        print(str(num_list[x]) + " is an odd number")

print("\n")

#Find and return all even numbers
for x in range(len(num_list)):
    if num_list[x] % 2 == 0:
        print(str(num_list[x]) + " is an even number")


