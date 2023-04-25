class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


# Create an object of the Pet class and prompt the user to enter the pet's information
name = input("Enter the name of your pet: ")
animal_type = input("Enter the type of animal that your pet is (e.g. 'Dog', 'Cat', 'Bird'): ")
age = int(input("Enter the age of your pet: "))

pet = Pet(name, animal_type, age)

# Display the pet's information using the accessor methods
print("Your pet's name is", pet.get_name())
print("Your pet is a", pet.get_animal_type())
print("Your pet is", pet.get_age(), "years old.")
