# Python Assignments: Object-Oriented Programming

class Test:
    x1=10
    x2=78
    def printval():
        print("hallow world")
    def __init__(self):
        print("hellow")
t1=Test()
t2=Test()
print(type(t1))
# 1. Write a Python program to create a User class with 3 properties: name, age, email.
class User:
    name=str()
    age=int()
    email=str()
    def __init__(self,N,A,S):
        self.name=N
        self.age=A
        self.email=S
    def display_info():
        print()
u1=User("harsh",18,"harsh90064@gmail.com")


# 2. Write a Python program to create a User class with a method to greet the user.

# 3. Write a Python program to create 2 objects of the User class and assign different values.

# 4. Write a Python program to initialize default values for a User object using the __init__ method.

# 5. Write a Python program to delete the age property of the User.

# 6. Write a Python program to create 3 User objects and find the youngest of all.

# 7. Write a Python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) 
#    and 2 methods (showConfig() to print values, __init__() to initialize values).

# 8. WRT 7th Question, create 3 Laptop objects and add them to a list in sorted order based on RAM size.

# 9. Write a Python program to create a School class with 3 instance variables and 1 class variable.

# 10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method 
#     to initialize instance object variables. Also, define instance methods to input and display field values.