class Animal :
    def __init__(self , name ):
        self.name = name

    def info(self):
        print("Animal Name: " + self.name + "")

class Dog(Animal):
    def sound(self):
        print("Woof Woof")


dog = Dog("Buddy")
dog.info()
dog.sound()