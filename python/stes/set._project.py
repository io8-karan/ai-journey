# “Create student course system using sets”
student1_courses={"python","java","ai","soft computing"}
student2_courses={"python","java","ai","reactjs"}
student3_courses={"python","java","ai","javascriipt"}
print("Add Subject choose==1")
print("Remove subject choose==2")
print("search as subject choose==3")
print("union of subject choose==4")
print("common subject choose==5")
print("total count of subject choose==6")
print("exit choose==7")
while True:
    choice=int(input("Enter Your choice:")) 
    if choice==1:
        student1_courses.add("javascript")
        student2_courses.add("soft computing")
        student3_courses.add("reactjs")
        print(student1_courses)
        print(student2_courses)
        print(student3_courses)
    elif choice==2:
       print("Remove subject")
       student1_courses.remove("soft computing")
       student2_courses.remove("java")
       student3_courses.remove("ai")
       print(student1_courses)
       print(student2_courses)
       print(student3_courses)
    elif choice==3:
        search_subject = input("Enter subject to search: ")
        found = False
        if search_subject in student1_courses:
         found = True
        if search_subject in student2_courses:
         found = True
        if search_subject in student3_courses:
         found = True
        if found:
         print("Subject found")
        else:
         print("Subject not found")
    elif choice==4:
        print("union of subject")
        combined=student1_courses.union(student2_courses)
        final_combined=combined.union(student3_courses)
        print("union=",final_combined)
    elif choice==5:
         print("Intersection of subject") 
         intersection=student1_courses.intersection(student2_courses)
         final_intersection=intersection.intersection(student3_courses)
         print("common subject=",final_intersection) 
    elif choice==6:
        print("total courses is =",len(final_combined))
    elif choice==7:
        print("exit")
        break
else:
    print("invalid input")    