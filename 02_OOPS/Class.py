class Dog:
    # use for same data
    species = "Canine"  # Class attribute
    name = "anonymous" # if two variable same then Instance attribute higher precedence

    def __init__(self, name, age):
        # use for different data
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def __str__(self):
        return f"{self.name} ({self.age})"


dog1 = Dog("Buddy", 3)  # Create an instance of Dog
# controls what is returned when the object is printed
# print(dog1)
# print(dog1.name)
# print(dog1.age)
# print(dog1.species)
# print(Dog.species)
# print()

# dog1.name = "Max"
# print(dog1.name)
# Dog.species = "Canis Lupus Familiaris"
# print(dog1.species)

# dog1.species = "Feline"
# print(dog1.species)
# print()

# # delete properties
# print(dog1.age)
# del dog1.age


# # add new property
# dog1.city = "Oslo"
# print(dog1.city)
# print()


# dog2 = Dog("Charlie", 5)
# print(dog2.name)
# print(dog2.age)

