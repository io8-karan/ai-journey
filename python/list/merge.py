#merge of two list 
list1=[]
list2=[]
number=int(input("enter the no. of element in list:"))
for i in range(number):
    list1.append(int(input("enter no. in list1:")))
    list2.append(int(input("enter a no. in list2:")))
print(list1)
print(list2) 
list=list1+list2
print("merged list is:")
print(list) 
