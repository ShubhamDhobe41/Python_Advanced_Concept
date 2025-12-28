class Company:
    name = "ABC"

    @classmethod
    def show(cls):
        print(cls.name)

    @staticmethod
    def add(a,b):
        return  a * b

    def sub(self,a,b):
        return a - b

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

company = Company()
# company.show()
# res = company.add(23,43)
# print(res)
# res = company.sub(23,33)
# print(res)
company.welcome()


# print(Company.name)
# Company.show()
# res = Company.add(23,23)
# print(res)
# res = Company.sub(0,33,43)
# print(res)