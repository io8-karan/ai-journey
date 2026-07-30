from abc import ABC, abstractmethod
import time

# BASE CLASS

class Person(ABC):
    def __init__(self,id,name,age,gender,phone_no,email,password):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        self.phone_no=phone_no
        self.email=email
        self.__password=password
    
    

    def change_password(self,enter_password , new_password):
        while True:
         if self.__password == enter_password:
            self.__password = new_password 
            print("Your New Password=",new_password)
            break
         else:
            print("Old password Mismatch,Enter a password again")
    @property
    def password(self):
        return self.__password
    
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def display_profile(self):
        pass

    @property
    def age(self):
      return self.__age
    @age.setter
    def age(self,new_age):
      if 0<new_age<=120:
       self.__age=new_age
      else:
         print("Invalid age ")

# DECORATOR SECTION 
def log_activity(fxn):
   def wrapper(*args,**kwargs):
      print("[LOG]")
      print(f"Method Name : {fxn.__name__}")
      current=time.strftime("%Y-%m-%d %H-%M-%S")
      print(f"Cureent Time:{current}")
      start=time.time()
      print(f"Start Time:{start}")
      result=fxn(*args,**kwargs)
      end=time.time()
      print(f"End Time={end}")
      total=end-start
      print(f"Total Program execution time:{total}")
      time.sleep(3)
      print("Finished Successfully")
      return result
   return wrapper

# DOCTOR CLASS

class Doctor(Person):
    def __init__(self,specialization,department,qualification,licence_number,experience,appointments,salary,**kwargs):
        super().__init__(**kwargs)
        self.specialization=specialization
        self.department=department
        self.qualification=qualification
        self.licence_number=licence_number
        self.experience=experience # setter call
        self.appointments=appointments
        self.salary=salary # setter call
 
# experience validation

    @property
    def experience(self):
     return self.__experience

    @experience.setter
    def experience(self, value):
        if value >= 0:
            self.__experience = value
        else:
            print("Experience cannot be negative")

  # Salary Validation
    @property
    def salary(self):
       return self.__salary
    @salary.setter
    def salary(self,new_salary):
       if new_salary > 0:
          self.__salary = new_salary
       else:
          print("Salary Can't be negative")
          
     
    def display_profile(self):
       print("-"*10)
       print("Doctor Profile")
       print("-"*10)
       print(f"Name={self.name}")
       print(f"Id: {self.id}")
       print(f"Id: {self.age}")
       print(f"Gender: {self.gender}")
       print(f"Phone NO.: {self.phone_no}")
       print(f"Email: {self.email}")
       print(f"Specialization: {self.specialization}")
       print(f"Department: {self.department}")
       print(f"Licence Number: {self.licence_number}")
       print(f"Experience: {self.experience}") # getter call
       print(f" Total Appointments :{self.appointments}")
       print(f"Salary:{self.salary}") # getter call
    def login(self):
       while True:
        passwords=input("Enter your Password=")
        if passwords == self.password:
            print("login Succesfully")
            break
        else:
            print("password wrong ,Enter a valid pass ")


class MedicalRecord:
   @property
   def records(self):
      return self.__records
   def __init__(self):
      self.__records=[] 
    
    
   def add_record(self):
      num=int(input("Enter how many visiters are want to add="))
      for i in range(1,num+1):
            
            r2 = input("Enter Medical History: ") 
            r3 = input("Enter Diagnosis: ")
            r4 = input("Enter Prescriptions: ") 
            r5 = input("Enter Allergies: ")
            record = {
               
                "medical_history": r2,
                "diagnosis": r3,
                "prescriptions": r4,
                "allergies": r5
            }
 
            
            self.__records.append(record)    
            
   def update_record(self):
     numb=int(input("Enter your choice you want to update"))
     index= numb-1
     if 0<=index < len(self.__records):
        visit=self.__records[index]
        print("old data=",visit)
        r3 = input("Enter Diagnosis: ")
        r4 = input("Enter Prescriptions: ") 
        r5 = input("Enter Allergies: ")
        visit.update({
                "diagnosis": r3,
                "prescriptions": r4,
                "allergies": r5
            })


   
   def show_record(self):
      return self.__records
   
# patients section

class Patient(Person):
  
      
   def __init__(self,blood_group,**kwargs):
      super().__init__(**kwargs)
      self.blood_group=blood_group
      self.medical_record=MedicalRecord(
         
      )
   def display_profile(self):
        print("-" * 10)
        print("Patient Profile")
        print("-" * 10)
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")          # property getter
        print(f"Gender: {self.gender}")
        print(f"Phone No.: {self.phone_no}")
        print(f"Email: {self.email}")
        print(f"Blood Group: {self.blood_group}")
        print(f"Medical Record ")
        print(self.medical_record.show_record())
   def login(self):
    
    while True:
     enter_password=input("ENter your Password= ")
     if enter_password == self.password:
         print("Login Successfully")
         break
     else:
         print("Try Again")
class Appointment:
    #appointment section

    def __init__(self, doctor, patient, date, time, status):
        self.doctor = doctor      # Doctor object
        self.patient = patient    # Patient object
        self.date = date
        self.time = time
        self.status = status
    def display_appointment(self):
        print("-" * 10)
        print("Appointment Details")
        print("-" * 10)
        print(f"Doctor: {self.doctor.name}")
        print(f"Patient: {self.patient.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Status: {self.status}")
    @log_activity
    def book_appointment(self):
       self.status="confirmed"
       print("Appointment Confirm Successfully")
       
       self.display_appointment()
    @log_activity
    def cancel_appointment(self):
       self.status="Cancelled"
       print("Appointment Cancelled Successfully")
       
       self.display_appointment()

# BILL SECTION 
class Bill:
   @property
   def amount(self):
      return self.__amount
   @amount.setter
   def amount(self,new_amount):
      while True:
       if new_amount >=0:
         self.__amount = new_amount
         break
       else:
         print("Enter Valid Amount")
   def __init__(self,amount,doctor,patient):
      self.amount=amount
      self.doctor=doctor
      self.patient=patient
   @log_activity
   def generate_bill(self):
      print("BILL")
      print(f"Doctor={self.doctor}")
      print(f"Patient={self.patient}")
      print(f"Amount={self.amount}")

# PAYMENT SECTION

class Payment(ABC):
   @abstractmethod
   def pay(self):
      pass
class CashPayment(Payment):
   def pay(self):
      print("Cash Payment Successfull")
class CardPayment(Payment):
   def pay(self):
      print("Card Payment Successfull")
class UpiPayment(Payment):
   def pay(self):
      print("Upi Payment Successfull")

class Hospital:
   def  __init__(self,hospital_name,hospital_id,address,contact_no):
    self.hospital_name = hospital_name
    self.hospital_id = hospital_id
    self.address = address

    self.contact_no = contact_no
    self.doctors=[]
    self.patients=[]
    self.appointments=[]
    self.bills=[]

   def add_doctor(self,doctor):
    self.doctors.append(doctor)
 
   def remove_doctor(self,doctor):
    if len(self.doctors) != 0:
     if doctor in self.doctors:
      self.doctors.remove(doctor)
     else:
        print("Teh Associated doctor not found ")
    else:
      print("Teh Associated doctor not found ")

   def register_patient(self,patient):
    self.patients.append(patient)

   def book_appointment(self,appointment):
    self.appointments.append(appointment)

   def cancel_appointment(self,appointment):
    if len(self.appointments) != 0:
     if appointment in self.appointments:
      self.appointments.remove(appointment)
     else:
        print("Teh Associated Appointment record not found ")
    else:
        print("Teh Associated Appointment record not found ")
   

   def add_bill(self,bill):
    self.bills.append(bill)

   def display_hospital(self):
    print("-" * 10)
    print("Hospital Details")
    print("-" * 10)

    print(f"Hospital Name: {self.hospital_name}")
    print(f"Hospital ID: {self.hospital_id}")
    print(f"Address: {self.address}")
    print(f"Contact No: {self.contact_no}")

    print("\n--- Records ---")
    print(f"Total Doctors: {len(self.doctors)}")
    print(f"Total Patients: {len(self.patients)}")
    print(f"Total Appointments: {len(self.appointments)}")
    print(f"Total Bills: {len(self.bills)}")

# object creation

print("\n--- Smart Hospital Management System ---")
hospital_name = input("Enter Hospital Name: ")
hospital_id = input("Enter Hospital ID: ")
address = input("Enter Hospital Address: ")
contact_no = input("Enter Hospital Contact Number: ")

hospital = Hospital(
         hospital_name=hospital_name,
         hospital_id=hospital_id,
         address=address,
         contact_no=contact_no)
while True: 

    
    print("1. For Add Doctor Details")
    print("2. For Show Doctor Details")
    print("3. For Add Patient Details")
    print("4. For Show Patient Details")
    print("5.  For Add Appointment Details")
    print("6.  For Show Appointment Details")
    print("7. For Add Bill Details")
    print("8. For Add Medical Record Details")
    print("9. Hospital Detail")
    print("10. Exit")

    
    
    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n--- Adding Doctor Details ---")

        doctor_id = input("Enter Doctor ID: ")
        doctor_name = input("Enter Doctor Name: ")
        doctor_age = int(input("Enter Doctor Age: "))
        doctor_gender = input("Enter Doctor Gender: ")
        doctor_phone = input("Enter Doctor Phone Number: ")
        doctor_email = input("Enter Doctor Email: ")
        doctor_password = input("Enter Doctor Password: ")

        specialization = input("Enter Specialization: ")
        department = input("Enter Department: ")
        qualification = input("Enter Qualification: ")
        licence_number = input("Enter Licence Number: ")
        experience = int(input("Enter Experience: "))
        appointment = int(input("Enter Total no. of  appointment: "))
        salary = int(input("Enter Salary: "))

        # doctor=Doctor(doctor_id ,doctor_name,doctor_age,doctor_gender,doctor_phone,doctor_email,doctor_password,specialization,department,qualification,licence_number,experience,appointment,salary) # problem order ot match so instead this use keyword arguments

        doctor=Doctor(
            id=doctor_id,
            name=doctor_name,
            age=doctor_age,
            gender=doctor_gender,
            phone_no=doctor_phone,
            email=doctor_email,
            password=doctor_password,
            specialization=specialization,
            department=department,
            qualification=qualification,
            licence_number=licence_number,
            experience=experience,
            appointments=appointment,
            salary=salary)
        hospital.add_doctor(doctor)
        
        
    elif choice == "2":
        print("\n--- Doctor Details ---")
       
        print("Enter 1 for dispplay docotr detail")
        print("Enter  2 for login status")
        choices=int(input("Enter your choice="))
        if choices == 1:
            if len(hospital.doctors) != 0:
             doctor.display_profile()
            else :
               print("please add Dcotor Detail First")
        elif choices ==2:
           if len(hospital.doctors) != 0:
            doctor.login()
           else :
               print("please add Dcotor Detail First")
        else:
           print("Invalid Input")
        
        
    elif choice == "3":
        print("\n--- Adding Patient Details ---")

        patient_id = input("Enter Patient ID: ")
        patient_name = input("Enter Patient Name: ")
        patient_age = int(input("Enter Patient Age: "))
        patient_gender = input("Enter Patient Gender: ")
        patient_phone = input("Enter Patient Phone Number: ")
        patient_email = input("Enter Patient Email: ")
        patient_password = input("Enter Patient Password: ")

        blood_group = input("Enter Blood Group: ")
        
        patient=Patient(
          blood_group=blood_group,
          id=patient_id,
          name=patient_name,
          age=patient_age,
          gender=patient_gender,
          phone_no=patient_phone,
          email=patient_email,
          password=patient_password)
        hospital.register_patient(patient)

  

    elif choice == "4":
        print("\n---  Patient Details ---")
        print("Enter 1 for dispplay patient detail")
        print("Enter  2 for login status")
        choices=int(input("Enter your choice="))
        if choices == 1:
           if len(hospital.patients) !=0:
            patient.display_profile()
           else:
              print("First Add Patient Detail")
        elif choices ==2:
            if len(hospital.patients) !=0:
             patient.login()
            else:
               print("First Add Patient Detail")
        else:
           print("Invalid Input")


    elif choice =="5":
        if len(hospital.patients) != 0 and len(hospital.doctors) != 0: 

         print("\n---Adding Appointment Details ---")

         date = input("Enter Appointment Date: ")
         times = input("Enter Appointment Time: ")
         status = input("Enter Appointment Status: ")

         appointment = Appointment(
          doctor=doctor,
          patient=patient,
          date=date,
          time=times,
          status=status)
         hospital.book_appointment(appointment)
         
        else:
           print("Please add First Docotr And Patient")

    elif choice =="6":
         if len(hospital.appointments) !=0:
          print("\n---Appointment Details ---")
          print("Enter 1 for dispplay Appointment detail")
          print("Enter  2 for Book Appointment")
          print("Enter 3 for cancel Appointment")
          choices=int(input("Enter your choice="))
          if choices == 1:
            appointment.display_appointment()
          elif choices ==2:
           appointment.book_appointment()
          elif choices ==3:
           appointment.cancel_appointment()
          else:
           print("Invalid input")
         else:
            print("Please add first appointment detail")

    elif choice =="7":
       if len(hospital.patients) != 0 and len(hospital.doctors) != 0: 


         print("\n--- Bill Details ---")

         amount = int(input("Enter Bill Amount: "))

         bill = Bill(
         amount=amount,
         doctor=doctor,
         patient=patient)

         bill.generate_bill()
         hospital.add_bill(bill)
       else:
           print("Please Add First Docotr And Patient")

    elif choice =="8":
       print("Medical Record")
       print("Enter 1 for add record")
       print("Enter 2 for update record")
       print("Enter 3 for show record")
       choices = int(input("Enter Your Choice= "))
       if choices ==1:
          patient.medical_record.add_record()
       elif choices ==2:
        patient.medical_record.update_record()
       elif choices == 3:
        patient.medical_record.show_record()
       else:
        print("Invalid choice")

    elif choice == "9":
       print("Hospital Detail")
       print("Enter 1 for Delete Doctor")
       print("Enter 2 for CAncel appointment")
       print("Enter 3 for display hospital details")
       choices=int(input("Enter a choice="))
       if choices == 1:
        hospital.remove_doctor(doctor)
       elif choices ==2:
        hospital.cancel_appointment(appointment)
       elif choices ==3:
        hospital.display_hospital()
    elif choice =="10":
        print("Program Closed")
        break


    else:
        print("Invalid Choice")