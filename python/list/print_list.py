# #   # create a list and print all no. 
old_list=[]
number=int(input("enter how many no. is list "))
print(number)
for i in range(number):
 old_list.append(int(input("enter a no.")))
print(old_list)     
new_list=list(set(old_list))
print(new_list)
