# Question 1
# Create
# Employee
# Requirements
# constructor
# class variable
# class method alternative constructor
# Input
# "Aman,60000,Python"
# Need object
# name
# salary
# departmen
# Also
# Print __dict__
# Use help()
# Print dir()

class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    @classmethod
    def from_str(clr,string):
        name,salary,department=string.split(",")
        return clr(name,int(salary),department)
    def show(self):
        print(f"Name: {self.name}" + "\n" + f"Salary : {self.salary}" + "\n" + f"Department : {self.department}")
while True:
    number=int(input("Enter 1 to create Employee object or 0 to exit and 2 for showing help: "))
    if number==1:
        strings=input("Enter Employee details in format 'name,salary,department': ")
        e=Employee.from_str(strings)
        e.show()
    elif number==2:
        print(e.__dict__)
        print(help(Employee))
    elif number==0:
        print("Exiting the program.")
        break

