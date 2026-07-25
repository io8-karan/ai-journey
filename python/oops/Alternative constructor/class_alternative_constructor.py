# 1. Class Method (Alternative Constructor)

# Create a Student class.

# Requirements:

# __init__(name, age)
# Create a class method from_string() that accepts
# "Rahul-20"

# and returns a Student object.

# Output

# Name : Rahul
# Age : 20

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Name: {self.name}" + "\n" + f"Age : {self.age}")
    @classmethod
    def from_str(cls,string):
        name,age=string.split("-")
        return cls(name,int(age))
    
   
s=Student.from_str("Rahul-20")
s.show()


# 2. dir()

# Create a class Laptop.

# Questions

# Print dir(Laptop)
# Print dir(object)
# Which methods are inherited from object?

class Laptop:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def show(self):
        print(f"Brand: {self.brand}" + "\n" + f"Model : {self.model}")

l = Laptop("Dell", "XPS 13")
l.show()
print(dir(Laptop))
print("\n")
print(dir(object))

# 3. dict

# Create

# class Employee:

# with

# name
# salary
# department

# Questions

# Print object __dict__
# Print class __dict__
# Add
# emp.location="Delhi"

# Print __dict__ again.

class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
e1=Employee("Rahul",50000,"IT")
print(e1.__dict__)
print(Employee.__dict__)
e1.location="Delhi"
print(e1.__dict__)

# 4. help()

# Create a class with proper docstrings.

# class Calculator

# Methods

# add()
# subtract()

# Use

# help(Calculator)

# Observe the output.

class Calculator:


    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self, a, b):
       
        return a + b

    def subtract(self, a, b):
      
        return a - b

help(Calculator)

# 5. super()

# Create

# Animal

# and

# Dog

# Use

# super().__init__()

# Print

# Animal Created
# Dog Created
class Animal:
    def __init__(self):
     print("Animal Created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Created")
d=Dog()

# 6. Magic Method

# Create

# Book

# with pages.

# Overload

# __add__
# Book1=120 pages
# Book2=250 pages

# Output

# 370

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
book1=Book(120)
book2=Book(250)
total_pages=book1+book2
print(total_pages)
