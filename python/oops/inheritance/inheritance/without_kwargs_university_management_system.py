class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display_info(self):
        print(f"Name:{self.name} \n Age:{self.age} \n Gender:{self.gender}")
    def introduce(self):
        print(f"Hello ,I am {self.name}, and i am {self.age},years old.")

# single Inheritance Student class inherit from base class Person

class Student(Person):
    
    def __init__(self,name,age,gender,roll_no,course,semester):
        super().__init__(name,age,gender)
        self.roll_no=roll_no
        self.course=course
        self.semester=semester
    def show_student_details(self):
        print(f"Name:{self.name} \n Age:{self.age} \n Gender:{self.gender} \n Roll_no:{self.roll_no} \n Course:{self.course} \n Semester:{self.semester}")
    def study(self):
        print(f"Name:{self.name} with Roll_no {self.roll_no} is studing {self.course} ")

#  Multilevel Inheritance  Graduate Student class inherit from  class Student and Student inherit form Person base class

class GraduateStudent(Student):
    def __init__(self,name,age,gender,roll_no,course,semester,research_topic,guide_name):
        super().__init__(name,age,gender,roll_no,course,semester)
        self.research_topic=research_topic
        self.guide_name=guide_name
    def research(self):
        print(f"{self.name} is working on a research topic {self.research_topic} under the guidence of {self.guide_name}.")
    def thesis_submission(self):
     print(f"{self.name} submitted the thesis for final evaluation on topic {self.research_topic}.")
    def introduce(self):
     print(f"Hello! I am {self.name}. I am {self.age} years old and I am a {self.gender}. I am a graduate student pursuing {self.course}. My research focuses on {self.research_topic}")

#  Hierarchical Inheritance  Teacher and staff class inherit from  class Person

class Teacher:
    def __init__(self,name,age,gender,employee_id,subject,salary):
        super().__init__(name,age,gender)def __init__(self,name,age,gender,employee_id,subject,salary)
        self.employee_id=employee_id
        self.subject=subject
        self.salary=salary
    def teach(self):
        print(f"The Teacher {self.name} teaches the subject {self.subject}")
    def evaluate_students(self):
     print(f"{self.name} is evaluating students' assignments, quizzes, and exams.")
    def introduce(self):
     print(f"Hello! I am {self.name}. I am {self.age} years old and I work as a teacher. I teach {self.subject}.")

class Staff:
     def __init__(self,name,age,gender,department,duty,attendence):
        super().__init__(name,age,gender)
        self.department=department
        self.duty=duty
        self.attendence=attendence
     def work(self):
        print(f"{self.name} is performing {self.duty} duties in the {self.department} department.")
     def attendances(self):
        print(f"{self.name}'s attendance has been marked successfully and his attendence out of 100 is {self.attendence}.")

# Multiple Inheritance

class Sports:
   def __init__(self,sports_name,medals):
      self.sports_name=sports_name
      self.medals=medals
   def practice(self):
       print(f"{self.name} is practicing {self.sports_name}.")
   def participate(self):
    print(f"{self.name} is participating in the {self.event} competition.")
class SportsStudent(Student,Sports):
    def __init__(self,name,age,gender,roll_no,course,semester,sports_name,medals):
       super.__init__(name,age,gender,roll_no,course,semester,sports_name,medals)
    def display_sports_profile(self):
     print("===== Sports Student Profile =====")
     print(f"Name      : {self.name}") 
     print(f"Age       : {self.age}")
     print(f"Gender    : {self.gender}")
     print(f"Roll No   : {self.roll_no}")
     print(f"Course    : {self.course}")
     print(f"Semester  : {self.semester}")
     print(f"Sport     : {self.sport}")
     print(f"Event     : {self.event}")

# Hybrid Inheritance 

class TeachingAssistant(GraduateStudent,Teacher):
       def __init__(self,name,age,gender,roll_no,semester,employee_id,subject,salary,lab_name):
          super.__init__(name,age,gender,roll_no,semester,employee_id,subject,salary)
          self.lab_name=lab_name
       def conduct_lab(self):
          print(f"{self.name} is conducting a lab session in the {self.lab_name}.") 
       def assist_professor(self):
          print(f"{self.name} is assisting the professor with lectures, lab sessions, and student guidance.")
       def introduce(self):
          print(f"Hello! I am {self.name}. I am a graduate student pursuing {self.course} and also work as a Teaching Assistant in the {self.lab_name}.")
         

while True:
    print("\n===== University Management System =====")
    print("1. Person")
    print("2. Student")
    print("3. Graduate Student")
    print("4. Teacher")
    print("5. Staff")
    print("6. Sports Student")
    print("7. Teaching Assistant")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
     p1 = Person("Rahul", 20, "Male")
     p1.display_info()
     p1.introduce()

    elif choice == 2:
     s1 = Student("Aman", 19, "Male", 101, "B.Tech CSE", 5)
     s1.display_info()          # inherited from Person
     s1.introduce()             # inherited (or overridden if you override it)
     s1.show_student_details()
     s1.study()

    elif choice == 3:
        g1 = GraduateStudent(
    "Neha", 23, "Female",
    201,
    "M.Tech AI",
    2,
    "Machine Learning",
    "Dr. Sharma"
)

g1.display_info()
g1.show_student_details()
g1.study()
g1.research()
g1.thesis_submission()
g1.introduce()

    elif choice == 4:
        # create Teacher object and call methods

    elif choice == 5:
        # create Staff object and call methods

    elif choice == 6:
        # create SportsStudent object and call methods

    elif choice == 7:
        # create TeachingAssistant object and call methods

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")