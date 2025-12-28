from abc import ABC ,abstractmethod

# Abstract class
class Greet(ABC):
    @property
    @abstractmethod
    def say_hello(self):
        pass

    # Abstract method
    @abstractmethod
    def personal_Info(self):
        pass

    # Concreate method
    def developed_idea(self):
        print("We can developed new idea about how they work !")


class English(Greet):
    def say_hello(self):
        return "Hello"
    def personal_Info(self):
        return "Shubham Patil"


g = English()
print(g.say_hello())
print(g.personal_Info())

