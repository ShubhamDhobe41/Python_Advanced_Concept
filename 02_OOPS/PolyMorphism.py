# method overloading example in python
class Ws:
    def displayInfo(selfself,name="" ):
        print("Welcome :",name)
obj = Ws()
# obj.displayInfo("Rahul")
# obj.displayInfo("manoj")
# obj.displayInfo()

# method overriding example in python
class Parent:
    def show(self):
        print("Parent class method called")
class Child(Parent):
    def show(self):
        super().show()
        print("Child class method called")
obj1 = Child()
# obj1.show()



class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat:

    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()


print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))
