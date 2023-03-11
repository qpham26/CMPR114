#Find the sum of all integers of a tuple
test_tup = ([17, 28], [93, 11], [20, 17])

total = 0
for inside_list in test_tup:
    for num in inside_list:
        total += num

print("The total of all integers in the tuple is: ",total)
