class Maths:
    @staticmethod
    def addNumber( num1,num2):
        return num1 + num2

# res = Maths.addNumber(32,33)
# print(res)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        return age > 18

    def __del__(self):
        print("Object Destroyed")

# result = Person.isAdult(17)
# print(result)


person = Person("Ajay",32)
print(person.isAdult(18))
# delete objects
del person

