#Find the sum of a tuple using while loop
test_tup = (15, 20, 123, 47, 26, 81)

i= 0
sum = 0

while i < len(test_tup):
    sum = sum + test_tup[i]
    i += 1

print(sum)
