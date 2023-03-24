def WriteNumbers():
    outfile = open('numbers.txt','a')
    num1 = int(input('enter #1 '))
    num2 = int(input('enter #2 '))
    num3 = int(input('enter #3 '))
    sum = num1 + num2 + num3
    avg = sum/3

    outfile.write("the 1st number is "   + str(num1) + '\n')
    outfile.write("the 2nd number is "   + str(num2) + '\n')
    outfile.write("the 3rd number is "   + str(num3) + '\n')
    outfile.write("the avg number is "   + str(avg)  + '\n')
    outfile.write("the total number is " + str(sum)  + '\n')

    print ('data recorded')
WriteNumbers()

def ReadNumbers():
    infile = open('numbers.txt', 'r')
    content = infile.read()
    infile.close()

    print(content)

ReadNumbers()






