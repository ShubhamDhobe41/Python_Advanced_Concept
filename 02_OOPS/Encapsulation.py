# example of Private access modifier in Encapsulation
class Person:
    # constructor
    def __init__(self,name,age):
        # private variable
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"The Person name is  {self.__name} and the age is {self.__age}")

    # private method
    def __Hello(self):
       print("Hello")

    def callMethod(self):
        self.__Hello()

person = Person("Ajay",32)
# person.callMethod()
# person.display_info()


# print(dir(Person))


# example of protected access modifier in Encapsulation
# Base Class
class Person:
    # constructor
    def __init__(self,name,age):
        self._name = name
        self._age = age

# Derived Class
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def display_info(self):
        print(f"The Person name is  {self._name} and the age is {self._age}")

# student = Student("Ajay",88)
# student.display_info()


