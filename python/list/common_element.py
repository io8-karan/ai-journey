# find common element in lists 
list1=[]
list2=[]
common=[]
num=int(input("enter:"))
for i in range(num):
     list1.append(int(input("enter the no. in list:")))
print(list1)
num=int(input("enter:"))
for i in range(num):
     list2.append(int(input("enter the no. in list:")))
print(list2)
for i in list1:
     for j in list2:
          if i==j:
               common.append(i)
if len(common)==0:
     print("no common element ")
else:
     print(common)
