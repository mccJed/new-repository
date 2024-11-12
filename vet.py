# Class Definition
class Pet:
    # Class variable
    vet_name = "Helping Paws Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self._owner_first_name = owner_first_name
        self._owner_last_name = owner_last_name
        self._pet_id = pet_id
        self._pet_name = pet_name
        self._pet_type = pet_type

    # Get
    def get_owner_first_name(self):
        return self._owner_first_name

    def get_owner_last_name(self):
        return self._owner_last_name

    def get_pet_id(self):
        return self._pet_id

    def get_pet_name(self):
        return self._pet_name

    def get_pet_type(self):
        return self._pet_type

    # Set
    def set_owner_first_name(self, first_name):
        self._owner_first_name = first_name

    def set_owner_last_name(self, last_name):
        self._owner_last_name = last_name

    def set_pet_id(self, pet_id):
        self._pet_id = pet_id

    def set_pet_name(self, pet_name):
        self._pet_name = pet_name

    def set_pet_type(self, pet_type):
        self._pet_type = pet_type

    # Method to display all pet information
    def display_pet_info(self):
        print(f"Owner Name: {self._owner_first_name} {self._owner_last_name}")
        print(f"Pet ID: {self._pet_id}")
        print(f"Pet Name: {self._pet_name}")
        print(f"Pet Type: {self._pet_type}")
        print(f"Veterinary Clinic: {Pet.vet_name}")
        print()

#Instances
pet1 = Pet("Jed", "Ledermann", 101, "Miley")
pet2 = Pet("Zia", "Rogers", 102, "Mort", "Cat")
pet3 = Pet("Amie", "Ledermann", 103, "Ginny")

# Using setter methods to update details for pet
pet1.set_pet_name("Lola.")
pet1.set_pet_type("Dog")

# Property Existence Check
def check_property(pet_object, property_name):
    exists = hasattr(pet_object, f"_{property_name}")
    print(f"Property '{property_name}' exists in {pet_object.get_pet_name()}: {exists}")
    return exists

#Display Information for Each Pet
print("Pet 1 Info:")
pet1.display_pet_info()

print("Pet 2 Info:")
pet2.display_pet_info()

print("Pet 3 Info:")
pet3.display_pet_info()

#Show Examples of check_property
check_property(pet1, "owner_first_name") 
check_property(pet2, "pet_id")          
check_property(pet3, "owner_middle_name")          

