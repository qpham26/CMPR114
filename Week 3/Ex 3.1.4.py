name = ['Nhat', 'Pham']
for x in range(len(name)):
    if x % 2 == 0:
        first_name = name[x]
        break
for x in range(len(name)):
    if x % 2 != 0:
        last_name = name[x]
        break

print("Your full name is " + last_name + " " + first_name)

