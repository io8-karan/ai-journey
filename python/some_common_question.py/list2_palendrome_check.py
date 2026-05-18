list=[]
list.append(input("Enter list element 1:"))
list.append(input("Enter list element 2:"))
list.append(input("Enter list element 3:"))
print("User Entered List is:",list)
rev=list[::-1]
print("Reversed List is:",list)
if(list==rev): 
  print("List is palindrome")
else:
  print("List is not palindrome")
  
  
  #also done by using copy in which we create a one copy of list rev=list.copy() and then reverse the copy list and check with original list