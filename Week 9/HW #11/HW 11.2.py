class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_job_title(self):
        return self.job_title

# create three Employee objects
susan = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
mark = Employee("Mark Jones", 39119, "IT", "Programmer")
joy = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# display the data for each employee
print("Name:", susan.get_name())
print("ID Number:", susan.get_id_number())
print("Department:", susan.get_department())
print("Job Title:", susan.get_job_title())
print()

print("Name:", mark.get_name())
print("ID Number:", mark.get_id_number())
print("Department:", mark.get_department())
print("Job Title:", mark.get_job_title())
print()

print("Name:", joy.get_name())
print("ID Number:", joy.get_id_number())
print("Department:", joy.get_department())
print("Job Title:", joy.get_job_title())
