# syntax error : Programmer responsible for correct the syntax

# x=10
# if x ==10
#     print("x is 10")

# print"Hello friends"


# # Runtime Errors :
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print('The division is: ', x/y)


# f = open('non_existent_file.txt', 'r')
# print(f.read())


"""Error : bug occur before compilation
Types of Errors :
Compile time error : bug occur during compilation
    1. Syntax Error : error arise due to incorrect syntax
    
Run time error : bug occur during execution of program 
    2. logical error/Semantic error : program runs but give incorrect output . 
                                  compiler cannot detect logical error 
    3. Runtime Error : error occur during execution of program
                      Exception: An event that occurs during the execution of a program that disrupts the normal flow of instructions

Exception:
 type of Exception:
 A} Build in Exception:
        1. ZeroDivisionError : division by zero 
        2. FileNotFoundError : file not found
        3. IndexError : index out of range
        4. KeyError : key not found in dictionary
        5. ValueError : invalid value
        6. TypeError : invalid data type
        7. ImportError : module not found
        8. AttributeError : attribute not found
        9. SyntaxError : wrong syntax
        10. I/O Error : some input output operation fails
        11. KeyboardInterrupt : program interrupted by user
        12. EOFError : end of file reached
        13. MemoryError : out of memory
        14. NameError : variable not defined
        
B} User Defined Exception :
        1. Custom Exception created by user by inheriting Exception class
      
Exception Handling : Exception handling is a mechanism to handle runtime errors
                    so that the normal flow of the application can be maintained.  
                    In Python, we use -
                    try, 
                    except,
                    else,
                    finally 
                        blocks to handle exceptions. 
              
"""
# Build in Exception Handling Example :

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
try:
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception:
    print("An error occurred during division.")
else:
    print("No exceptions occurred. The operation was successful.")
finally:
    print("Resource cleanup can be done here.")
    print("Execution completed.")


# user defined Exception Handling Example : raise keyword is used to raise an exception
class NegativeValueError(Exception):
    """Custom exception for negative values."""
    pass
def calculate_square_root(value):
    if value < 0:
        raise NegativeValueError("Cannot calculate square root of a negative number.")
    return value ** 0.5
try:
    num = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}.")
except NegativeValueError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("Execution completed.")


#  another user defined Exception Handling Example :
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass
def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return True
try:
    user_age = int(input("Enter your age: "))
    if validate_age(user_age):
        print("Age is valid.")
except InvalidAgeError as e:
    print(f"Error: {e}")
finally:
    print("Execution completed.")


#  customized message print
age = int(input("Enter your age:"))
try:
    if age < 0:
        raise Exception("Age cannot be negative")
    elif age >= 18:
        print("You are eligible for voting ")
    else:
        print("not eligible for voting")
except Exception as e:
    print("Error:", e)

# proper Exception message display
age = int(input("Enter your age:"))
if age < 0:
    raise Exception("Age cannot be negative")
elif age >= 18:
    print("You are eligible for voting ")
else:
    print("not eligible for voting")
