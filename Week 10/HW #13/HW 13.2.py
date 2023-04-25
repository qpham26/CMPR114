class Person:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, mailing_list):
        super().__init__(name, address, phone_number)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

# Usage:
customer1 = Customer("Nick Robinson", "111 Shadow St", "222-1234", 5555, True)
print("Name:", customer1.name)
print("Address:", customer1.address)
print("Phone Number:", customer1.phone_number)
print("Customer Number:", customer1.customer_number)
print("Mailing List:", customer1.mailing_list)
