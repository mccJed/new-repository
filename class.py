# Class definition for Person
class Person:
    # Initializer with private variables
    def __init__(self, name, address, age, phone):
        self._name = name
        self._address = address
        self._age = age
        self._phone = phone

    # Get   
    def get_info(self):
        return f"Name: {self._name} Address: {self._address} Age: { self._age} Phone: {self._phone}"
    
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age

    def get_phone(self):
        return self._phone

    # Set
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_age(self, age):
        self._age = age

    def set_phone(self, phone):
        self._phone = phone

# Instances
person1 = Person("Jed Ledermann", "123 Maple Street", 22, "123-4567")
person2 = Person("Jace Stewart", "123 Oak Street", 23, "234-5678")
person3 = Person("Jacob Kimbelle", "123 Pine Street", 25, "345-6789")

# Display
print(person1.get_info())

print(person2.get_info())

print(person3.get_info())