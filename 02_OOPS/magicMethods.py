class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "This is a Person object"

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return "Person(name='Vaibhav', age=22)"

    def __call__(self):
        print("Called")

# p = Person("Vaibhav", 22)
# print(p)
# print((len(p)))
# print(repr(p))
# p()


class Number:
    def __init__(self, value,marks):
        self.value = value
        self.marks = marks

    def __add__(self, other):
        return self.value + other.value

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __del__(self):
        print("Object destroyed")

a = Number(10,98)
b = Number(20,98)
print(a + b)
# print()
# print(a == b)
# print(a < b)

print(dir(int))





