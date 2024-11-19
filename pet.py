class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind  
        self._breed = breed
        self._name = name

    # Getter and Setter for kind
    def get_kind(self):
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    # Getter and Setter for breed
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    # Getter and Setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # method
    def print_details(self):
        print(f"Pet Details: Kind: {self._kind}, Breed: {self._breed}, Name: {self._name}")

# instances
pet1 = Pet(kind="Dog", breed="Doodle", name="Barbara")
pet2 = Pet(kind="Cat", breed="Siamese", name="Sister")
pet3 = Pet(kind="Bird", breed="Parrot", name="Polly")

pet1.print_details()
pet2.print_details()
pet3.print_details()

#choose one
print(f"Name of pet1 using getattr: {getattr(pet1, 'get_name')()}")


