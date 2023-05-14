class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_rate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__hourly_rate = hourly_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_shift(self):
        return self.__shift

    def get_hourly_rate(self):
        return self.__hourly_rate


# Program to create a list of 3 ProductionWorker objects and display their details
worker_list = []

for i in range(3):
    print(f"Enter details for ProductionWorker {i+1}:")
    name = input("Name: ")
    number = input("Employee Number: ")
    shift = int(input("Shift (1 for Day Shift, 2 for Night Shift): "))
    hourly_rate = float(input("Hourly Pay Rate: "))
    worker = ProductionWorker(name, number, shift, hourly_rate)
    worker_list.append(worker)
    print()

print("Production Worker Details:")
for i, worker in enumerate(worker_list):
    print(f"ProductionWorker {i+1}:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    if worker.get_shift() == 1:
        print("Shift: Day Shift")
    else:
        print("Shift: Night Shift")
    print(f"Hourly Pay Rate: ${worker.get_hourly_rate():.2f}")
    print()
