#this program will add to the list and delete from the list

def main():
    names = ['Howard', 'Jamie', 'Jill']
    #element    0         1        2
    print(' the list before the insert or remove ')
    print(names)
    NameRemove = input(' enter the name to remove ')
    names.insert(0, 'Joe') #insert the new name at element 0, moving or shifting element 0 to 1
    names.remove(NameRemove) #removename from the list
    print('the list after the insert ')
    print(names)

#main()

def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum+=value #total numbers in the list

    average = sum/len(numbers)
    print('the total is ', sum,' the average is ', average)
    with open("numbers.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")
total()
