#Sort a tuple by the sum of each inner list
input_tup = ([2, 20], [44, 1], [3, 13])

sorted_tup = sorted(input_tup, key=lambda x: sum(x))

print(sorted_tup)
