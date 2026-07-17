# 📁 Q1 — File Handling (Level Up) "Student Record Management System banao using file handling in Python." 📋 Requirements: Ek Python program banao jisme 5 features hon: Add Student — student ka name, roll number, aur marks ek file students.txt mein save ho View All — file se saare students padhke table format mein print ho Search — roll number deke uss student ki details nikalo Update Marks — roll number deke uske marks update karo (file rewrite ho) Delete Student — roll number deke uss record ko file se hata do 📌 Constraints: Data format: roll,name,marks (comma separated) Agar file exist nahi karti toh gracefully handle karo (try-except) Har operation ke baad confirm message print ho 💡 Concepts covered: open(), read(), write(), append(), readlines(), writelines(), os.path.exists(), try-except



import os
result=os.path.defpath
print(result)

# for adding a students detail in file

def add_student(): 
 student_name=input("Enter Your Name=")
 while True:
  
  student_roll_no=(input("Enter your Roll no.="))
  
  if  student_roll_no.isdigit() and len(student_roll_no)<=10:
   print("valid ")
   break
  else:
   print("Enter Valid Roll No.")
 while True:
  marks=(input("Enter a marks="))
  if  marks.isdigit() and len(marks)<=2:
   print("valid ")
   break
  else:
   print("Enter Valid Marks")
 with open("d:/ai journey/python/mini project/myfile.txt" , "r+") as f:
  
  for data in f.readlines():
   new=data.strip()
   new=new.split(",")
   if student_roll_no == new[1]:
    print("|This Roll No. student already in system")
    break
  else:
   f.write( student_name + "," + student_roll_no + "," + marks + "\n")
   print("Add student sucessfully")
    
 # for viewing all the detail in file

def view_all(): 
  with open("d:/ai journey/python/mini project/myfile.txt" , "r") as f:
   print(f"{'name':<10}{'roll_no':<15}{'marks':<10}")
   print("="*30)
   for data in f.readlines():
    new=data.strip()
    new=new.split(",")
    print(f" {new[0]:<10}{new[1]:<15}{new[2]:<10}")


  # for searching a student based on roll no.

def search():
 seraching=input("Enter a Roll No. you Want to serach=")
 with open("d:/ai journey/python/mini project/myfile.txt" , "r") as f:
  for data in f.readlines():
     new=data.strip()
     new=new.split(",")
     if seraching == new[1]:
      print(f"{'name':<10}{'roll_no':<15}{'marks':<10}")
      print(f" {new[0]:<10}{new[1]:<15}{new[2]:<10}")
      break
  else:
    print("There is No student Found With This Roll No.")

# for updating student marks

def  update_marks(): 
  updated=input("Enter a Roll No. you Want to update marks=")
  mark=input("Enter a marks=")
  with open("d:/ai journey/python/mini project/myfile.txt" , "r+") as f:
   data1=[]
   for data in f.readlines():
     new=data.strip()
     new=new.split(",")
     if updated == new[1]:
       new[2]=mark
     new_data=(",".join(new) + "\n")
     data1.append(new_data)
  with open("d:/ai journey/python/mini project/myfile.txt" , "w") as f:
    f.writelines(data1)

 
 # for deleting student record

def  delete(): 
  deleted=input("Enter a Roll No. you Want to delete=")
  with open("d:/ai journey/python/mini project/myfile.txt" , "r") as f:
   data1=[]
   for data in f.readlines():
     new=data.strip()
     new=new.split(",")
     if deleted == new[1]:
      continue
     else:
      data1.append(",".join(new) + "\n")
  with open("d:/ai journey/python/mini project/myfile.txt" , "w") as f:
    f.writelines(data1)

# for choices to perform a task

def main():
    print("=" * 45)
    print("Student Record Management System")
    print("=" * 45)

    while True:
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4.Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("\nChoose option (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search()
        elif choice == "4":
           update_marks()
        elif choice == "5":
            delete()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
