class Person:
    def __init__(self, name, age, gender, **kwargs):
        self.name = name
        self.age = age
        self.gender = gender
        super().__init__(**kwargs)

    def display_info(self):
        print(f"Name:{self.name} \n Age:{self.age} \n Gender:{self.gender}")

    def introduce(self):
        print(f"Hello ,I am {self.name}, and i am {self.age},years old.")


# Single Inheritance: Student inherits from Person

class Student(Person):
    def __init__(self, roll_no, course, semester, **kwargs):
        
        self.roll_no = roll_no
        self.course = course
        self.semester = semester
        super().__init__(**kwargs)
    def show_student_details(self):
        print(f"Name:{self.name} \n Age:{self.age} \n Gender:{self.gender} \n "
              f"Roll_no:{self.roll_no} \n Course:{self.course} \n Semester:{self.semester}")

    def study(self):
        print(f"Name:{self.name} with Roll_no {self.roll_no} is studing {self.course} ")


# Multilevel Inheritance: GraduateStudent -> Student -> Person

class GraduateStudent(Student):
    def __init__(self,research_topic, guide_name,**kwargs):
        super().__init__(**kwargs)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def research(self):
        print(f"{self.name} is working on a research topic {self.research_topic} "
              f"under the guidence of {self.guide_name}.")

    def thesis_submission(self):
        print(f"{self.name} submitted the thesis for final evaluation on topic {self.research_topic}.")

    def introduce(self):
        print(f"Hello! I am {self.name}. I am {self.age} years old and I am a {self.gender}. "
              f"I am a graduate student pursuing {self.course}. My research focuses on {self.research_topic}")


# Hierarchical Inheritance: Teacher and Staff both inherit from Person

class Teacher(Person):
    def __init__(self, employee_id, subject, salary,**kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def teach(self):
        print(f"The Teacher {self.name} teaches the subject {self.subject}")

    def evaluate_students(self):
        print(f"{self.name} is evaluating students' assignments, quizzes, and exams.")

    def introduce(self):
        print(f"Hello! I am {self.name}. I am {self.age} years old and I work as a teacher. "
              f"I teach {self.subject}.")


class Staff(Person):
    def __init__(self,department, duty, attendence,**kwargs):
        super().__init__(**kwargs)
        self.department = department
        self.duty = duty
        self.attendence = attendence

    def work(self):
        print(f"{self.name} is performing {self.duty} duties in the {self.department} department.")

    def attendances(self):
        print(f"{self.name}'s attendance has been marked successfully and "
              f"his attendence out of 100 is {self.attendence}.")


# Multiple Inheritance: SportsStudent inherits from Student and Sports

class Sports:
    def __init__(self, sports_name, medals,**kwargs):
        self.sports_name = sports_name
        self.medals = medals
        super().__init__(**kwargs)
    def practice(self):
        print(f"{self.name} is practicing {self.sports_name}.")

    def participate(self):
        print(f"{self.name} is participating in the competition.")


class SportsStudent(Student, Sports):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def display_sports_profile(self):
        print("===== Sports Student Profile =====")
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")
        print(f"Gender    : {self.gender}")
        print(f"Roll No   : {self.roll_no}")
        print(f"Course    : {self.course}")
        print(f"Semester  : {self.semester}")
        print(f"Sport     : {self.sports_name}")
        print(f"Medals    : {self.medals}")


# Hybrid Inheritance: TeachingAssistant inherits from GraduateStudent and Teacher

class TeachingAssistant(GraduateStudent, Teacher):
    def __init__(self, lab_name,**kwargs):
      super().__init__(**kwargs)
      self.lab_name=lab_name
    def conduct_lab(self):
        print(f"{self.name} is conducting a lab session in the {self.lab_name}.")

    def assist_professor(self):
        print(f"{self.name} is assisting the professor with lectures, lab sessions, and student guidance.")

    def introduce(self):
        print(f"Hello! I am {self.name}. I am a graduate student pursuing {self.course} "
              f"and also work as a Teaching Assistant in the {self.lab_name}.")

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
        s1 = Student(
    roll_no=101,
    course="B.Tech CSE",
    semester=5,
    name="Aman",
    age=19,
    gender="Male"
)
        s1.display_info()
        s1.introduce()
        s1.show_student_details()
        s1.study()

    elif choice == 3:
        g1 = GraduateStudent(
    research_topic="Machine Learning",
    guide_name="Dr. Sharma",
    roll_no=201,
    course="M.Tech AI",
    semester=2,
    name="Neha",
    age=23,
    gender="Female"
)
        g1.display_info()
        g1.show_student_details()
        g1.study()
        g1.research()
        g1.thesis_submission()
        g1.introduce()

    elif choice == 4:
        t1 = Teacher(
    employee_id="EMP101",
    subject="Python",
    salary=60000,
    name="Mr. Singh",
    age=40,
    gender="Male"
)
        t1.display_info()
        t1.teach()
        t1.evaluate_students()
        t1.introduce()

    elif choice == 5:
        st1 = Staff(
    department="Administration",
    duty="Office Work",
    attendence=95,
    name="Ramesh",
    age=35,
    gender="Male"
)
        st1.display_info()
        st1.work()
        st1.attendances()

    elif choice == 6:
        sp1 = SportsStudent(
    name="Karan",
    age=20,
    gender="Male",
    roll_no=301,
    course="B.Tech CSE",
    semester=6,
    sports_name="Cricket",
    medals=5)
        sp1.study()
        sp1.practice()
        sp1.participate()
        sp1.display_sports_profile()

    elif choice == 7:
        ta1 = TeachingAssistant(
    lab_name="AI Lab",
    research_topic="Deep Learning",
    guide_name="Dr. Mehta",
    roll_no=401,
    course="M.Tech AI",
    semester=2,
    employee_id="EMP201",
    subject="Python",
    salary=30000,
    name="Priya",
    age=24,
    gender="Female"
)
        ta1.display_info()
        ta1.research()
        ta1.teach()
        ta1.conduct_lab()
        ta1.assist_professor()
        ta1.introduce()

    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
