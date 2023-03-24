def main():
    num_emps = int(input('Enter the number of employee records: '))

    emp_file = open('employees.txt', 'w')

    for count in range(1, num_emps + 1):
        print('Enter data for employee #', count)

        name = input("Name: ")
        id_num = input("ID NUMBER: ")
        dept = input('DEPARTMENT: ')
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()
    print('recorded')

    # Open the file for reading
    emp_file = open('employees.txt', 'r')

    # Read the contents of the file and print each employee's data
    for line in emp_file:
        # Each employee's data is on three lines: name, ID number, and department
        name = line.strip()
        id_num = emp_file.readline().strip()
        dept = emp_file.readline().strip()

        print('Name:', name)
        print('ID Number:', id_num)
        print('Department:', dept)
        print()

    emp_file.close()


main()
